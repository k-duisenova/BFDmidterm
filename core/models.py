from django.db import models
from util.types import TYPES, SPORT


class BookJournalBase(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    created_at = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Book journal'
        verbose_name_plural = 'Book journals'


class Book(BookJournalBase):
    num_pages = models.IntegerField()
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.genre

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class Journal(BookJournalBase):
    type = models.SmallIntegerField(choices=TYPES, default=SPORT)
    publisher = models.CharField(max_length=255)

    def __str__(self):
        return self.publisher

    class Meta:
        verbose_name = 'Журнал'
        verbose_name_plural = 'Журналы'