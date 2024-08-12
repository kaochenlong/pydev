from django.db import models
from django.utils import timezone


class Resume(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    introduce = models.CharField(max_length=200)
    profile = models.TextField()
    online = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.email})"


class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at=None)


class Comment(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(default=None, null=True)

    objects = SoftDeleteManager()

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()

    # def really_delete(self):
    #     self.delete()

    class Meta:
        indexes = [
            models.Index(fields=["deleted_at"]),
        ]
