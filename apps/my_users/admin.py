from django.contrib import admin

from .models import CustomUser

# @admin.register(CustomUser)

admin.site.register(CustomUser)

