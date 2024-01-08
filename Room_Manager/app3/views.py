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
        # czy mamy 4 serwera
        self.check_and_create_servers()
        return Status.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
class JoinServerView(APIView):
    def post(self, request, *args, **kwargs):
        server_id = request.data.get('server_id')

        try:
            server = Status.objects.get(id=server_id)
            occupation = int(server.occupation)
            if occupation < 4:
                server.occupation = occupation + 1
                server.save()
                return Response(StatusSerializer(server).data, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Server is full'}, status=status.HTTP_400_BAD_REQUEST)
        except (Status.DoesNotExist, ValueError):
            return Response({'error': 'Server not found or invalid data'}, status=status.HTTP_404_NOT_FOUND)
        
class ReplaceServerView(APIView):
    def post(self, request, *args, **kwargs):
        server_id = request.data.get('server_id')
        Status.objects.filter(id=server_id).delete()
        new_server = Status.objects.create(ip="Server_" + str(server_id), occupation=0, status='Available')
        return Response(StatusSerializer(new_server).data, status=status.HTTP_201_CREATED)