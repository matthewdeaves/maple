from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class Post(BaseModel):
    title = models.CharField(max_length=75)
    body = models.TextField()
    slug = models.SlugField()
    banner = models.ImageField(default='fallback.png', blank=True)

    def __str__(self):
        return self.title