from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Book
from profiles.models import Profile


COURSE_CHOICES=[
	('All Available','All Available'),
	('Bsc Computer Science','Bsc Computer Science'),
	('Bsc in Commerce','Bsc in Commerce'),
	('Bsc Quantity Survey','Bsc Quantity Survey')
]
class SignUpForm(UserCreationForm):
	email = forms.EmailField(
		label='',
		max_length=254,
		widget=forms.EmailInput(
			attrs={
				"placeholder": "Email",
				"class": "form-control"
			}
		)
	)

	username = forms.CharField(
		label='',
		max_length=30,
		min_length=5,
		required=True,
		widget=forms.TextInput(
			attrs={
				"placeholder": "Username",
				"class": "form-control"
			}
		)
	)

	password1 = forms.CharField(
		label='',
		max_length=30,
		min_length=8,
		required=True,
		widget=forms.PasswordInput(
			attrs={
				"placeholder": "Password",
				"class": "form-control"
			}
		)
	)

	password2 = forms.CharField(
		label='',
		max_length=30,
		min_length=8,
		required=True,
		widget=forms.PasswordInput(
			attrs={
				"placeholder": "Confirm Password",
				"class": "form-control"
			}
		)
	)
	
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')

	def save(self,commit=True):
		user =super().save(commit=False)

		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class CourseProfileForm(forms.ModelForm):
	course = forms.CharField(
		label = '',
		required = True,
		widget=forms.Select(
			choices = COURSE_CHOICES,
			attrs={
				"class": "form-control"
			}
			)
		)
	class Meta:
		model = Profile
		fields = ('course',)


class BookForm(forms.ModelForm):
	class Meta:
		model = Book
		fields = ('title', 'author', 'pdf', 'cover')

class SearchBookForm(forms.Form):
    search_name = forms.CharField(required=False,
			widget=forms.TextInput(
			attrs={
				"placeholder": "  Search Topic",
			}
		)
			)