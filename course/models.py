from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    title = models.CharField(max_length=35, blank=True, null=True, validators=[
        MaxLengthValidator(
            limit_value=35,
            message="Не более 20 символов"
        ),
        MinLengthValidator(
            limit_value=3,
            message="не менее 3 символов"
        )
    ])
    address = models.TextField(max_length=128, blank=True, null=True)

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.title


class ProgrammingLanguages(models.Model):
    title = models.TextField(max_length=64, blank=False, null=True)

    class Meta:
        verbose_name = "Язык программирования"
        verbose_name_plural = "Языки программирования"

    def __str__(self):
        return f'{self.title}'


class CourseInfo(models.Model):
    title = models.CharField(max_length=75, blank=True, null=True, verbose_name="Название курса")
    address = models.TextField(max_length=150, blank=True, null=True, verbose_name="Адрес")
    programming_languages_id = models.ForeignKey(ProgrammingLanguages, blank=True, null=True,
                                                 verbose_name="язык программирования",
                                                 on_delete=models.SET_NULL)
    price_per_month = models.IntegerField(verbose_name="Цена за месяц")
    description = models.TextField(max_length=100, verbose_name="Описание курса")
    image = models.ImageField(verbose_name="фотоязыкапрограммирования",
                              upload_to="media/course_info", blank=True, null=True)
    continuance = models.IntegerField(verbose_name="Количество месяцев")
    course_id = models.ForeignKey(Course, blank=True, null=True, verbose_name="Курс",
                                  on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "Информация о курсе"
        verbose_name_plural = "Информация о курсах"

    def __str__(self):
        return self.title


class CourseSignUp(models.Model):
    user = models.ForeignKey(User, verbose_name="Студент", null=True, on_delete=models.SET_NULL)
    courseinfo_id = models.ForeignKey(CourseInfo, verbose_name="Информация о курсах", null=True,
                                      on_delete=models.SET_NULL, related_name='course_signup')
    price_per_month = models.ForeignKey(CourseInfo, verbose_name="Цена за месяц", null=True,
                                        on_delete=models.SET_NULL)
    date = models.DateField(auto_now=True, auto_now_add=False)
    programming_languages_id = models.ForeignKey(ProgrammingLanguages, verbose_name="языки программирования",
                                                 null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "Запись на курс"
        verbose_name_plural = "Запись на курсы"

    def __str__(self):
        return self.user
