from django import forms
from helloworld.models import Funcionario, Equipe, Tarefa

class InsereFuncionarioForm(forms.ModelForm):
    class Meta:
        model=Funcionario
        fields='__all__'
    chefe = forms.BooleanField(
        label='Este Funcionário exerce função de Chefia?',
        required=False,
        widget=forms.CheckboxInput
    )
    biografia = forms.CharField(
        label='Biografia:',
        required=False,
        widget=forms.Textarea
    )

class InsereEquipeForm(forms.ModelForm):
    class Meta:
        model=Equipe
        fields='__all__'
        widgets = { 
            'integrantes': forms.SelectMultiple(attrs={'class':'form-select'})
        }
    descricao = forms.CharField(
        label='Descrição da equipe',
        required=False,
        widget=forms.Textarea
    )

class InsereTarefaForm(forms.ModelForm):
    class Meta:
        model=Tarefa
        fields='__all__'
        widgets = {
            'equipes': forms.SelectMultiple(attrs={'class':'form-select'})
        }
    descricao = forms.CharField(
        label='Descrição da tarefa',
        required=False,
        widget=forms.Textarea
    )