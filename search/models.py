from django.db import models

class Mentors(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    expertise = models.CharField(max_length=100)  # Assuming expertise is a subject in computer science
    experience = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name