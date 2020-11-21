from django.db import models
from django import forms
from autoslug import AutoSlugField


class Task(models.Model):
    title = models.CharField(max_length=200)

    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(
        help_text='Use the following format: %Y-%m-%d %H:%M:%S')

    #slug = models.SlugField(max_length=200)
    slug = AutoSlugField(populate_from='title')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created']
        #ordering = ['-created']
