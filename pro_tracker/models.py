from django.db import models

# Create your models here.

class Player(models.Model): 
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    account_id = models.IntegerField()
    is_pro = models.BooleanField()

    class Meta: 
        ordering = ['name'] 

class Match(models.Model): 
    created = models.DateTimeField(auto_now_add=True)
    started_at = models.DateTimeField()
    average_mmr = models.IntegerField()
    players = models.ManyToManyField(Player)

    class Meta: 
        ordering = ['started_at'] 

