from django.db import models


# Create your models here.
#Artist, Music, Comment
class Artist(models.Model):
    name = models.TextField()
    
    def __str__(self):
        return self.name
        
class Music(models.Model):
    title = models.TextField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
        
class Comment(models.Model):
    content = models.TextField()
    music = models.ForeignKey(Music, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.content