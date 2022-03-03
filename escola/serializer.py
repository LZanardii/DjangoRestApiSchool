from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ("id", "nome_completo", "rg","cpf", "data_nascimento")

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ("id", "codigo_curso", "nome", "descricao", "nivel")

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []

class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):
    aluno = serializers.ReadOnlyField(source="aluno.nome_completo")
    curso = serializers.ReadOnlyField(source="curso.nome")
    turno = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ["aluno", "curso", "turno"]
    def get_turno(self, obj):
        return obj.get_turno_display()

class ListaAlunosCursoSerializer(serializers.ModelSerializer):
    curso_nome = serializers.ReadOnlyField(source="curso.nome")   
    aluno_nome_completo = serializers.ReadOnlyField(source="aluno.nome_completo")
    aluno_cpf = serializers.ReadOnlyField(source="aluno.cpf")
    class Meta:
        model = Aluno
        fields = ["curso_nome", "aluno_nome_completo", "aluno_cpf"]