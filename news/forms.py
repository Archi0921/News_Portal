from importlib.resources import contents

from django import forms
from django.core.exceptions import ValidationError
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        content = cleaned_data.get('content')
        if content is not None and len(content) < 20:
            raise ValidationError({'content': 'Content не может быть менее 20 символов'})

        heading = cleaned_data.get('heading')
        if heading == content:
            raise ValidationError('Content не должен соответствовать heading')
        return cleaned_data





