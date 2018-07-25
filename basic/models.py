# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class PersonalDetails(models.Model):
    form_id = models.IntegerField()
    full_nam = models.CharField(max_length=50)
    apply_for = models.CharField(max_length=15)
    dob = models.CharField(max_length=25)
    gender = models.CharField(max_length=7)
    aadhar = models.IntegerField()
    bg = models.CharField(max_length=5)
    rel = models.CharField(max_length=20)
    cat = models.CharField(max_length=5)
    nat = models.CharField(max_length=10)
    addr = models.CharField(max_length=150)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    code = models.IntegerField()
    country = models.CharField(max_length=10)
    sc = models.CharField(max_length=5)
    fc = models.CharField(max_length=5)
    sp = models.CharField(max_length=5)
    np = models.CharField(max_length=5)
    
class OtherDetails(models.Model):
    form_id = models.IntegerField()
    full_nam1 = models.CharField(max_length=50)
    age1 = models.IntegerField()
    edu1 = models.CharField(max_length=30)
    occ1 = models.CharField(max_length=30)
    des1 = models.CharField(max_length=30)
    inc1 = models.CharField(max_length=50)
    addr1 = models.CharField(max_length=150)
    offnum1 = models.IntegerField()
    mob1 = models.IntegerField()
    email1 = models.EmailField(max_length=100)
    full_nam2 = models.CharField(max_length=50)
    age2 = models.IntegerField()
    edu2 = models.CharField(max_length=30)
    occ2 = models.CharField(max_length=30)
    des2 = models.CharField(max_length=30)
    inc2 = models.CharField(max_length=10)
    addr2 = models.CharField(max_length=150)
    offnum2 = models.IntegerField()
    mob2 = models.IntegerField()
    email2 = models.EmailField(max_length=100)
    personalDetails = models.ForeignKey(PersonalDetails)
    