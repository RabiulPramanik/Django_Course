from django import forms
from first_app.models import StudentModels

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModels
        fields = '__all__'
        # exclude = ['roll']  #bad jabe roll
        # fields = ['name', 'roll']

        labels = {
            'name':'User Name',
            'roll':'User Id',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'btn-primary'}),
            # 'roll': forms.PasswordInput()
        }
        help_texts = {
            'name' : 'Enter your name'
        }
        error_messages = {
            'name' : {'required': 'Your name is required!'}
        }
