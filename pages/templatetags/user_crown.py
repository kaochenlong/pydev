from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name="user_crown")
def user_crown(user):
    if user.has_perm("comments.change_comment"):
        return mark_safe('<i class="text-yellow-400 fa-solid fa-crown"></i>')

    return ""
