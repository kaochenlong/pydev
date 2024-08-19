from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Initialize Database"

    def handle(self, *args, **options):
        # 建立 VIP 權限
        perm_delete_resume = Permission.objects.get(codename="delete_resume")
        perm_change_comment = Permission.objects.get(codename="change_comment")

        # 建立 VIP Group
        group, created = Group.objects.get_or_create(name="VIP")

        if created:
            group.permissions.add(
                perm_change_comment,
                perm_delete_resume,
            )

        print("init databased done!!")
