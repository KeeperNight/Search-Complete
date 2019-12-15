from django.db import models
from multiselectfield import MultiSelectField
from django.urls import reverse
from author.models import Author
from django.contrib.auth.models import User


class Book(models.Model):
    name = models.CharField(max_length=100)
    rating = models.PositiveIntegerField(default=0)
    PUBLISHED = (('D', 'Draft'), ('P', 'Published'))
    image = models.ImageField(default='default.jpg', upload_to='Book_covers')
    published = models.CharField(max_length=2, choices=PUBLISHED)
    GENRE = (('R', 'Romance'), ('D', 'Drama'), ('F', 'Fiction'), ('M', 'Mystery'))
    genre = MultiSelectField(choices=GENRE)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    book_creator = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'pk': self.pk})
