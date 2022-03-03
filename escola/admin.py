from django.contrib import admin
from escola.models import Aluno, Curso, Matricula

class Alunos(admin.ModelAdmin):
    list_display = ("id", "nome_completo", "rg", "cpf", "data_nascimento")
    list_display_links = ("id", "nome_completo")
    search_fields =  (["id", "nome_completo", "rg", "cpf",])
    list_per_page = 20

admin.site.register(Aluno, Alunos)

class Cursos(admin.ModelAdmin):
    list_display = ("id","nome", "codigo_curso", "descricao")
    list_display_links = ("id", "nome")
    search_fields =  (["nome", "codigo_curso"])
    list_per_page = 20

admin.site.register(Curso, Cursos)

class Matriculas(admin.ModelAdmin):
    list_display = ("id", "aluno", "curso", "turno")
    list_display_links = ("id", "aluno", "curso")

admin.site.register(Matricula, Matriculas)