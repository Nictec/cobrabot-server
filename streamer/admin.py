from django.contrib import admin
from .models import Streamer, Command

# Register your models here.
admin.site.register(Streamer)
admin.site.register(Command)