from django import forms

from .models import Sign_for_class


class SignForm(forms.ModelForm):
    name = forms.CharField(required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
    phone = forms.IntegerField(
        widget=forms.TextInput(attrs={'placeholder': '+7 123 45 77'})
                               )
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    description = forms.CharField(required=False, widget=forms.Textarea(
        attrs={'placeholder': 'Комментарий (необязательно)'}))

    class Meta:
        model = Sign_for_class
        fields = ['name', 'phone', 'email', 'description']
