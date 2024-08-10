import os
import zipfile
from core.api.base.views import G3WAPIView, Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404

from dam_monitor.models import Site
from .serializers import UploadShapefileSerializer
from .permissions import UploadShapefilePermission

import logging

logger = logging.getLogger('g3wadmin.debug')


class GetRelativeOrbit(G3WAPIView):
    """Get Relative Orbit of a site
    """

    def get(self, request, site_id):
        try:
            site = get_object_or_404(Site, id=site_id)
        except ValidationError as e:
            return Response({"error": e.message}, status=HTTP_400_BAD_REQUEST)

        return Response({"relative_orbit": site.relative_orbit})


class UploadShapefileAPIView(G3WAPIView):
    """
    API for uploadin shapefile
    """
    permission_classes = (
        UploadShapefilePermission,
    )
    serializer_class = UploadShapefileSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            validated_data = serializer.validated_data
            client_id = validated_data['client_id']
            site_id = validated_data['site_id']
            model_run_id = validated_data['model_run_id']
            file = validated_data['file']
            extract_dir = f"/shared-volume/project_data/{client_id}/{site_id}/{model_run_id}/"
            os.makedirs(extract_dir, exist_ok=True)
            # zip_path = f"/shared-volume/project_data/{client_id}/{site_id}/{model_run_id}/{file.name}"
            with zipfile.ZipFile(file, 'r') as zip_ref:
                # Extract all files to the specified directory
                zip_ref.extractall(extract_dir)

                # Get the list of extracted files
                extracted_files = zip_ref.namelist()
                shp_filename = [f for f in extracted_files if f.endswith('.shp')]
                if len(shp_filename) > 0:
                    shp_filename = shp_filename[0]
                    return Response({"filepath": os.path.join(extract_dir, shp_filename)})
                else:
                    return Response({"message": "No .shp file"}, status=HTTP_400_BAD_REQUEST)
