from django import forms
from posts.models import Post, PostAttachment
from posts.utility import POST_FILTER_CHOICES

class PostCreateForm(forms.Form):
    post_text = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Type your post text hear...',
            'id': 'post-text'
        }
    ))

    post_attachments = forms.ImageField(required=False, widget=forms.FileInput(
        attrs={
            'class': 'form-control',
            'id': 'post_atts',
            'multiple': True,
        }
    ))

class PostFilterForm(forms.Form):
    post_filter_choice = forms.ChoiceField(
        choices=POST_FILTER_CHOICES,
        widget=forms.Select(
            attrs={
                'class': 'form-control form-control-sm'
            }
    ))

