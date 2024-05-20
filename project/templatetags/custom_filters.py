from django import template
from django.utils.timesince import timesince
from django.utils import timezone

register = template.Library()

@register.filter
def custom_pub_date(pub_date):
    now = timezone.now()
    time_difference = now - pub_date
    if time_difference.days == 0:
        if time_difference.seconds < 60:
            # Less than a minute
            return 'just now'
        elif time_difference.seconds < 3600:
            # Less than an hour
            minutes = time_difference.seconds // 60
            return f'{minutes} {"minute" if minutes == 1 else "m"}'
        else:
            # Less than 24 hours
            hours = time_difference.seconds // 3600
            return f'{hours} {"hour" if hours == 1 else "hr"}'
    else:
        # More than 24 hours
        return pub_date.strftime('%d/%m/%Y')

