from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here
class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'Graham'),
        (2, 'Director'),
        (3, 'Coordinador'),
        (4, 'Profesor'),
        (5, 'Padre de Familia'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, null=True, default=1)


class Graham(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username


class Director(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username


class Coordinador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username


class Profesor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username


class PadreDeFamilia(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username
