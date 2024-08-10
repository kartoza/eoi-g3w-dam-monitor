from rest_framework.permissions import BasePermission


class UploadShapefilePermission(BasePermission):
    """ Check permission for uploading Shapefile data """

    def has_permission(self, request, view):
        return request.user.is_superuser
