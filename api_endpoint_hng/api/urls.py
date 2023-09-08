from django.urls import path
from .views import GetInfo

urlpatterns = [
    path('api/', GetInfo.as_view(), name='get_info'),
]