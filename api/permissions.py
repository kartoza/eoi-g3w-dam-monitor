# coding=utf-8
""""

.. note:: This program is free software; you can redistribute it and/or modify
    it under the terms of the Mozilla Public License 2.0.

"""

__author__ = 'lorenzetti@gis3w.it'
__date__ = '2020-09-23'
__copyright__ = 'Copyright 2015 - 2020, Gis3w'

from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import BasePermission
from qdjango.models.projects import Layer
from qdjango.api.projects.permissions import ProjectRelationPermission
from qplotly.models import QplotlyWidget


class DamMonitorPermission(ProjectRelationPermission):
    """
    API permission for Dam Permission urls
    Allows access only to users have permission view_project on project
    """