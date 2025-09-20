from django import forms
from .models import Task
from datetime import date

class TaskForm(forms.ModelForm):
    class Meta():
        model = Task
        exclude = ['created_at','user','is_completed']
        widgets = {
            'due_date': forms.DateInput(attrs={'type':'date'}), 
        }

    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')

        if due_date and due_date <= date.today():
            raise forms.ValidationError('You cant set a due date in the past')
        
        return due_date
 
   