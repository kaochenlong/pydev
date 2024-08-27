from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Initialize Database"

    def handle(self, *args, **options):
        # 建立 VIP Group
        group, _ = Group.objects.get_or_create(name="VIP")

        # 建立 VIP 權限
        perm_list = [
            "delete_resume",
            "change_comment",
        ]
        permissions = Permission.objects.filter(codename__in=perm_list)
        group.permissions.set(permissions)

        print("init databased done!!")
