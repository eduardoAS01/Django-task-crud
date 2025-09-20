from django.test import TestCase
from datetime import date,timedelta
from .models import Task
from django.contrib.auth.models import User


# Create your tests here.

class TaskTests(TestCase):

    def setUp(self):
        
        self.user = User.objects.create(username = 'testuser',password='12345678')
        
        self.task1= Task.objects.create(
            title = "Task 1",
            due_date = date.today() + timedelta(days=2),
            is_completed = False,
            user = self.user
        )
        self.task2 = Task.objects.create(
            title = "Task 2",
            due_date = date.today() + timedelta(days=1),
            is_completed = True,
            user = self.user
        )
            
        

    def test_create_task(self):
        self.assertEqual(Task.objects.count(),2)

    def test_filter_completed_task(self):
        completeds = Task.objects.filter(is_completed = True)
        self.assertIn(self.task2,completeds)
        self.assertNotIn(self.task1,completeds)

    def test_order_by_date(self):
        task = Task.objects.order_by('due_date')
        self.assertEqual(task[0],self.task2)