from django import forms
from .models import City


class CityForm(forms.Form):
    name = forms.CharField(max_length=100, label='Назва',
                           widget=forms.TextInput(attrs={'class': "form-control",
                                                         'placeholder': 'Введіть назву міста', }))


class CityForm2(forms.ModelForm):
    name = forms.CharField(label='Назва',
                           widget=forms.TextInput(attrs={'class': "form-control",
                                                         'placeholder': 'Введіть назву міста', }))

    class Meta:
        model = City
        fields = '__all__'
