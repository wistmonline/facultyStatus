from django.forms import ModelForm
from .models import Account

from django import  forms

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Enter password',
        'class':'form-control'
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Confirm password',
        'class':'form-control'
    }))
    
    class Meta:
        model = Account
        fields = ['email','name','dept', 'gender','phone']


    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email'
        self.fields['name'].widget.attrs['placeholder'] = 'Full Name'
        self.fields['dept'].widget.attrs['placeholder'] = 'select'
        self.fields['phone'].widget.attrs['placeholder'] = 'Mobile Number'
        self.fields['password'].widget.attrs['placeholder'] = 'Enter Password'
        self.fields['confirm_password'].widget.attrs['placeholder'] = 'Confirm Password'

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            # self.fields[field].widget.attrs['placeholder'] = field

    # Confirm password in the form itself
    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        conf_password = cleaned_data.get('confirm_password')

        if password != conf_password:
            raise forms.ValidationError(
                'Password Does Not Match'
            )
