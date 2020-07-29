from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, related_name='user_profile', on_delete=models.CASCADE)
    address = models.CharField(
        max_length=300, help_text='Required. Inform your address')

    def __str__(self):
        return f'{self.user} Profile'
