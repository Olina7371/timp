from django.db import models


# Create your models here.\
class Contacts(models.Model):
    phone_number = models.TextField(max_length=12)
    email = models.EmailField()


class Acconts(models.Model):
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    authecation = models.BooleanField(default=False)


class User(models.Model):
    Name = models.TextField(max_length=100)
    Surname = models.TextField(max_length=100)
    fatherland = models.TextField(max_length=40)
    contact = models.ForeignKey(Contacts, on_delete=models.CASCADE)
    account = models.OneToOneField(Acconts, on_delete=models.CASCADE,null=True)


class TodoList(models.Model):
    name = models.TextField()
    status = models.BooleanField(default=False)


class Notes(models.Model):
    accounts = models.ForeignKey(Acconts, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)
    inform = models.TextField(blank=True)


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
