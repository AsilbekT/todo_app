from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class ToDo(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    date_created = models.DateTimeField(
        auto_now_add=True, null=True
    )
    deadline = models.DateTimeField(null=True)

    def __str__(self):
        return self.title