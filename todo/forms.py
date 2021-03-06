from django import forms
from django.forms import ModelForm
from .models import Todo


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'memo', 'important']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title'
            }),
            'memo': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Memo...'
            }),
        }
