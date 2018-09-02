from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Stomach(models.Model):
    time = models.DateTimeField()
    consistency = models.CharField(
        max_length=255,
        choices=(
            ('OK', 'OK'),
            ('QMUSHY', 'Quite mushy'),
            ('RMUSHY', 'Really mushy'),
            ('DIARRHEA', 'Full-on diarrhea')
        )
    )
    bloodiness = models.CharField(
        max_length=255,
        choices=(
            ('NONE', 'None'),
            ('BLOT', 'Lots of bright blood'),
            ('BSOME', 'Some bright blood'),
            ('DLOT', 'Lots of dark blood'),
            ('DSOME', 'Some dark blood'),
            ('MLOT', 'Lots of blood, hard to say if it is dark or bright'),
            ('MSOME', 'Some blood, hard to say if it is dark or bright')
        )
    )
    comment = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.time

class Edible(models.Model):
    name = models.CharField(max_length=255, unique=True)
    ingredients = models.ManyToManyField('self', blank=True, related_name="ingredients")
    def __str__(self):
        return self.name

class Feeding(models.Model):
    timestamp = models.DateTimeField()
    food = models.ManyToManyField(Edible, related_name='food')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        foods = []
        for food in self.food.all():
            foods.append(str(food))
        foodstring = ', '.join(foods)

        return str(self.timestamp) + " (" + foodstring + ") "
