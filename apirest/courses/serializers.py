from rest_framework import serializers
from .models import courses

class CourseSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = courses
		fields = ('id' ,'url' , 'name' , 'language' , 'price')
