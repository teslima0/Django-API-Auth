from django.db import models
import uuid
from UserAuth.models import Profile
# Create your models here.

class Task(models.Model):
    title= models.CharField(max_length=200)
    completed=models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.title
    
class Project(models.Model):
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    title=models.CharField( max_length=255)
    description=models.TextField(null= True, blank=True)
    owner= models.ForeignKey(Profile,null=True, blank=True, on_delete=models.SET_NULL)
    created= models.DateTimeField(auto_now_add=True)