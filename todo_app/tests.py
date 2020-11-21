from django.test import TestCase
from .models import Task


class TaskTestCase(TestCase):

    def setUp(self):
        Task.objects.create(title='Task1', deadline='2020-12-1 12:00:00')
        Task.objects.create(title='Task2', deadline='2019-12-1 12:00:00')

    def test_date_correctness(self):
        case1 = Task.objects.get(title="Task1")
        case2 = Task.objects.get(title="Task2")
