from django.contrib import admin
from task.models import *
# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display   = ['user','title','discription','due_date','created_at','priority','status']
    list_filter = ['status','priority']
    search_fields = ['user','title','due_date','status','priority']