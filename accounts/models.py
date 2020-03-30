import random

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

# Create your models here.
DEFAULT_PICS = [
    'https://cdn3.iconfinder.com/data/icons/avatars-9/145/Avatar_Alien-512.png',
    'https://66.media.tumblr.com/15aa93b2b3b4949d6d061735c9ba6b21/tumblr_inline_n6y3qnRoSg1r73jj6.png',
    'https://cdn.dribbble.com/users/6142/screenshots/5679189/profiledefault_2x.png',
    'https://cdn.imgbin.com/0/10/15/imgbin-robot-scalable-graphics-euclidean-icon-robot-qDGV4CMnQsejEwaqGRvRiU1PH.jpg',
    'https://cdn.dribbble.com/users/2101624/screenshots/6068793/dribbble5.jpg',
    'https://i0.wp.com/aqyi.org/wp-content/uploads/2017/12/blank-profile.png?fit=449%2C449&ssl=1&w=640',
    'https://miro.medium.com/max/800/0*QCRunR_VjAIrvkjC.png',
    'https://icon-library.net/images/cool-profile-icon/cool-profile-icon-9.jpg',
]

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(default=0)
    image_url = models.TextField(default=random.choice(DEFAULT_PICS))
    join_date = models.DateTimeField(auto_now_add=True)
    bio = models.TextField(default="This user has no written a bio.")

    def get_absolute_url(self):
        return reverse('user_detail', args=[str(self.id)])