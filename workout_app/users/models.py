from django.db import models

# Create your models here.
class Trainers(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.CharField(max_length=250)
    phone_number = models.CharField(default='000-000-0000', max_length=50, null=False, blank=False, unique=False)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Trainer'
        verbose_name_plural = 'Trainers'
