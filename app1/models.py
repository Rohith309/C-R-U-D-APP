from django.db import models
class Student(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    course=models.CharField(max_length=20)
    fee=models.DecimalField(max_digits=8,decimal_places=2)
