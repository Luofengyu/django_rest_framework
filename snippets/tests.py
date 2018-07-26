from django.test import TestCase

# Create your tests here.

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


class ModelSnippetOperateTest(TestCase):
    def setUp(self):
        self.origin_data = dict(title="Test snippet model", code="This is a single data for test operate")
        self.test_data_id = None
        self.query = Snippet.objects.filter(id=self.test_data_id)

    def test_create(self):
        test_data = Snippet(title="Test snippet model", code="This is a single data for test operate")
        test_data.save()
        self.test_data_id = test_data.id
        self.assertEqual(test_data.title, self.origin_data['title'], "Snippet 对象创建失败")

    def test_update(self):
        pass

