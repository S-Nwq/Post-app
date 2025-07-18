from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default='got.png', blank=True)
    # author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # tags = models.ManyToManyField('Tag', related_name='posts')
    def __str__(self):
        return self.title
    
    