from django.contrib import admin
from django.urls import path, include
from escola.views import AlunosViewSet, CursoViewSet, ListaAlunosCursoView, ListaMatriculasAlunoView, MatriculaViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register("alunos", AlunosViewSet, basename="Alunos")
router.register("cursos", CursoViewSet, basename="Cursos")
router.register("matriculas", MatriculaViewSet, basename="matriculas")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("alunos/<int:pk>/matriculas/", ListaMatriculasAlunoView.as_view()),
    path("curso/<int:pk>/alunos/", ListaAlunosCursoView.as_view())
]
