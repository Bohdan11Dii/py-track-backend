from django.contrib import admin
from django.contrib.auth.models import User

from courses.models import Topic, Module

# Register your models here.


admin.site.register(Module)
admin.site.register(Topic)
