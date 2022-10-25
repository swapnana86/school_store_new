from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Department(models.Model):
    dept_name = models.CharField(max_length=250)

    def __str__(self):
        return self.dept_name


class Course(models.Model):
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=250)

    def __str__(self):
        return self.course_name


class Userdata(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    name = models.CharField(max_length=50)
    # gender = models.CharField(max_length=50)

    # gender_choices = models.IntegerChoices('Gender', 'Male Female')
    # gender = models.CharField(max_length=6, choices=gender_choices.choices)

    gender = models.CharField(max_length=6, default=False, choices=[('M', 'Male'), ('F', 'Female')])

    # favorite_fruit = models.CharField(label='Select Gender',widget=models.RadioSelect(choices=FRUIT_CHOICES))

    email = models.EmailField(blank=False)
    dob = models.DateTimeField(null=True, blank=True)
    age = models.IntegerField()
    phone = models.IntegerField()
    address = models.TextField(max_length=250)
    dept = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
