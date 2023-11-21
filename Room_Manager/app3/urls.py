
from django.urls import path
from .views import StatusDetail, StatusList

urlpatterns = [
    path('status/', StatusList.as_view()),
    path('status/<int:pk>/', StatusDetail.as_view()),
]
