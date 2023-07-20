from django.db import models
from django.urls import reverse

# Create your models here.

class MGroup(models.Model):
    mgroup_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)

    class Meta:
        verbose_name = 'main group'
        verbose_name_plural = 'main groups'

    def __str__(self):
        return self.mgroup_name
    
class MSGroup(models.Model):
    msgroup_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    mgroup_name = models.ForeignKey(MGroup, on_delete=models.CASCADE)
    description = models.TextField(max_length=255, blank=True)

    class Meta:
        verbose_name = 'sub group'
        verbose_name_plural = 'sub groups'

    def __str__(self):
        return self.msgroup_name