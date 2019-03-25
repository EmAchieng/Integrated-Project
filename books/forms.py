from django import forms


class ContactForm(forms.Form):
	fullname = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control",
															 "placeholder": "Your full name"}))
	email    = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control",
															  "placeholder": "Your email address"}))
	content  = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control",
															"placeholder": "Your message"}))
	def clean_email(self);
		email = self.cleaned_data.get("email")