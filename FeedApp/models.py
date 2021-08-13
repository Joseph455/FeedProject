from django.db import models
from django.conf import Settings, SettingsReference, settings


# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.CharField(max_length=250)
    date_posted = models.DateTimeField(auto_now_add=True)
    hidden = models.BooleanField(default=False)
    date_hidden = models.DateTimeField(blank=True, null=True)
    hidden_by = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="mod_hidden_by")


    def __str__(self):
        return self.text


class Report(models.Model):
    reported_by =  models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Report_{self.id}_on_{self.post.__str__()}"

