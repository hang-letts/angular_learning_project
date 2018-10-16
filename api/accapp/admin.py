from django.contrib import admin
from .models import LoginModel, ProfileModel

# Register your models here.
admin.site.register(LoginModel)
admin.site.register(ProfileModel)
