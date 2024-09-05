from django.contrib.auth import get_user_model
from django.db import models

class Articles(models.Model):
    title = models.CharField('Title', max_length=100)
    intro = models.CharField('Intro', max_length=250)
    text = models.TextField('Article text')
    date = models.DateField('Date', null=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='articles', null=True, default=None)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'





