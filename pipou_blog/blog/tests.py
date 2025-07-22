from django.test import TestCase
from django.urls import reverse

class BlogViewTests(TestCase):
    def test_index_view_status_code(self):
        """Test that the index view returns a 200 OK status code."""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

