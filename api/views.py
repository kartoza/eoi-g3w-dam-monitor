# coding=utf-8
"""" API qplotly widgets

.. note:: This program is free software; you can redistribute it and/or modify
    it under the terms of the Mozilla Public License 2.0.

"""

__author__ = 'lorenzetti@gis3w.it'
__date__ = '2020-09-23'
__copyright__ = 'Copyright 2015 - 2020, Gis3w'

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from django.core.exceptions import ValidationError

from core.api.authentication import CsrfExemptSessionAuthentication
from dam_monitor.models import Site
from django.shortcuts import get_object_or_404

import logging

logger = logging.getLogger('g3wadmin.debug')


class GetRelativeOrbit(APIView):
    """Get Relative Orbit of a site
    """

    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication, BasicAuthentication]

    def get(self, request, site_id):
        try:
            site = get_object_or_404(Site, id=site_id)
        except ValidationError as e:
            return Response({"error": e.message}, status=HTTP_400_BAD_REQUEST)

        return Response({"relative_orbit": site.relative_orbit})
