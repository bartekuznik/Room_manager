from django.shortcuts import render
from .models import Status
from .serializers import StatusSerializer
from rest_framework import generics

# Create your views here.

class StatusList(generics.ListAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    
class StatusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
