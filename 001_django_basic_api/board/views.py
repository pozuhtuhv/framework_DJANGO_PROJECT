from rest_framework import generics

from .models import BoardModel
from .serializers import BoardModelSerializer


class BoardListCreate(generics.ListCreateAPIView):
    queryset = BoardModel.objects.all()
    serializer_class = BoardModelSerializer

class BoardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BoardModel.objects.all()
    serializer_class = BoardModelSerializer