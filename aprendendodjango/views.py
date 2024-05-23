from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic import TemplateView, CreateView, UpdateView, DetailView, DeleteView
from helloworld.models import Funcionario, Equipe, Tarefa
from website.forms import InsereFuncionarioForm, InsereEquipeForm, InsereTarefaForm

# Create your views here.

def cria_funcionario(request, pk):
    #verificamos se o método POST
    if request.method == 'POST':
        form = InsereFuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('lista_funcionarios'))
        
    else:
        return render(request,"templates/form.html", {'form':form})
    
def cria_equipe(request, pk):
    #verificamos se o método POST
    if request.method == 'POST':
        form = InsereEquipeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('lista_equipes'))
        
    else:
        return render(request,"templates/form.html", {'form':form})

#view index
class IndexTemplateView(TemplateView):
    template_name = 'website/index.html'

#view para equipes
class EquipesListView(ListView):
    template_name = 'equipes.html'
    model = Equipe
    context_object_name='equipes'
    def get_queryset(self):
        queryset=super().get_queryset()
        nome=self.request.GET.get('nome')
        if nome:
            queryset = queryset.filter(nome__icontains=nome)
        return queryset

class EquipeCreate(CreateView):
    template_name = 'website/cadastra-equipe.html'
    model = Equipe
    #fields = '__all__'
    form_class = InsereEquipeForm
    success_url='/equipes/'

class EquipeUpdate(UpdateView):
    template_name = 'website/updateequipe.html'
    model = Equipe
    fields = '__all__'
    success_url='/equipes/'

class EquipeDetail(DetailView):
    template_name = 'website/verequipe.html'
    model = Equipe

class EquipeDelete(DeleteView):
    template_name = 'website/excluiequipe.html'
    model = Equipe
    success_url='/equipes/'

#views para Funcionario

class ListaFuncionariosListView(ListView):
    template_name = 'funcionarios.html'
    model = Funcionario
    context_object_name = "funcionarios"
    def get_queryset(self):
        queryset=super().get_queryset()
        nome=self.request.GET.get('nome')
        if nome: 
            queryset = queryset.filter(nome__icontains=nome)
        sobrenome=self.request.GET.get('sobrenome')
        if sobrenome: 
            queryset = queryset.filter(sobrenome__icontains=sobrenome)
        return queryset

class FuncionarioCreate(CreateView):
    template_name = 'website/cadastra-funcionario.html'
    model = Funcionario
   #fields = '__all__'
    form_class = InsereFuncionarioForm
    success_url='/funcionarios/'

class FuncionarioUpdate(UpdateView):
    template_name = 'website/updatefunc.html'
    model = Funcionario
    fields = '__all__'
    success_url='/funcionarios/'

class FuncionarioDetail(DetailView):
    template_name = 'website/verfunc.html'
    model = Funcionario

    def get_context_data(self, **kwargs: Any):
        context=super().get_context_data(**kwargs)
        funcionario=self.get_object()
        context['teste']=funcionario
        return context

class FuncionarioDelete(DeleteView):
    template_name = 'website/excluifunc.html'
    model = Funcionario
    success_url = '/funcionarios/'

#views para tarefa

class ListaTarefaListView(ListView):
    template_name='tarefas.html'
    model = Tarefa
    context_object_name = "tarefas"
    def get_queryset(self):
        queryset=super().get_queryset()
        nome=self.request.GET.get('nome')
        if nome: 
            queryset = queryset.filter(nome__icontains=nome)
        return queryset

class TarefaCreate(CreateView):
    template_name = 'website/cadastra-tarefa.html'
    model = Tarefa
   #fields = '__all__'
    form_class = InsereTarefaForm
    success_url='/tarefas/'

class TarefaUpdate(UpdateView):
    template_name = 'website/updatetarefa.html'
    model = Tarefa
    fields = '__all__'
    success_url='/tarefas/'

class TarefaDetail(DetailView):
    template_name = 'website/vertarefa.html'
    model = Tarefa

class TarefaDelete(DeleteView):
    template_name = 'website/excluitarefa.html'
    model = Tarefa
    success_url='/tarefas/'

class CalcView(TemplateView):
    template_name = 'website/calculadora.html'
    def post(self,request,*args,**kwargs):
        input1 = request.POST.get('input1')
        input2 = request.POST.get('input2')
        operacao = request.POST.get('operacao')
        if operacao == 'soma':
            resultado = float(input1) + float(input2)
            op=operacao
            operacao = '+'
        if operacao == 'subtracao':
            resultado = float(input1) - float(input2)
            op=operacao
            operacao = '-'
        if operacao == 'multiplicacao':
            resultado = float(input1) * float(input2)
            op=operacao
            operacao = 'x'
        if operacao == 'divisao':
            resultado = float(input1) / float(input2)
            op=operacao
            operacao = '÷'
        if operacao == 'exponenciacao':
            resultado = float(input1)**float(input2)
            op=operacao
            operacao = '^'
        if operacao == 'raiz':
            resultado = float(input1)**(1/float(input2))
            op=operacao
            operacao = '√'
        return render(request,'website/resultado.html',{'input1':input1,'input2':input2,'operacao':operacao,'resultado':resultado,'op':op})