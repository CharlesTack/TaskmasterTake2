from django.test import TestCase, Client
from django.urls import reverse
from tasks.models import Task, Category

class TaskViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name="Work", description="Work related tasks")
        self.task = Task.objects.create(
            title="Complete project",
            description="Complete the Django project",
            due_date="2025-01-31",
            completed=False,
            category=self.category
        )

    def test_index_view(self):
        # Test the index view
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/index.html')

    def test_home_view(self):
        # Test the home view
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/index.html')

    def test_task_create_view(self):
        # Test the task create view
        response = self.client.get(reverse('task-create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/task_form.html')

    def test_task_update_view(self):
        # Test the task update view
        response = self.client.get(reverse('task-update', args=[self.task.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/task_form.html')

    def test_task_delete_view(self):
        # Test the task delete view
        response = self.client.get(reverse('task-delete', args=[self.task.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/task_confirm_delete.html')