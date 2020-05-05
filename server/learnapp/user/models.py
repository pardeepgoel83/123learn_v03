from django.db import models


class Permission(models.Model):
  name = models.CharField(max_length=100)
  status = models.CharField(max_length=20)


class TeamRole(models.Model):
  name = models.CharField(max_length=100)
  permission = models.ManyToManyField(Permission, related_name='team_set')
  status = models.CharField(max_length=20)


class User(models.Model):
  name = models.CharField(max_length=100)
  username = models.CharField(max_length=100)
  password = models.CharField(max_length=200)
  gender = models.CharField(max_length=20)
  dob = models.DateTimeField('date of birth')
  status = models.CharField(max_length=20)
  pub_date = models.DateTimeField('date published')
