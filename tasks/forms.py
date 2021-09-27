from .models import Tasks, Type, Comments
from django.forms import ModelForm, TextInput, Textarea, ModelChoiceField


class TasksForm(ModelForm):
	class Meta:
		model = Tasks
		fields = ['title', 'task', 'type']

		type = ModelChoiceField(queryset=Type.objects.all(), to_field_name='type')

		widgets = {
			'title': TextInput(attrs={
					'class': 'form-input',
					'tabindex': 1,
					'placeholder': 'Название',
			}),

			'task': Textarea(attrs={
					'class': 'form-input',
					'tabindex': 2,
					'placeholder': 'Текст задачи',
			}),
		}

class CommentForm(ModelForm):
	class Meta:
		model = Comments
		fields = ('text', )

		widgets = {
			'text': Textarea(attrs={
					'class': 'form-input comment',
					'placeholder': 'Текст комментария'
				})
		}


