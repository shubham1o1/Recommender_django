from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'

class KeyVal(models.Model):
    name      = models.CharField(max_length=50,default="", editable=False)
    key       = models.CharField(max_length=240, db_index=True)
    value     = models.IntegerField(db_index=True)

    def __str__(self):
        return '%s'%(self.name+' '+self.key+' '+str(self.value))


# class KeyVal(models.Model):
#     container = models.ForeignKey(User, db_index=True, on_delete=models.CASCADE)
#     key       = models.CharField(max_length=240, db_index=True)
#     value     = models.IntegerField(db_index=True)

#     def __str__(self):
#         return '%s'%(self.container.username)