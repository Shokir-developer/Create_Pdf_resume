from django.db import models

class PdfModel(models.Model):
	JINS = (
		('erkak','erkak'),
		('ayol','ayol')
		)

	MILLAT = (
		('uzbek','uzbek'),
		('rus','rus'),
		('qozoq','qozoq'),
		('tojik','tojik'),
		('boshqa','boshqa'),
		)
	FUQOROLIK = (
		('Uzbekistan','Uzbekistan'),
		('Russian','Russian'),
		('Kazak','Kazak'),
		('Tadjik','Tadjik'),
		('Boshqa','Boshqa'),
		)

	MALUMOT = (
		('Oliy','Oliy'),
		("O'rta","O'rta"),
		("Maxsus o'rta", "Maxsus o'rta"),
		('Magistr','Magistr'),
		)

	fish = models.CharField(max_length=100, null=True)
	sana = models.DateField(auto_now=False, null=True)

	jinsi = models.CharField(choices=JINS, max_length=100, null=True)
	email = models.EmailField(max_length=100, null=True)
	phone= models.CharField(max_length=100, null=True)
	manzil = models.CharField(max_length=100, null=True)
	image = models.ImageField(upload_to='user_avatar/', blank=True, null=True)

	millati = models.CharField(choices=MILLAT, max_length=100, null=True)
	fuqorolik = models.CharField(choices=FUQOROLIK, max_length=100, null=True)

	ishlamoqchi_kasb = models.CharField(max_length=100, null=True)
	ishlamoqchi_info = models.TextField(null=True)
	oylik = models.IntegerField("maosh ($)",blank=True, null=True)

	oxirgi_ish_joy_vaqti = models.CharField(max_length=100, null=True)
	oxirgi_ish_joy_nomi = models.CharField(max_length=100, null=True)
	oxirgi_ish_joy_lavozimi = models.CharField(max_length=100, null=True)

	malumot = models.CharField(choices=MALUMOT, max_length=100, null=True)
	education = models.CharField(max_length=200, null=True)
	endDate = models.DateField(auto_now=False, null=True)

	skills = models.CharField("Programming Languages:",max_length=200, null=True)
	profile = models.TextField(null=True)
	

	prava = models.CharField(max_length=50, null=True)


	def __str__(self):
		return self.fish
