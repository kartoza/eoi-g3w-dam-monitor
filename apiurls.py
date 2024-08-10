from django.urls import path
from .api.views import GetRelativeOrbit, UploadShapefileAPIView

urlpatterns = [
    path("api/get-relative-orbit/<str:site_id>/", GetRelativeOrbit.as_view(), name="get-site-relative-orbit"),
    path("api/upload-shapefile/", UploadShapefileAPIView.as_view(), name="uplaod-shapefile"),
]