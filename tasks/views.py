from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Tasks, Type
from .forms import TasksForm, CommentForm
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy


def tasks_home(request):
	type = Type.objects.all()
	data = {
		'title': 'Задачи',
		'type': type,
	}
	return render(request, 'tasks/tasks_home.html', data)

def task_type(request, type_id):
	tasks = Tasks.objects.filter(type_id=type_id)
	data = {
		'title': 'Задачи',
		'tasks': tasks,
		'type_id': type_id
	}
	return render(request, 'tasks/tasks_type.html', data)

class TasksDetailView(FormMixin, DetailView):
	model = Tasks
	template_name = 'tasks/details_view.html'
	context_object_name = 'task'
	form_class = CommentForm
	success_url = '/'

	def post(self, request, *args, **kwargs):
		form = self.get_form()
		if form.is_valid():
			return self.form_valid(form)
		else:
			return self.form_invalid(form)
	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.task = self.get_object()
		self.object.author = self.request.user
		self.object.save()
		return super().form_valid(form)


class TasksUpdateView(LoginRequiredMixin, UpdateView):
	login_url = reverse_lazy('login')
	model = Tasks
	template_name = 'tasks/update_task.html'	
	form_class = TasksForm

	def get_form_kwargs(self):
		kwargs = super().get_form_kwargs()
		if self.request.user != kwargs['instance'].author:
			return self.handle_no_permission()
		return kwargs

class TasksDeleteView(LoginRequiredMixin, DeleteView):
	login_url = reverse_lazy('login')
	model = Tasks
	template_name = 'tasks/delete_task.html'
	success_url = '/tasks'

	def delete(self, request, *args, **kwargs):
		self.object = self.get_object()

		if self.request.user != self.object.author:
			return self.handle_no_permission()
		success_url = self.get_success_url()
		self.object.delete()
		return HttpResponseRedirect(success_url)

'''
@login_required(login_url = '/account/login/')
def create_task(request):
	error = ''
	if request.method == 'POST':
		form = TasksForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/tasks')
		else:
			error = 'Форма заполнена неверно!'
	form = TasksForm()

	data = {
		'title': 'Добавление задачи',
		'form': form,
	}
	return render(request, 'tasks/create_task.html', data)
'''

class TaskCreateView(LoginRequiredMixin, CreateView):
	login_url = reverse_lazy('login')
	model = Tasks
	template_name = 'tasks/create_task.html'
	form_class = TasksForm
	success_url = reverse_lazy('tasks_home')
	context_object_name = 'form'

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.author = self.request.user
		self.object.save()
		return super().form_valid(form)


