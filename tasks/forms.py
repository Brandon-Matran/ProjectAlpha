from django.forms import ModelForm
from tasks.models import Task


class TaskForm(ModelForm):

    class Meta:
        db_table = 'project', 'assignee'
        model = Task
        fields = [
            "name",
            "start_date",
            "due_date",
            'project',
            'assignee'
        ]
