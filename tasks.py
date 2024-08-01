from django.utils import timezone
from datetime import timedelta
from huey import crontab
from huey.contrib.djhuey import lock_task, periodic_task
from dam_monitor.models import ModelRun
from qdjango.models import Project


@periodic_task(crontab(hour=1))
def remove_monitoring_results():
    """
    Delete project and model run that is older than 30 days
    """
    now = timezone.now()
    date_threshold = now - timedelta(days=30)
    ModelRun.objects.filter(date__lt=date_threshold).delete()
    Project.objects.filter(created__lt=date_threshold).delete()