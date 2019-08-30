from django.db import models



# Create your models here.
class AdminPersons(models.Model):
    name = models.CharField(max_length = 30)
    sur_name = models.CharField(max_length = 30)
    address = models.CharField(max_length = 60)
    email = models.EmailField()
    mobile_no = models.CharField(max_length = 20)
    adhar_no = models.CharField(max_length = 12)


class TicketManagers(models.Model):
    name = models.CharField(max_length = 30)
    sur_name = models.CharField(max_length = 30)
    address = models.CharField(max_length = 60)
    email = models.EmailField()
    mobile_no = models.CharField(max_length = 20)
    adhar_no = models.CharField(max_length = 12)

class UserRegistration(models.Model):
    name = models.CharField(max_length = 30)
    username = models.CharField(max_length = 30)
    password = models.CharField(max_length = 20)
    address = models.CharField(max_length = 60)
    email = models.EmailField()
    mobile_no = models.CharField(max_length = 20)
    country = models.CharField(max_length = 12)
    country_id = models.CharField(max_length = 20)
    ctnid_no = models.IntegerField()


class AdminPersons1(models.Model):
    name = models.CharField(max_length = 30)
    sur_name = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30)
    address = models.CharField(max_length = 60)
    email = models.EmailField()
    mobile_no = models.CharField(max_length = 20)
    adhar_no = models.CharField(max_length = 12)
