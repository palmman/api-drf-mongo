from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


from .models import Account, UserProfile


def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = UserProfile.objects.create(
            user=user,
            email=user.email,
        )
        
        
post_save.connect(createProfile, sender=Account)