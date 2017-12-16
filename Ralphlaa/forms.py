from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate



class UserRegister(forms.ModelForm):
	username = forms.CharField(label='Username ou', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entre Username ou pou mwen Bazzz'}))
	first_name = forms.CharField(label='Non ou', widget=forms.TextInput(attrs={'class': 'form-control col-md-6', 'placeholder': 'Entre non ou pou mwen Bazzz'}))
	last_name = forms.CharField(label='Prenon ou', widget=forms.TextInput(attrs={'class': 'form-control col-md-6', 'placeholder': 'Entre prenon ou pou mwen Bazzz'}))
	email = forms.EmailField(label='email ou', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entre email ou pou mwen Bazzz'}))
	class Meta:
		model = User
		fields = [
			'first_name',
			'last_name',
			'username',
			'email'
		]

		def clean_username(self):
			username = self.cleaned_data.get('username')
			username_qs = User.objects.filter(username=username)


			if username_qs.exists():
				raise ValidationError('Moun sa nan base de donnees a deja ti bray!! Reessayer')

		def clean_email(self, *args, **kwargs):
			email = self.cleaned_data.get('email')
			email_qs = User.objects.filter(email=email)

			if email_qs.exists():
				raise ValidationError('Email sa la deja Bazz!! LOLLL')

		def clean(self):
			return super(UserRegister, self).clean(*args, **kwargs)



class ContactForm(forms.ModelForm):
	email = forms.EmailField(label="Email Adress", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))
	email2 = forms.EmailField(label="Confirm Email Adress", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email 2'}))
	password = forms.CharField(label="Your Password", widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}))
	password2 = forms.CharField(label="Confirm Your Password", widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password 2'}))
	class Meta:
		model = User
		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
			'email2',
			'password',
			'password2'
		]

	def clean_email2(self):
		email = self.cleaned_data.get('email')
		email2 = self.cleaned_data.get('email2')

		if email != email2:
			raise forms.ValidationError('Email 1 an pa menm ak Email 2 aa!! Check It again')
		
		email_qs = User.objects.filter(email=email)
		if email_qs.exists():
			raise forms.ValidationError('Email sa ap use deja kolonn')

	def clean_password(self):
		password = self.cleaned_data.get('password')
		password2 = self.cleaned_data.get('password2')

		if password and password2:
			if password != password2:
				raise forms.ValidationError('Modpas sa yoo pa menm nn afe pam')