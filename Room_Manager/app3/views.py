from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Server
from .serializers import ServerSerializer

class ServerStatusView(APIView):
    def get(self, request):
        server, created = Server.objects.get_or_create(
            ip='0', 
            defaults={'occupation': 0}
        )
        serializer = ServerSerializer(server)
        return Response(serializer.data)

class JoinServerView(APIView):
    def post(self, request):
        server = Server.objects.first()
        if not server:
            return Response({'message': 'Server not found'}, status=404)

        new_occupancy = request.data.get('occupancy')
        new_ip = request.data.get('ip')
        if new_occupancy is not None:
            try:
                new_occupancy = int(new_occupancy)
                server.occupancy = new_occupancy
                server.ip = new_ip
                server.save()
                message = 'Server occupancy updated'
            except ValueError:
                message = 'Invalid occupancy value'
        else:
            message = 'Occupancy not provided'

        response_data = {
            'message': message,
            'server_ip': server.ip,
            'occupancy': server.occupancy
        }

        return Response(response_data)
