from django.contrib.auth.models import User
from django.db import models

from lib.models.soft_delete import SoftDeleteable, SoftDeleteManager


class Resume(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    introduce = models.CharField(max_length=200)
    profile = models.TextField()
    online = models.BooleanField(default=False)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    bookmark = models.ManyToManyField(User, related_name="bookmarks")

    def __str__(self):
        return f"{self.name} ({self.email})"

    def bookmarked_by(self, user) -> bool:
        return self.bookmark.filter(id=user.id).exists()


class Comment(SoftDeleteable, models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(default=None, null=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    objects = SoftDeleteManager()

    class Meta:
        indexes = [
            models.Index(fields=["deleted_at"]),
        ]
