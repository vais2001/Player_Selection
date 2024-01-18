from django.db import models

# Create your models here.

class Skill(models.Model):
    skillname = models.CharField(max_length=50)
    value = models.IntegerField()

    def __str__(self):
        return self.skillname

class Player(models.Model):
    name = models.CharField(max_length=100)
    POSITION_CHOICES=(
            ('defender','Defender'),
            ('midfielder','Midfielder'),
            ('forward','Forward'),
    )
    position = models.CharField(max_length=100, choices=POSITION_CHOICES)
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return self.name
