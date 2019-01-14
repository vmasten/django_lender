"""Tests on the model and views for the book lender app."""
from django.test import TestCase, RequestFactory, Client
from .models import Book
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


class TestBookModel(TestCase):
    """Tests for the model."""

    def setUp(self):
        """Create some book instances."""

        user = User.objects.create_user('test', 'user@example.com', 'pass')

        Book.objects.create(
                            title='Sphere',
                            author='Michael Chrichton',
                            year='1992',
                            status='AV',
                            user=user)
        Book.objects.create(
                            title='The Killing Floor',
                            author='Lee Child',
                            year='1996',
                            status='CO',
                            user=user)
        Book.objects.create(
                            title='The Lovely Bones',
                            author='Alice Sebold',
                            year='2002',
                            status='AV',
                            user=user)

    def test_book_titles(self):
        """Test whether title field is correct."""
        first = Book.objects.get(title='Sphere')
        self.assertEqual(first.title, 'Sphere')

    def test_book_authors(self):
        """Test the author field of the db."""
        books = Book.objects.all()
        self.assertEqual(books[2].author, 'Alice Sebold')

    def test_image_upload(self):
        """Simulate image upload into the db's ImageField."""
        books = Book.objects.all()
        books[0].cover_image = SimpleUploadedFile(
            name='jp.jpg',
            content=open('/src/lender_books/media/jp.jpg', 'rb').read(),
            content_type='image/jpeg')

    def test_year(self):
        """Test the year field."""
        test = Book.objects.get(year=1996)
        self.assertEqual(test.author, 'Lee Child')

    def test_status(self):
        """Test the status field."""
        test = Book.objects.get(title='The Lovely Bones')
        self.assertEqual(test.status, 'AV')


class TestBookViews(TestCase):
    """Class to test the views."""

    def setUp(self):

        user = User.objects.create_user('test', 'user@example.com', 'pass')

        """Create some more book instances."""
        self.request = RequestFactory()

        self.book = Book.objects.create(
                                        title='Sphere',
                                        cover_image='jp.jpg',
                                        author='Michael Chrichton',
                                        year='1992',
                                        status='AV',
                                        user=user)
        Book.objects.create(
                            title='The Killing Floor',
                            author='Lee Child',
                            year='1996',
                            status='CO',
                            user=user)
        Book.objects.create(
                            title='The Lovely Bones',
                            author='Alice Sebold',
                            year='2002',
                            status='AV',
                            user=user)

        self.client = Client()
        self.client.force_login(user=user, backend=None)

    def test_list_view_context(self):
        """Test the book list view."""
        from .views import book_list
        request = self.client.get('', follow=True)
        response = book_list(request)
        self.assertIn(b'Sphere', response.content)

    def test_list_view_status(self):
        """Test the return status on the list view."""
        from .views import book_list
        request = self.request.get('')
        response = book_list(request)
        self.assertEqual(200, response.status_code)

    def test_detail_view_context(self):
        """Test the detail view."""
        from .views import book_detail
        request = self.request.get('')
        response = book_detail(request, self.book.id)
        self.assertIn(b'Michael Chrichton', response.content)

    def test_detail_view_failure(self):
        """Test a bad route."""
        from .views import book_detail
        from django.http import Http404
        request = self.request.get('')

        with self.assertRaises(Http404):
            book_detail(request, '0')
