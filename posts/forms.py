from django import forms
from posts.models import Post, PostAttachment
from posts.utility import POST_FILTER_CHOICES, POST_TEXT_PLACEHOLDER, MAX_FILES_COUNT, MAX_FILES_COUNT_ERROR

class PostCreateForm(forms.Form):
    post_text = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': POST_TEXT_PLACEHOLDER,
            'id': 'post-text'
        }
    ))

    post_attachments = forms.ImageField(required=False, widget=forms.ClearableFileInput(
        attrs={
            'class': 'form-control',
            'id': 'post_atts',
            'multiple': True,
        }
    ))

    def clean(self):
        cleaned_data = self.cleaned_data
        
        #cc_myself = cleaned_data.get("post_text")
        post_attachments = self.files.getlist("post_attachments")

        if len(post_attachments) > MAX_FILES_COUNT:
            msg = MAX_FILES_COUNT_ERROR.format(MAX_FILES_COUNT)
            self._errors["post_attachments"] = self.error_class([msg])
        
        return cleaned_data

class PostFilterForm(forms.Form):
    post_filter_choice = forms.ChoiceField(
        choices=POST_FILTER_CHOICES,
        widget=forms.Select(
            attrs={
                'class': 'form-control form-control-sm'
            }
    ))

