# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from app1.models import reg
from django.shortcuts import render

# Create your views here.

def home(request):
	try:
		a = reg.objects.all()
		context = {
			'message': "hello",
			'message1': "hey kaise ho",
			'message2': a

		}
		return render(request, "app1/index.html", context)
	except:
		print("error")



#      		{{ message1  }}
#		{% for i in message2 %}
#			<h1>{{ i.email  }}</h1>
#			<h2>{{ i.id  }}</h2>
