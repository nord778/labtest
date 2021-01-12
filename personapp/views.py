from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status 
from personapp.serializers import personserializer,personListserializer
from personapp.models import person


class personcreateview(generics.CreateAPIView):
	serializer_class = personserializer
	queryset = person.objects.all()
	status=status.HTTP_201_CREATED

	
class PersonListView(generics.ListAPIView):
	serializer_class = personListserializer
	queryset = person.objects.all()

class personDetailView(generics.RetrieveAPIView):
	serializer_class  = personserializer
	queryset = person.objects.all()

class personUpdateView(generics.UpdateAPIView):
	serializer_class  = personserializer
	queryset = person.objects.all()

class personDeleteView(generics.DestroyAPIView):
	serializer_class  = personserializer
	queryset = person.objects.all()
	
			



# class personDetailView(generics.RetrieveUpdateDestroyAPIView):
# 	serializer_class  = personserializer
# 	queryset = person.objects.all()

# def post(self, request):
# 		serializer = self.serializer_class(data=request.data)
# 		if serializer.is_valid():
# 			message = f'hellllo'
# 			return Response({'message': message})