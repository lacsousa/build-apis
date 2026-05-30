from django.db import models


class Empresa(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField(null=False)
    telefone = models.TextField(null=True)
