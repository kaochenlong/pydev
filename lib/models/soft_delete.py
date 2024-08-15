from django.db import models
from django.utils import timezone


class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at=None)


class SoftDeleteable:
    def delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def really_delete(self):
        self.delete()

    objects = SoftDeleteManager()
