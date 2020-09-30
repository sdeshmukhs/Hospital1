from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers #its going to take care of generating all the urls for the models


router = routers.DefaultRouter()
router.register('language', views.LanguageView) #this is used for post, get, put, delete requests
router.register('paradigm',views.ParadigmView)
router.register('programmer',views.ProgrammerView)

urlpatterns = [
    path('',include(router.urls)),

]
