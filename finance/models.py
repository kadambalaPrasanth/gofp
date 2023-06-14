from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class portfolio(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    schema_name=models.CharField(max_length=100)
    qnt=models.IntegerField()
    price=models.FloatField()
    category=models.CharField(max_length=100)
    investment=models.IntegerField()
    def __str__(self):
        return f"{self.user.first_name} {self.schema_name}"