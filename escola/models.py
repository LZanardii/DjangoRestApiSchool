from datetime import datetime
from tkinter import CASCADE
from django.db import models
from django.forms import DateField

class Aluno(models.Model):

    nome_completo = models.CharField(max_length=45)
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=9)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome_completo

class Curso(models.Model):
    NIVEL = (
        ("B", "Básico"),
        ("I", "Intermediário"),
        ("A", "Avançado"),
    )
    
    codigo_curso = models.CharField(max_length=10)
    nome = models.CharField(max_length=45)
    descricao = models.CharField(max_length=150) 
    nivel = models.CharField(max_length=1, choices=NIVEL, blank=False, null=False, default="B")

    def __str__(self):
        return self.nome

class Matricula(models.Model):

    TURNO = (
        ("M", "Manhã"),
        ("T", "Tarde"),
        ("N", "Noite"),
    )

    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    turno = models.CharField(max_length=1, choices=TURNO, blank=False, null=False, default="M")
