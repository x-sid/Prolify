from rest_framework import generics
from .serializers import ContactSerializer
from.permissions import IsOwnerOrReadOnly
from album.models import Contact


class ContactList(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)



class ContactRudView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ContactSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return Contact.objects.all()