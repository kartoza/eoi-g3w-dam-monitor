from django.contrib import admin
from .models import (
    MonitoringFrequency,
    MonitoringPoint,
    MonitoringSample,
    Client,
    Site,
    ModelRun
)

class ModelRunAdmin(admin.ModelAdmin):
    list_display = ('site', 'date')
    list_filter = ('site', )


class MonitoringPointAdmin(admin.ModelAdmin):
    list_display = (
        'run_date',
        'site_name',
        'client_name',
        'height',
        'vel',
        'v_stdev',
        'coherence'
    )
    list_filter = ('model_run__site__name', )

    def site_name(self, obj):
        return obj.model_run.site.name

    def client_name(self, obj):
        return obj.model_run.site.client.name

    def run_date(self, obj):
        return obj.model_run.date


class MonitoringPointSampleAdmin(admin.ModelAdmin):
    list_display = (
        'monitoring_point',
        'date',
        'value'
    )
    list_filter = ('monitoring_point__model_run__site__name', )


admin.site.register(MonitoringFrequency)
admin.site.register(MonitoringPoint, MonitoringPointAdmin)
admin.site.register(MonitoringSample, MonitoringPointSampleAdmin)
admin.site.register(ModelRun, ModelRunAdmin)
admin.site.register(Site)
admin.site.register(Client)
