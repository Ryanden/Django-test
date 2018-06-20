from django.db import models

# Create your models here.


class Place(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    name = models.CharField(max_length=50)

    place = models.OneToOneField(
        Place,
        on_delete=models.CASCADE,
        related_name='restaurant_name',
    )

    def __str__(self):
        return self.name


class BlogUser(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class UserInfo(models.Model):

    user = models.OneToOneField(
        BlogUser,
        on_delete=models.CASCADE,
    )

    address = models.CharField(max_length=50)

    phone_number = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.address} {self.phone_number}'


class UserInfo2(models.Model):

    title = models.CharField(max_length=5)