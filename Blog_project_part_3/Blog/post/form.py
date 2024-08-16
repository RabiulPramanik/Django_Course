from django import forms
from .models import PostModel, CommentModel

class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        # fields = '__all__'
        exclude = ['author']
class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['name', 'body', 'email']