from django.contrib import admin

# Register your models here.
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    fields = ["description", "pub_date"]

admin.site.register(Todo, TodoAdmin)
