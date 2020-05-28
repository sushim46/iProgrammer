from django.db import models

# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    slug = models.CharField(max_length=130)
    thumbnail = models.ImageField(upload_to='blog/images',default='')
    timestamp = models.DateTimeField(blank=True)
    published = models.BooleanField(default=True)
    longer_feature = models.BooleanField(default=False)

    def __str__(self):
        return self.title + ' by ' + self.author 
