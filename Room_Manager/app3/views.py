from django.shortcuts import render
from .models import Status
from .serializers import StatusSerializer
from rest_framework import generics
from .models import Status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class StatusList(generics.ListAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    
class StatusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class GetAvailableServerView(generics.ListAPIView):
    serializer_class = StatusSerializer

    def check_and_create_servers(self):
        current_server_count = Status.objects.count()
        servers_to_create = 4 - current_server_count
        for i in range(servers_to_create):
            Status.objects.create(ip=f"Server_{current_server_count + i + 1}", occupation=0, status='Available')

    def get_queryset(self):
        # Check and create servers if less than 4
        if Status.objects.count() < 4:
            for i in range(4 - Status.objects.count()):
                Status.objects.create(ip=f"Server_{i+1}", status='offline', occupation=0)
        return Status.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
class ManageServerView(APIView):
    def post(self, request, *args, **kwargs):
        server_ip = request.data.get('server_ip')

        try:
            server = Status.objects.get(ip=server_ip)
            occupation = int(server.occupation) if server.occupation.isdigit() else 0

            if server.status == 'offline':
                server.status = 'online'
                occupation = 1
            else:
                if occupation < 4:
                    occupation += 1
                else:
                    return Response({'message': 'Server is full', 'ip': server.ip, 'status': server.status, 'occupation': occupation}, status=status.HTTP_400_BAD_REQUEST)
            
            server.occupation = occupation
            server.save()
            return Response({'message': 'Server status updated', 'ip': server.ip, 'status': server.status, 'occupation': occupation}, status=status.HTTP_200_OK)

        except (Status.DoesNotExist, ValueError):
            return Response({'error': 'Server not found or invalid data'}, status=status.HTTP_404_NOT_FOUND)

class ReplaceServerView(APIView):
    def post(self, request, *args, **kwargs):
        server_ip = request.data.get('server_ip')
        Status.objects.get(ip=server_ip).delete()
        new_server = Status.objects.create(ip=f"{server_ip}", status='offline', occupation=0)
        return Response(StatusSerializer(new_server).data, status=status.HTTP_201_CREATED)