from django.urls import path, include
from .import views
from rest_framework import routers
app_name = "course"


router = routers.DefaultRouter()
router.register("course", views.CourseViewSet)
router.register("courseinfo", views.CourseInfoViewSet)
router.register("programminglanguages", views.ProgrammingLanguagesViewSet)
router.register('CourseSignUp', views.CourseSignUpViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
