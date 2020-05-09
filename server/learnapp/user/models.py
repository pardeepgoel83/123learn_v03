from django.db import models
from simple_history.models import HistoricalRecords

STATUS_CHOICES = [
    ('Active', 'Active'),
    ('In-Active', 'In-Active'),
]
GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
]


class Permission(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=250, default='')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    history = HistoricalRecords()

    def __str__(self):
        return self.name


class TeamRole(models.Model):
    name = models.CharField(max_length=100)
    permission = models.ManyToManyField(Permission, related_name='team_set')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    history = HistoricalRecords()

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    dob = models.DateTimeField('date of birth')
    team = models.ManyToManyField(TeamRole, related_name='user_set')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    add_date = models.DateTimeField('user add date', auto_now=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name
