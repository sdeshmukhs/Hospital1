from django.shortcuts import render
from rest_framework import viewsets
from . models import Language
from . serializers import *
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class LanguageView(viewsets.ModelViewSet):    
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    Permission_class = (permissions.IsAuthenticatedOrReadOnly)


class ParadigmView(viewsets.ModelViewSet):
    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializer


class ProgrammerView(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer
    

