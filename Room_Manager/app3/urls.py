
from django.urls import path
from .views import ServerStatusView, JoinServerView

urlpatterns = [
    path('status/', ServerStatusView.as_view(), name='status'),
    path('update/', JoinServerView.as_view(), name='update'),
]
