from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.text import slugify

from .models import CustomUser, Tag, Post


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email',)


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['title', 'slug']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def save(self):
        tag, created = Tag.objects.update_or_create(
            title=self.cleaned_data['title'],
            slug=slugify(self.cleaned_data['title'], allow_unicode=True)
        )
        return tag


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'tags']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

    def save(self):
        tags =
        post, created = Post.objects.create(title=self.cleaned_data['title'],
                                            body=self.cleaned_data['body'],
                                            slug=slugify(self.cleaned_data['title'],
                                                         allow_unicode=True),
                                            tags=self.cleaned_data['tags'])
        return post
