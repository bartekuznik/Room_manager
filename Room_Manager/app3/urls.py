
from django.urls import path
from .views import GetAvailableServerView, ManageServerView, ReplaceServerView

urlpatterns = [
path('status/', GetAvailableServerView.as_view(), name='get_available_server'),
    path('manage_server/', ManageServerView.as_view(), name='manage_server'),
    path('replace_server/', ReplaceServerView.as_view(), name='replace_server'),
]
