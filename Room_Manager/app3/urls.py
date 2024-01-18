
from django.urls import path
from .views import ServerStatusView, UpdateServerView

urlpatterns = [
    path('status/', ServerStatusView.as_view(), name='status'),
    path('update/', UpdateServerView.as_view(), name='update'),
]
