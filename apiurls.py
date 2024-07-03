from django.urls import path
from .api.views import GetRelativeOrbit

urlpatterns = [
    path("api/dam_monitor/<str:site_id>/", GetRelativeOrbit.as_view(), name="get-site-relative-orbit"),
]