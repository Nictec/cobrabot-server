from django.db import models

# Create your models here.
class Streamer(models.Model):
    streamer_name = models.TextField(max_length=20, null=True, blank=True)
    bot_name = models.TextField(max_length=20, null=True, blank=True)
    bot_key = models.TextField(max_length=35, null=True, blank=True)
    streamer_key = models.TextField(max_length=35, null=True, blank=True)
    cobra_key = models.TextField(max_length=32)

    def __str__(self):
        return self.streamer_name

class Command(models.Model):
    streamer = models.ForeignKey(Streamer, on_delete=models.CASCADE)
    cmd = models.TextField(max_length=50)
    response = models.TextField(max_length=500)
    cost = models.IntegerField(null=True, blank=True)
    mod_only = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    type = models.IntegerField()

    def __str__(self):
        return self.cmd
