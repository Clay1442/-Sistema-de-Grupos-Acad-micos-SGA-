from django.db import models
from config import settings 

# Create your models here.
class Club(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True, default='')
    logo = models.ImageField(upload_to='club_logos/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    advisor = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name='advised_clubs'
    )

    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL, 
        through='Membership',
        related_name='joined_clubs', blank=True
        )
    
    def __str__(self):
        return self.name

# Membership class
class Membership(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    position = models.CharField(max_length=100, default='Member')
    input_date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'club')

    def __str__(self):
        return f"{self.user.username} - {self.club.name} as {self.position}"
    

# Event class
class Event(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='events')
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    event_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.club.name}"    
    

# Project class
class Project(models.Model):

    STATUS_CHOICES = (
        ('concluido', 'Concluido'),
        ('em andamento', 'Em andamento'),
        )


    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=200)
    objective = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='Em andamento')
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.club.name}"
