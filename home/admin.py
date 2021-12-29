from django.contrib import admin

from . models import Video


class VideoModel(admin.ModelAdmin):
    list_display=['title','ps','uploader']

admin.site.register(Video,VideoModel)

# Register your models here.
