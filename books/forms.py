from django import forms

class ContactForm(forms.Form):
	subject = forms.CharField(max_length=100)
	email = forms.EmailField(required=False, label='E-mail')
	message = forms.CharField(widget=forms.Textarea)
	
	def clean_message(self):
		message = self.cleaned_data['message']
		num_worlds = len(message.split())
		if num_worlds < 4:
			raise forms.ValidationError('Not enough worlds!')
		return message