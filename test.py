from app import app
import unittest

class FlaskTestCase(unittest.TestCase):

	# Ensure that Flask was set up correctly
	def test_index(self):
		tester = app.test_client(self)
		response = tester.get('/', content_type='html/text')
		self.assertEqual(response.status_code, 200)


	# Ensure that the index page loads correctly
	def test_index_page_loads(self):
		tester = app.test_client(self)
		response = tester.get('/', content_type='html/text')
		self.assertTrue(b'Login' in response.data)


	# Ensure that the index page loads correctly
	def test_correct_login(self):
		tester = app.test_client(self)
		response = tester.post(
			'/login',
			data=dict(username="nick@nick.com", password="nick"),
			follow_redirects=True
		)
		self.assertIn(b"You've been logged in!", response.data)

if __name__ == '__main__':
	unittest.main()