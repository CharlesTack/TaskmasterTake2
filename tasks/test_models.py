from django.test import TestCase
from tasks.models import Task, Category
from django.core.exceptions import ValidationError

class TaskModelTest(TestCase):

    def setUp(self):
        # Set up non-modified objects used by all test methods
        self.category = Category.objects.create(name="Work", description="Work related tasks")
        self.task = Task.objects.create(
            title="Complete project",
            description="Complete the Django project",
            due_date="2025-01-31",
            completed=False,
            category=self.category
        )

    def test_task_creation(self):
        # Test task creation
        self.assertEqual(self.task.title, "Complete project")
        self.assertEqual(self.task.description, "Complete the Django project")
        self.assertEqual(self.task.due_date, "2025-01-31")
        self.assertEqual(self.task.completed, False)
        self.assertEqual(self.task.category, self.category)

    def test_task_str(self):
        # Test the string representation of the task
        self.assertEqual(str(self.task), "Complete project")

    def test_task_due_date(self):
        # Test the due date of the task
        self.assertEqual(self.task.due_date, "2025-01-31")

    def test_task_completed(self):
        # Test the completed status of the task
        self.assertEqual(self.task.completed, False)

    def test_task_category(self):
        # Test the category of the task
        self.assertEqual(self.task.category, self.category)

    def test_task_title_length(self):
        # Test the title length of the task
        self.task.title = "a" * 201
        with self.assertRaises(ValidationError):
            self.task.full_clean()