from django.contrib.auth.models import Group


def join_group(user, group_name):
    group = Group.objects.get(name=group_name)
    if not group.user_set.filter(id=user.id).exists():
        group.user_set.add(user)


def leave_group(user, group_name):
    group = Group.objects.get(name=group_name)
    if group.user_set.filter(id=user.id).exists():
        group.user_set.remove(user)
