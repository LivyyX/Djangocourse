from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    
    title = forms.CharField(help_text='POMOCY!')
    
    class Meta:
        model=Post
        fields =['title','text','image']
        
