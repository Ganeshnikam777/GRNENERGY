import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from app import app


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        app.testing = True

    def test_index(self):
        r = self.client.get('/')
        self.assertEqual(r.status_code, 200)
        self.assertIn(b'GRN Energy', r.data)

    def test_index_shows_services(self):
        r = self.client.get('/')
        self.assertIn(b'Energy Auditing', r.data)

    def test_index_shows_blog_preview(self):
        r = self.client.get('/')
        self.assertIn(b'IPMVP', r.data)

    def test_services_page(self):
        r = self.client.get('/services')
        self.assertEqual(r.status_code, 200)
        self.assertIn(b'Energy Auditing', r.data)
        self.assertIn(b'ISO 50001', r.data)
        self.assertIn(b'Carbon Footprint', r.data)

    def test_about_page(self):
        r = self.client.get('/about')
        self.assertEqual(r.status_code, 200)
        self.assertIn(b'GRN Energy', r.data)
        self.assertIn(b'Pune', r.data)

    def test_blog_listing(self):
        r = self.client.get('/blog')
        self.assertEqual(r.status_code, 200)
        self.assertIn(b'IPMVP', r.data)

    def test_blog_post_valid(self):
        r = self.client.get('/blog/1')
        self.assertEqual(r.status_code, 200)
        self.assertIn(b'IPMVP', r.data)

    def test_blog_post_all_posts_accessible(self):
        for post_id in range(1, 6):
            r = self.client.get(f'/blog/{post_id}')
            self.assertEqual(r.status_code, 200, msg=f'Post {post_id} returned {r.status_code}')

    def test_blog_post_not_found(self):
        r = self.client.get('/blog/999')
        self.assertEqual(r.status_code, 404)

    def test_contact_get(self):
        r = self.client.get('/contact')
        self.assertEqual(r.status_code, 200)
        self.assertIn(b'GRN Energy', r.data)

    def test_contact_post(self):
        r = self.client.post('/contact', data={
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test@example.com',
            'company': 'Test Co',
            'service': 'energy_audit',
            'message': 'Test message',
        })
        self.assertEqual(r.status_code, 200)
        self.assertIn(b'Thank you', r.data)


if __name__ == '__main__':
    unittest.main()
