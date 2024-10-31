from django.db import models
from django.db.models import User

# Create your models here.

class Testimonials(models.Model):
    content=models.TextField()
    image=models.ImageField(upload_to="root",default="default.jpg")
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.first_name


class FQA(models.Model):
    title=models.TextField()
    answer=models.TextField()


class Pros(models.Model):
    title=models.CharField(max_length=220)
    status=models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title
    

class Prices(models.Model):
    title=models.CharField(max_length=220)
    price=models.IntegerField(default=0)
    pros=models.ManyToManyField(Pros, on_delete=models.CASCADE)
    status=models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title


class Services(models.Model):
    title=models.CharField(max_length=200)
    desc=models.TextField()
    status=models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title


class Services_two(models.Model):
    title=models.CharField(max_length=200)
    desc=models.TextField()
    status=models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title

