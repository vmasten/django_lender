from django.db import models

class Book(models.Model):
    AVAILABLE = 'AV'
    CHECKED_OUT = 'CO'
    STATUS_CHOICES = (
        (AVAILABLE, 'available'),
        (CHECKED_OUT, 'checked out')
    )
    cover_image = models.ImageField()
    title = models.TextField()
    author = models.TextField()
    year = models.CharField(max_length=4)
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=AVAILABLE)
    date_added = models.DateTimeField(auto_now_add=True)
    last_borrowed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} ({self.status})'
