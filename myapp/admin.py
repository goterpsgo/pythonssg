from django.contrib import admin

# Register your models here.
from .models import User, Templates

admin.site.register(User)
admin.site.register(Templates)
