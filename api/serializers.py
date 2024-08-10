import zipfile
from rest_framework import serializers
from rest_framework.serializers import Serializer, FileField, IntegerField


# Serializers define the API representation.
class UploadShapefileSerializer(Serializer):
    client_id = IntegerField()
    site_id = IntegerField()
    model_run_id = IntegerField()
    file = FileField()

    def validate_file(self, value):
        if not zipfile.is_zipfile(value):
            raise serializers.ValidationError("The uploaded file is not a valid ZIP file.")
        return value

    class Meta:
        fields = ['client_id', 'site_id', 'model_run_id', 'file']
