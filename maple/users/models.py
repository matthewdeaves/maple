from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class User(BaseModel):
    username = models.CharField(max_length=75)
    email = models.TextField()
    icon = models.ImageField(default='fallback.png', blank=True)

    def __str__(self):
        return self.title