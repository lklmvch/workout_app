from django.contrib import admin
from .models import UserContacts, Image, Course, Registration

admin.site.register(UserContacts)
admin.site.register(Image)
admin.site.register(Registration)
admin.site.register(Course)