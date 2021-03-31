from django.contrib import admin

from .models import Course, CourseInfo, ProgrammingLanguages, CourseSignUp

admin.site.register(Course)
admin.site.register(CourseInfo)
admin.site.register(ProgrammingLanguages)
admin.site.register(CourseSignUp)

