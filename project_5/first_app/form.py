from django import forms
from django.core import validators

class ContactForm(forms.Form):
    name = forms.CharField(label='Username:', help_text='Enter your Name---',required=False,
                           widget=forms.Textarea(attrs={ 'id' : 'text_box','class':'class1','placeholder':'Enter you name--'}))
    file = forms.FileField(label='File')
    email = forms.EmailField(label='Useremail')
    age = forms.CharField(label='Age',widget=forms.NumberInput())
    wieght = forms.FloatField(label='Weight')
    balance = forms.DecimalField(label='Balance')
    cleck = forms.BooleanField(label='Cleck')
    birthday = forms.DateField(label='Birthday',widget=forms.DateInput(attrs={'type':'date'}))
    appointment = forms.DateTimeField(label='Appointment',widget=forms.DateTimeInput(attrs={'type':'datetime-local'}))
    choice = [('S','Small'),('M','Midium'),('L','Large')]
    choices = forms.ChoiceField(label='Choice',choices=choice,widget=forms.RadioSelect)
    meals = [('R','Rice'),('M','Meet'),('A','Aluvotta'),('C','Ciken')]
    meal = forms.MultipleChoiceField(label='Choice your meal',choices=meals,widget=forms.CheckboxSelectMultiple)

# class StudentForm(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()
#     # def clean_name(self):
#     #     valName = self.cleaned_data['name']
#     #     if len(valName) < 10:
#     #         raise forms.ValidationError("Enter your name at list 10 charecter!")
#     #     else:
#     #         return valName
#     # def clean_email(self):
#     #     valemail = self.cleaned_data['email']
#     #     if '.com' and '@' not in valemail:
#     #         raise forms.ValidationError("No include .com amd @ in your email")
#     #     else:
#     #         return valemail
#     def clean(self):
#         cleaned_data = super().clean()
#         valname = self.cleaned_data['name']
#         valemail = self.cleaned_data['email']
#         if len(valname) < 10:
#             raise forms.ValidationError("Enter your name at list 10 charecter!")
#         if '.com' not in valemail:
#             raise forms.ValidationError("No include .com amd @ in your email")

def len_ceck(value):
    if len(value) <10:
        raise forms.ValidationError("Atlist 10 char")
class StudentForm(forms.Form):
    name = forms.CharField(validators=[validators.MinLengthValidator(10,message="Enter your name at list 10 charecter!")])
    text = forms.CharField(validators=[len_ceck])
    email = forms.EmailField(validators=[validators.EmailValidator(message="enter right email")])
    age = forms.IntegerField(validators=[validators.MinValueValidator(24,message="Enter gater then 24"),validators.MaxValueValidator(34,message="Enter less then 34")])
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'],message="Only for pdf")])

class passward_valid(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    passward = forms.CharField(widget=forms.PasswordInput)
    comfirm_passward = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        pas = self.cleaned_data['passward']
        com_pas = self.cleaned_data['comfirm_passward']
        if pas != com_pas:
            raise forms.ValidationError("Doesnot match passward")