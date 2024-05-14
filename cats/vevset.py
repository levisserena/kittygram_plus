from rest_framework import viewsets
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from .models import Cat
from .serializers import CatSerializer


class CatViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Cat.objects.all()
        serializer = CatSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Cat.objects.all()
        cat = get_object_or_404(queryset, pk=pk)
        serializer = CatSerializer(cat)
        return Response(serializer.data)
