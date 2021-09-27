from django.contrib import admin
from .models import Tasks, Type, Comments

class TasksAdmin(admin.ModelAdmin):
	list_display = ('title', 'task', 'date', 'updated_date')
	list_display_links = ('title', 'task')
	search_fields = ('title', 'task')

class TypeAdmin(admin.ModelAdmin):
	list_display = ('name',)
	list_display_links = ('name',)
	search_fields = ('name',)

class CommentsAdmin(admin.ModelAdmin):
	list_display = ('author', 'created_date', 'text')
	list_display_links = ('author', 'text')
	search_fields = ('author', 'text')

admin.site.register(Tasks, TasksAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Comments, CommentsAdmin)
