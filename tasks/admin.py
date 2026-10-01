from django.contrib import admin
from .models import WeeklyTask, DailyTodo
# Register your models here
admin.site.register(WeeklyTask)
admin.site.register(DailyTodo)

