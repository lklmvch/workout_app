from django import forms
from django.forms import TextInput, Textarea, ModelForm, DateInput

from .models import Articles


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'intro', 'text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': "col-lg-6",
                'placeholder': "Title"
            }),
            'intro': TextInput(attrs={
                'class': "col-lg-6",
                'placeholder': "Intro"
            }),
            'text': Textarea(attrs={
                'class': 'col-lg-12',
                'placeholder': "Text"
            }),
            'date': DateInput(attrs={
                'class': 'col-lg-12',
                'placeholder': "Date"
            }),
            # 'author': TextInput(attrs={
            #     'class': "col-lg-6",
            #     'placeholder': "Author"
            # })

        }
