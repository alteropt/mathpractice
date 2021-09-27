from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login


def register(request):
	form = None
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			ins = form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)		
			form.save_m2m()
			messages.success(request, 'Вы успешно зарегестрировались!')
			return redirect('/')

	else:
		form = UserRegisterForm()

	data = {
		'form': form,
	}
	return render(request, 'account/register.html', data)

