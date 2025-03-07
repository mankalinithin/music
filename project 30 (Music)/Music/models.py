from django.db import models
from django.contrib.auth.models import User
class Music(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.TextField()
    artist=models.TextField()
    genre=models.TextField()
    image=models.ImageField(upload_to='images/')
    file=models.FileField(upload_to='songs/',max_length=100)
    def __str__(self):
        return self.title
class MyPlaylist(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    fav=models.ForeignKey(Music, on_delete=models.CASCADE)
    
    
