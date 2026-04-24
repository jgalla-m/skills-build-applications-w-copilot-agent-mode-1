from djongo import models
import uuid

def uuid4_hex():
    return uuid.uuid4().hex

class User(models.Model):
    id = models.CharField(primary_key=True, max_length=24, default=uuid4_hex, editable=False)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    is_superhero = models.BooleanField(default=False)
    def __str__(self):
        return self.email

class Team(models.Model):
    id = models.CharField(primary_key=True, max_length=24, default=uuid4_hex, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.name

class Activity(models.Model):
    id = models.CharField(primary_key=True, max_length=24, default=uuid4_hex, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    duration = models.IntegerField()  # minutes
    date = models.DateField()
    def __str__(self):
        return f"{self.user.email} - {self.type}"

class Workout(models.Model):
    id = models.CharField(primary_key=True, max_length=24, default=uuid4_hex, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    suggested_for = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Leaderboard(models.Model):
    id = models.CharField(primary_key=True, max_length=24, default=uuid4_hex, editable=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField()
    def __str__(self):
        return f"{self.team.name} - {self.points}"