from django import forms
from .models import TaskModel

class TaskmodelFrom(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['title','decription','is_complete','assing_date']
        widgets = {
            'assing_date': forms.DateTimeInput(attrs={'type':'datetime-local'}),
        }