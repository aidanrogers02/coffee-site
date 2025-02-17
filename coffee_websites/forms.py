from django import forms

from .models import Review

class ReviewForm(forms.ModelForm):
	class Meta:
		model = Review
		fields = ['title', 'rating', 'text']
		labels = {'title': 'Title', 'rating':'Rating', 'text': 'Text'}
		widgets = {'text': forms.Textarea(attrs={'cols':80})}
		
