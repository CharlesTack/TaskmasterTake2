from django.test import TestCase
from tasks.forms import TaskForm
from tasks.models import Task, Category

class TaskFormTest(TestCase):

    def setUp(self):
        # Set up non-modified objects used by all test methods
        self.category = Category.objects.create(name="Work", description="Work related tasks")
        self.valid_data = {
            'title': 'Complete project',
            'due_date': '2025-01-31',
            'category': self.category.id,
        }
        self.invalid_data = {
            'title': '',
            'due_date': '',
            'category': '',
        }

    def test_task_form_valid(self):
        # Test form with valid data
        form = TaskForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_task_form_invalid(self):
        # Test form with invalid data
        form = TaskForm(data=self.invalid_data)
        self.assertFalse(form.is_valid())

    def test_task_form_title_max_length(self):
        # Test form title max length
        self.invalid_data['title'] = 'a' * 201
        form = TaskForm(data=self.invalid_data)
        self.assertFalse(form.is_valid())

    def test_task_form_category_field(self):
        # Test form category field
        self.invalid_data['category'] = 'invalid_category'
        form = TaskForm(data=self.invalid_data)
        self.assertFalse(form.is_valid())
