from django.test import SimpleTestCase


class HomeViewTestCase(SimpleTestCase):

    def test_request_home_page(self):
        response = self.client.get('/')
        self.assertContains(response, 'Hi welcome to mainpage!', status_code=200)
