from rest_framework.serializers import ModelSerializer

from mainapp.models import Student


class StudentModelSerializer(ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'
