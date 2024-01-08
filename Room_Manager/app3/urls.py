
from django.urls import path
from .views import GetAvailableServerView, JoinServerView, ReplaceServerView

urlpatterns = [
    path('status/', GetAvailableServerView.as_view(), name='get_available_server'),
    path('join_server/', JoinServerView.as_view(), name='join_server'),
    path('replace_server/', ReplaceServerView.as_view(), name='replace_server'),
]
