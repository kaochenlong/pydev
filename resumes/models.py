from django.db import models


class Resume(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    introduce = models.CharField(max_length=200)
    profile = models.TextField()
    online = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.email})"
