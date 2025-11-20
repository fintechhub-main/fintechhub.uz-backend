from django.db import models


# Create your models here.
class Course(models.Model):
    language_choices = [
        ("Uzbek", "O'zbek tili"),
        ("Russian", "Rus tili"),
        ("English", "Ingliz tili"),
    ]
    title = models.CharField(max_length=100)
    lesson_time = models.DecimalField(max_digits=3, decimal_places=1, default=2)
    lesson_duration = models.PositiveIntegerField(default=10)
    number_of_students = models.PositiveIntegerField(default=12)
    type_of_education = models.CharField(max_length=36 , default="Offline")
    level = models.CharField(max_length=48)
    language = models.CharField(
        max_length=36, choices=language_choices, default="Uzbek"
    )
    banner = models.ImageField(upload_to="course_banners/")
    price = models.PositiveIntegerField(default=0)
    logo = models.ImageField(upload_to="course_logos/")

    def __str__(self):
        return self.title


class CourseDescriptionGroup(models.Model):
    title = models.CharField(max_length=96)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="description_groups"
    )


class CourseDescription(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    group = models.ForeignKey(
        CourseDescriptionGroup, on_delete=models.CASCADE, related_name="descriptions"
    )


class CourseIcon(models.Model):
    icon = models.ImageField(upload_to="course_icons/")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="icons")


class Teacher(models.Model):
    full_name = models.CharField(max_length=96)
    specialty = models.CharField(max_length=96)
    photo = models.ImageField(upload_to="teacher_photos/")


class BannerImage(models.Model):
    image = models.ImageField(upload_to="banner_images/")


class Partner(models.Model):
    logo = models.ImageField(upload_to="partners/")
    title = models.CharField(max_length=96)


class FAQ(models.Model):
    question = models.CharField(max_length=350)
    answer = models.TextField()