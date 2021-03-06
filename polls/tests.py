from django.test import TestCase
from django.utils import timezone
import datetime
from .models import Question

class QuestionModelTests(TestCase):
    def test(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.recent(), False)
