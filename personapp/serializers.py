from rest_framework import serializers
from personapp.models import person

class personListserializer(serializers.ModelSerializer):
	class Meta : 
		model = person
		fields = ('id','name','adress','work','age')


class personserializer(serializers.ModelSerializer):
	class Meta : 
		model = person
		fields = '__all__'