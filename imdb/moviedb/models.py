from django.db import models

class Movie(models.Model):
    pass

class Actor(models.Model):
    movies=models.ManyToManyField(Movie, through="Role", related_name="actors")
    
class Role(models.Model):
    actor=models.ForeignKey(Actor, on_delete=models.CASCADE, related_name="roles")
    movie=models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="roles")

    class Meta:
        unique_together = (("actor", "movie"))

