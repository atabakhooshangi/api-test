from django.shortcuts import render
from rest_framework import viewsets
from .models import courses
from .serializers import CourseSerializer


class CourseView(viewsets.ModelViewSet):
	queryset = courses.objects.all()
	serializer_class = CourseSerializer

