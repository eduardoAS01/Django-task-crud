from django import forms
from .models import Task
from datetime import date

class TaskForm(forms.ModelForm):
    class Meta():
        model = Task
        exclude = ['created_at','user']
        widgets = {
            'end_at': forms.DateInput(attrs={'type':'date'}),
            'done_it':forms.CheckboxInput(attrs={'type':'checkbox'})
        }

    def clean_end_at(self):
        end_at = self.cleaned_data.get('end_at')

        if end_at and end_at <= date.today():
            raise forms.ValidationError('No puedes crear una tarea en el pasado')
        
        return end_at
 
   