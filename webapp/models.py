from __future__ import unicode_literals

from django.db import models

class videos(models.Model):
    video_id = models.CharField(max_length = 140)
    video_name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.video_id

class sync_time(models.Model):
    time_in_seconds = models.IntegerField()
    issue_time = models.DateField()

    def __str__(self):
        return self.time_in_seconds

class commands(models.Model):
    command = models.CharField(max_length = 20)
    issue_time = models.DateField()

    def __str__(self):
        return self.command
