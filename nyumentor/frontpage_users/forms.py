from django import forms
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.models import User
from django.utils.translation  import ugettext_lazy as _
from registration.forms import RegistrationFormUniqueEmail
from frontpage_users.models import UserProfile

class MyAuthenticationForm(AuthenticationForm):
	def __init__(self, *args, **kwargs):
		super(MyAuthenticationForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget = forms.TextInput(attrs={
														'class': 'form-box',
														'size': 10,
														'placeholder': 'Username'})
		self.fields['password'].widget = forms.PasswordInput(attrs={
														'class': 'form-box',
														'size': 10,
														'placeholder': 'Password'})

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User 
		fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile 
		fields = ('picture',)

class RegistrationFormNYUEmail(RegistrationFormUniqueEmail):
	'''
	Subclass of RegistrationFromUniqueEmail that only accepts
	NYU.edu emails
	'''
	good_domains = ['nyu.edu']

	def clean_email(self):
		'''
		Check the supplied email address 
		'''
		email_domain = self.cleaned_data['email'].split('@')[1]
		if email_domain not in self.good_domains:
			raise forms.ValidationError(_("Registration using non nyu.edu addresses is prohibited. Please supply an nyu.edu address."))
		return self.cleaned_data['email']






