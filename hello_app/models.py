from django.db import models

# Register your models here.
class HomepageContent(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to='homepage_images/')
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Homepage Content"