from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile

class MyProfile(UserenaBaseProfile):
    user = models.OneToOneField(User, unique=True,
                                verbose_name = _('user'), related_name='my_profile')
    USER_TYPES = (
            (u'Individual', u'individual'),
            (u'School', u'school'),
            (u'Organization', u'organization'),
        )
    user_type = models.CharField(max_length=100,
                                choices = USER_TYPES                        
        )
# Create your models here.
