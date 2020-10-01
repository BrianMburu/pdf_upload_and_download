from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
	COURSE_CHOICES=[
	('All Available','All Available'),
	('Bsc Computer Science','Bsc Computer Science'),
	('Bsc in Commerce','Bsc in Commerce'),
	('Bsc Quantity Survey','Bsc Quantity Survey')
	]
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.CharField(max_length=50, blank=True)
	course = models.CharField(max_length=100, choices = COURSE_CHOICES,default='Available Courses')
	location = models.CharField(max_length=30)
	email_confirmed = models.BooleanField(default=False)
	
	def __str__(self):
		return self.user.username

'''
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
'''

