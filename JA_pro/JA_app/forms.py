from django import forms
from .models import *
from django.contrib.auth import get_user_model


class OfferForm(forms.ModelForm):

    class Meta:
        model=Offer
        fields='__all__'
        widgets={

            'title':forms.TextInput(attrs={'class':'form-control mb-2'}),
            'description':forms.Textarea(attrs={'class':'form-control mb-2'}),
        }
class CategoryForm(forms.ModelForm):
     class Meta:

        model=Category
        fields='__all__'
        widgets={

            'name':forms.TextInput(attrs={'class':'form-control mb-2'}),
            'description':forms.Textarea(attrs={'class':'form-control mb-2'}), 
        }   
User=get_user_model()
class RegisterForm(forms.ModelForm):
    confirmpass = forms.CharField(

        widget=forms.PasswordInput(attrs={

            'class': 'form-control',
            'placeholder': 'Confirm Password'

        })

    )

    class Meta:
        model= User
        fields=['username','first_name', 'last_name', 'email','password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})


        }


    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password') 
        confirmpass = cleaned_data.get('confirmpass')

        if password and confirmpass and password != confirmpass:
            raise form.ValidationError("كلمتا المرور غير متطابقتين")

        return cleaned_data   

          




        
