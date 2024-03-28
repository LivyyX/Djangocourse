from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text= models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    publish_date= models.DateTimeField(blank=True,null=True)
    image=models.ImageField(null=True,blank=True,upload_to='images/')
    
    def publish(self):
        self.publish_date = timezone.now()
        self.save()
        
    def __str__(self):
        return self.title