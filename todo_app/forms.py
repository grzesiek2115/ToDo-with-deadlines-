from .models import Task
from django import forms
#from django.utils import timezone
import datetime


class TaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(label='Date',
                                   widget=forms.DateTimeInput)

    class Meta:
        model = Task
        fields = ['title', 'deadline', ]

    def clean_deadline(self):
        cd = self.cleaned_data

        user_date_input = datetime.datetime.strptime(
            self.data['deadline'], '%Y-%m-%d %H:%M:%S'
        )
        if user_date_input < datetime.datetime.now():
            raise forms.ValidationError("Date is coming from past!")
        return cd['deadline']

        """
        def is_valid(self):
            valid = super(TaskForm, self).is_valid()

            user_date_input = datetime.datetime.strptime(
            self.data['deadline'], '%Y-%m-%d %H:%M:%S'
            )

            if user_date_input > datetime.datetime.now():
                return True
            else:
                return False"""
