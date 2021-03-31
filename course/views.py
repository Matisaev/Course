from rest_framework.viewsets import ModelViewSet


from .models import Course, CourseInfo, ProgrammingLanguages, CourseSignUp
from .serializers import CourseSerializer, CourseInfoSerializer, \
    ProgrammingLanguagesSerializer, CourseSignUpSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseInfoViewSet(ModelViewSet):
    queryset = CourseInfo.objects.all()
    serializer_class = CourseInfoSerializer


class ProgrammingLanguagesViewSet(ModelViewSet):
    queryset = ProgrammingLanguages.objects.all()
    serializer_class = ProgrammingLanguagesSerializer


class CourseSignUpViewSet(ModelViewSet):
    queryset = CourseSignUp.objects.all()
    serializer_class = CourseSignUpSerializer
