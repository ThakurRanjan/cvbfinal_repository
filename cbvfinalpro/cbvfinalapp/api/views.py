from rest_framework import viewsets
from cbvfinalapp.models import Beer
from cbvfinalapp.api.serializers import BeerSerializer

class BeerSerializerView(viewsets.ModelViewSet):
    queryset = Beer.objects.all()
    serializer_class = BeerSerializer
