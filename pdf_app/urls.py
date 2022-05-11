from django.urls import path
from .views import  formFill, render_pdf_view

urlpatterns = [
	path('', formFill, name='formFill'),
	path('pdf/', render_pdf_view, name='render_pdf_view'),
]