from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from mainapp.models import Student
from mainapp.serializers import StudentModelSerializer


class StudentViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, GenericViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
