from django.db import models

class Alert(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.TextField()
    place = models.URLField()
    priority = models.TextField()

class Media(models.Model):
    alert = models.ForeignKey(Alert, on_delete=models.CASCADE, related_name="media")
    image = models.ImageField(upload_to="alert_images")
    video = models.FileField(upload_to="alert_vidoes")

class Updates(models.Model):
    alert = models.ForeignKey(Alert, on_delete=models.CASCADE, related_name="updates")
    update = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)