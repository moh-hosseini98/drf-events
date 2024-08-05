from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,permissions,generics
from rest_framework.generics import get_object_or_404
from .serializers import EventSerializer
from .models import Event
from .permissions import OrganizerRequiredPermission

class EventListCreateAPIView(generics.ListCreateAPIView):
    queryset = Event.objects.select_related("organizer").prefetch_related("users").all()
    serializer_class = EventSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = (permissions.AllowAny,)

        elif self.request.method == 'POST':
            self.permission_classes =(permissions.IsAuthenticated,)    

        return super().get_permissions()    

    def perform_create(self,serializer):
         serializer.save(organizer=self.request.user)        


class EventDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = (permissions.AllowAny,)

        else:
            self.permission_classes = (OrganizerRequiredPermission,)  

        return super().get_permissions()   


class RegisterEventAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = None

    def post(self,request,id):
        event = get_object_or_404(Event,id=id)

        if event.organizer == self.request.user:
            return Response({"msg":"you cant join your event!"})

        if event.users.filter(id=self.request.user.id).exists():
            return Response({"msg":"already joined event!"}) 

        event.users.add(self.request.user)

        return Response({"message": "User registered on event successfully"}, status=status.HTTP_200_OK)

   







