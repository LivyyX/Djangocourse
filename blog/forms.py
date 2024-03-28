from django import forms
from .models import Post

class ImgForm(forms.ModelForm):
    class Meta:
        model=Post
        fields =['image']