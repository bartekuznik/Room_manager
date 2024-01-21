from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Server
from .serializers import ServerSerializer
import random


class ServerStatusView(APIView):
    def get(self, request):
        ports = [9000]

        for port in ports:
            Server.objects.get_or_create(ip=str(port), defaults={'occupation': random.uniform(0, 3)})

        all_servers = Server.objects.all()
        serializer = ServerSerializer(all_servers, many=True)
        return Response(serializer.data)
    
class UpdateServerView(APIView):
    def post(self, request):
        ip = request.data.get('ip')
        new_occupation = request.data.get('new_occupation')
        if ip is None or new_occupation is None:
            return Response({'message': 'IP and new occupation must be provided'}, status=400)

        try:
            new_occupation = int(new_occupation)
        except ValueError:
            return Response({'message': 'Invalid new occupation value'}, status=400)

        server, created = Server.objects.get_or_create(ip=ip)
        server.occupation = new_occupation
        server.save()

        serializer = ServerSerializer(server)
        return Response(serializer.data)