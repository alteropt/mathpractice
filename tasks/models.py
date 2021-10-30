from django.db import models
from django.contrib.auth.models import User

class Tasks(models.Model):
	id = models.AutoField(primary_key=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	title = models.CharField('Title', max_length=50)
	task = models.TextField('Task')
	date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	updated_date = models.DateTimeField(auto_now=True, null=True, blank=True)
	type = models.ForeignKey('Type', on_delete=models.PROTECT, null=True)
	
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return f'/tasks/{self.type_id}'
	
	class Meta:
		verbose_name = 'Задача'
		verbose_name_plural = 'Задачи'
		ordering = ('-date',)

class Type(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50, db_index=True)
	
	def __str__(self):
		return self.name
	
	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'
		ordering = ('name',)

class Comments(models.Model):
	id = models.AutoField(primary_key=True)
	task = models.ForeignKey(Tasks, on_delete=models.CASCADE, blank=True, null=True, related_name='comments_tasks')
	author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
	created_date = models.DateTimeField(auto_now=True)
	text = models.TextField()

	class Meta:
		verbose_name = 'Комментарий'
		verbose_name_plural = 'Комментарии'
		ordering = ('-created_date',)


