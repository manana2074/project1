
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, RegexValidator


class User(AbstractUser):
    pass


class Speciality(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Doctor(User):

    lisence_number = models.CharField(
        max_length=6,
        unique=True,
        validators=[MinLengthValidator(6)]
    )

    phone_number = models.CharField(
        max_length=15,
        validators=[RegexValidator(regex=r"^\d{8}$")]
    )

    specialities = models.ManyToManyField(
        Speciality,
        related_name='doctors'
    )

    def __str__(self):
        return self.username


class Patient(User):

    national_id = models.CharField(
        max_length=8,
        unique=True
    )

    phone = models.CharField(
        max_length=15,
        validators=[RegexValidator(regex=r"^\d{8}$")]
    )

    birth_date = models.DateField()