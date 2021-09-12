from django.db import models
from django.conf import settings
from django.utils import timezone
from django import forms

    

class Rule(models.Model):
    """
    Правила. Создается администратором
    Набор политик, регулирующий права доступа к хостам
    или группе хостов (в том числе и принтерам)
    """
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    data = models.JSONField()

class Group(models.Model):
    """
    Группы. Создается администратором
    """
    name = models.CharField(max_length=50)
    permissions = models.ForeignKey(Rule, on_delete=models.CASCADE)

class Client(models.Model):
    """
    Клиент. Создается администратором
    """
    login = models.CharField(max_length=20)
    tempPass = models.CharField(max_length=20)
    # permissionStamp = models.JSONField()
    # permissionStamp = models.ForeignKey(Rule, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    createdDate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.login

    def setNewPass(self, newPass):
        self.tempPass = newPass

class Host(models.Model):
    """
    Любой хост в сети (Клиентский пк, сервер, принтер)
    """
    CHOICES = (
        ('Srv', 'Server'),
        ('Cln', 'Client'),
        ('Prt', 'Printer'),
    )

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    ip = models.CharField(max_length=100)
    description = models.CharField(max_length=250, default="Host")
    # permissionStamp = models.ForeignKey(Rule, on_delete=models.CASCADE)
    typeHost = models.CharField(max_length=3, choices=CHOICES)
    createdDate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def getIp(self):
        return self.ip

    def getPermissions(self):
        return self.permissions

    def setPermissions(self, newPermissions):
        self.permissions = newPermissions

# class Store(Host):
#     # Хранилище
#     # TODO
