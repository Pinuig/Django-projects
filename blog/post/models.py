from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to='media/images/')
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now_add=True)
    

