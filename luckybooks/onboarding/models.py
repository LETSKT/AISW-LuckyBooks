from djongo import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publiser = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    published = models.DateField()
    cover_url = models.URLField()
    category = models.CharField(max_length=255)
    def __str__(self):
        return self.title
    
    
class User(models.Model):
    nickname = models.CharField(max_length=127)
    gender = models.CharField(max_length=1)
    age = models.IntegerField()
    preferred_books = models.ManyToManyField(Book)
    preferred_authors = models.ManyToManyField(Book, through='BookAuthor')
    preferred_genres = models.ManyToManyField(Book, through='BookGenre')
    
class BookShelf(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)