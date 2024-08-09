from django.db import models

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
