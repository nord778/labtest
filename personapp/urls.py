from django.contrib import admin
from django.urls import path,include
from personapp.views import *

urlpatterns = [
    path('POST/person/', personcreateview.as_view()),
    path('GET/persons/',PersonListView.as_view()),
    path('GET/person/<int:pk>/',personDetailView.as_view()),
    path('PATCH/person/<int:pk>/',personUpdateView.as_view()),
    path('DELETE/person/<int:pk>/',personDeleteView.as_view()),	
]

