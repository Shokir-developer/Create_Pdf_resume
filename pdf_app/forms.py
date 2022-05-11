from django import forms
from .models import PdfModel

class PdfForm(forms.ModelForm):
	class Meta:
		model = PdfModel
		fields = '__all__'

		widgets = {
		'fish' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'F.I.SH'}),
		'sana' : forms.DateInput(attrs={'class':'form-control', 'placeholder':'Tugilgan sana'}),
		'jinsi' : forms.Select(attrs={'class':'form-control'}),
		'email' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'E-mail'}),
		'phone' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'+99890-999-99-99'}),
		'manzil' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Manzil'}),
		'image' : forms.ClearableFileInput(attrs={'class':'form-control'}),
		'millati' : forms.Select(attrs={'class':'form-control', 'placeholder':'Millati'}),
		'fuqorolik' : forms.Select(attrs={'class':'form-control', 'placeholder':'fuqorolik'}),
		'ishlamoqchi_kasb' : forms.TextInput(attrs={'class':'form-control'}),
		'ishlamoqchi_info' : forms.Textarea(attrs={'class':'form-control'}),
		'oylik' : forms.NumberInput(attrs={'class':'form-control'}),
		'oxirgi_ish_joy_vaqti' : forms.TextInput(attrs={'class':'form-control'}),
		'oxirgi_ish_joy_nomi' : forms.TextInput(attrs={'class':'form-control'}),
		'oxirgi_ish_joy_lavozimi' : forms.TextInput(attrs={'class':'form-control'}),
		'malumot' : forms.Select(attrs={'class':'form-control', 'placeholder':'Oliy/Orta...'}),
		'education' : forms.TextInput(attrs={'class':'form-control'}),
		'endDate' : forms.DateInput(attrs={'class':'form-control'}),
		'skills' : forms.TextInput(attrs={'class':'form-control'}),
		'profile' : forms.Textarea(attrs={'class':'form-control'}),
		'prava' : forms.TextInput(attrs={'class':'form-control'}),
		}
