from django.db.models.signals import post_save
from django.dispatch import receiver
from custom_user.models import User
from django.core.mail import send_mail




@receiver(post_save, sender=User)
def new_user_alert(sender, instance, created, **kwargs):
    if created:
        send_mail('New user on Testappkpsea', 'A new user has just signed up on kpsea', 'Testprep@testprepken.com',
        ['bestessays001@gmail.com'], fail_silently=True)


@receiver(post_save, sender=User)
def print_only_after_deal_created(sender, instance, created, **kwargs):
    if created:
        print(f'New deal with pk: {instance.pk} was created.')