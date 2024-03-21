from django.db import models
from django.contrib.auth.hashers import make_password,check_password
# Create your models here.
class PassManager(models.Model):

    social_network = models.CharField('Red Social', max_length=50, blank= False, null=False)
    username = models.CharField('Nombre de usuario', max_length=150)
    password = models.CharField('Contraseña', max_length=250)



    def set_password(self,raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
    