from django.db import models
from users.models import Trainers
import datetime
from django.utils import timezone

class UserContacts(models.Model):
    name = models.CharField(max_length=100, editable=True)
    email = models.CharField(max_length=100, editable=True)
    message = models.TextField(editable=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'UserContact'
        verbose_name_plural = 'UserContacts'


class Image(models.Model):
    name = models.CharField(max_length=50, default=None)
    img = models.ImageField(upload_to='images/', default=None)



class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    trainer = models.ForeignKey(
         Trainers,
         related_name='Trainers',
         on_delete=models.CASCADE,
         default=None

     )

    def __str__(self):
        return self.name

class Registration(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=13)
    course = models.ForeignKey(
        Course,  # Ensure this reference is correct
        related_name='registrations',
        on_delete=models.CASCADE,
        default=None

    )
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.course.name

