import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Todo

class TodoModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_todo = Todo(pub_date=time)
        self.assertIs(future_todo.was_published_recently(), False)

