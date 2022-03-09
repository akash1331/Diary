from django.contrib import admin
from DiaryApp.models import diaryModel
from DiaryApp.views import *
# Register your models here.

class DiaryAdminSite(admin.ModelAdmin):
    list_display = ['text','datesave']
    list_filter = ['datesave']

admin.site.site_header = 'MyDiary Admin'
admin.site.register(diaryModel,DiaryAdminSite)
