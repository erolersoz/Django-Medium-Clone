from django import forms
from django.core import validators
from .models import BlogPost
from tinymce.widgets import TinyMCE

from config.validators import min_length_3





class BlogPostModelForm(forms.ModelForm):
    tag = forms.CharField()
    content = forms.CharField(widget=TinyMCE(attrs={'cols':40,'rows':20}))
    title = forms.CharField(validators=[min_length_3])

    class Meta:
        model = BlogPost
        fields = [
            'title',
            'cover_image',
            'content',
            'category',
            'tag',

        ]
    
    # def clean_title(self):
    #     title = self.cleaned_data.get('title')
    #     if len(title) < 3:
    #         raise forms.ValidationError('OOooo en az 3 karakter olmali')
    #     return title.upper()