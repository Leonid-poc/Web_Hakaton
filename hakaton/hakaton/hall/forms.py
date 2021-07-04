from django import forms

class ContactForm(forms.Form):
  full_name = forms.CharField(max_length=128, required=True, label='', widget=forms.TextInput(attrs={'placeholder': 'Ф.И.О.'}))
  email = forms.EmailField(max_length=128, required=True, label='', widget=forms.TextInput(attrs={'placeholder': 'Почта'}))
  ask = forms.CharField(max_length=1024, label='', widget=forms.Textarea(attrs={'cols': 30, 'rows': 10, 'placeholder': 'Введите ваш вопрос...'}))