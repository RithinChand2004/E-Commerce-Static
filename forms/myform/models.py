from django.db import models

class Form1Submission(models.Model):
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    hobbies = models.TextField()

    def __str__(self):
        return self.name

class Form2Submission(models.Model):
    name = models.CharField(max_length=100)
    subject_marks = models.IntegerField()

    def __str__(self):
        return self.name