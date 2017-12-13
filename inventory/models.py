# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class Item(models.Model):
    owner = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    description = models.TextField()
    container = models.CharField(max_length=100, default="None")
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
