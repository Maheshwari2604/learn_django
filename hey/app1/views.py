# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def home(request):
	try:
		return render(request, "app1/index.html")
	except:
		print("error")
