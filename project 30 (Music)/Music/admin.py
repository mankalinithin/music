from django.contrib import admin
from .models import Music,MyPlaylist
@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ['id','title']
@admin.register(MyPlaylist)
class MyPlaylistAdmin(admin.ModelAdmin):
    list_display =['id','user'] 


