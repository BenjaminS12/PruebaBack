from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Usuario(AbstractUser):
    ROL_CHOICES = [
        ('LIDER', 'Líder'),
        ('GENERAL', 'General'),
    ]
    rol = models.CharField(max_length=10, choices=ROL_CHOICES, default='GENERAL')

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',  
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',  
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

class Asignatura(models.Model):
    nombre = models.CharField(max_length=100)  
    horas = models.PositiveIntegerField(default=0)  

    def __str__(self):
        return self.nombre

class Asistencia(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)  
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)  
    fecha = models.DateTimeField(auto_now_add=True)  
    horas_registradas = models.PositiveIntegerField()  

    def __str__(self):
        return f"Asistencia de {self.usuario.username} en {self.asignatura.nombre} - {self.horas_registradas} horas"
