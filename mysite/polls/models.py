import datetime

from django.db import models
from django.utils import timezone
from datetime import *


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Autor(models.Model):
    nombre = models.CharField(null=True,  blank=True, max_length=50)
    apellido = models.CharField(max_length=50, null=True, blank=True)
    pais = models.CharField(max_length=50, null=True, blank=True)
    fecha = models.DateField(default=date.today, null=True)

    class Meta:
        verbose_name='Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    # autor = models.ForeignKey(Autor)
    titulo = models.CharField(null=True,blank=True, max_length=100)
    nombre_autor = models.CharField(max_length=50, null=True, blank=True)
    unidad = models.IntegerField(default=0)
    precio = models.FloatField(default=0)
    estado = models.CharField(help_text='Ingresa el estado del libro: "R = renta, V = venta"',max_length=2)
    fecha = models.DateField(default=date.today, null=True)

    class Meta:
        verbose_name='Libro'
        verbose_name_plural = 'Libros'

    def __str__(self):
        return self.titulo
