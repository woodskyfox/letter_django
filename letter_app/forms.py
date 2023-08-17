from django import forms

from . models import Message

# class MessageForm(forms.ModelForm):
# 	class Meta:
# 		model = Message
# 		fields = ['text']
# 		labels = {'text': ''}

class MessageForm(forms.ModelForm):
	class Meta:
		model = Message
		fields = ['text']
		labels = {'text': 'Message'}
		widgets = {'text': forms.Textarea(attrs={'cols': 80})}
