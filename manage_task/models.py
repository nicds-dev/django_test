from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

def is_digit(value):
    if not value.isdigit():
        raise ValidationError('Must be number')
    
def limit_date(value):
    if value <= timezone.now().date():
        raise ValidationError('Must be a future date')

class Person(models.Model):

    class IdChoices(models.TextChoices):
        CEDULA_CIUDADANIA = 'CC', 'Cedula de Ciudadania'
        CEDULA_EXTRANJERA = 'CE', 'Cedula Extranjera'
        TARJETA_IDENTIDAD = 'TI', 'Tarjeta de Identidad'

    name = models.CharField('User name', max_length=100)
    last_name = models.CharField('User last name', max_length=100)
    document_type = models.CharField('Document type', max_length=2, choices=IdChoices.choices)
    document_number = models.CharField('Document number', max_length=10, validators=[is_digit], unique=True)
    email = models.EmailField('Email address', max_length=150, unique=True)

    class Meta:
        verbose_name = ('Person')
        verbose_name_plural = ('Persons')

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField('Task tittle', max_length=150)
    description = models.TextField('Task description')
    deadline_date = models.DateField('Task deadline date', validators=[limit_date], auto_now=False, auto_now_add=False)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ('Task')
        verbose_name_plural = ('Tasks')

    def __str__(self):
        return self.title