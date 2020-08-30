from django.test import TestCase, Client
from .models import Article

import sys
sys.path.append('../')
from users.models import User

class TestIndex(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client = Client()
        self.client.login(username='testuser', password='testpass123')

    def test_index_too_title_has_100char(self):
        """タイトル文字数が上限
        """
        Article.objects.create(title='1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890', user_id=1)
        self.assertEqual(1, len(Article.objects.all()))

    def test_index_too_title_has_100char(self):
        """重複した記事の保存
        """
        try:
            Article.objects.create(title='1234567890', user_id=1)
            Article.objects.create(title='1234567890', user_id=1)
        except Exception:
            print("重複した保存がリクエストされました")