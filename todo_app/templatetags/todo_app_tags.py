from django import template
from ..models import Task

register = template.Library()


@register.simple_tag(name='tasks_amount')
def total_tasks():
    return Task.objects.count()
