from django.urls.conf import include
from django.contrib import admin
from django.urls import path
from . import views
from website.views import EquipesListView, EquipeCreate, EquipeDetail, EquipeDelete, EquipeUpdate, \
    ListaFuncionariosListView, IndexTemplateView, FuncionarioCreate, FuncionarioUpdate, FuncionarioDetail, \
    FuncionarioDelete, ListaTarefaListView, TarefaCreate, TarefaUpdate, TarefaDetail, TarefaDelete, CalcView

app_name = 'website'

# urlpatterns contém a lista de roteamentos de URLs
urlpatterns = [
    #GET
    path('',IndexTemplateView.as_view(), name='index'), #homepage=index
    path('equipes/', EquipesListView.as_view(), name='lista_equipes'),
    path('equipe/create/', EquipeCreate.as_view(), name='create_equipe'),
    path('equipe/update/<int:pk>', EquipeUpdate.as_view(), name='update_equipe'),
    path('equipe/detail/<int:pk>', EquipeDetail.as_view(), name='detail_equipe'),
    path('equipe/delete/<int:pk>', EquipeDelete.as_view(), name='delete_equipe'),
    path('funcionarios/', ListaFuncionariosListView.as_view(), name='lista_funcionarios'),
    path('funcionario/create/', FuncionarioCreate.as_view(), name='create_funcionario'),
    path('funcionario/update/<int:pk>', FuncionarioUpdate.as_view(), name='update_funcionario'),
    path('funcionario/detail/<int:pk>', FuncionarioDetail.as_view(), name='detail_funcionario'),
    path('funcionario/delete/<int:pk>', FuncionarioDelete.as_view(), name='delete_funcionario'),
    path('tarefas/', ListaTarefaListView.as_view(), name='lista_tarefas'),
    path('tarefa/create/', TarefaCreate.as_view(), name='create_tarefa'),
    path('tarefa/update/<int:pk>', TarefaUpdate.as_view(), name='update_tarefa'),
    path('tarefa/detail/<int:pk>', TarefaDetail.as_view(), name='detail_tarefa'),
    path('tarefa/delete/<int:pk>', TarefaDelete.as_view(), name='delete_tarefa'),
    path('calculadora/',CalcView.as_view(),name='calculadora')
]