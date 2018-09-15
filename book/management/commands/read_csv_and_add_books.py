from django.core.management.base import BaseCommand, CommandError
from book.models import Book
from author.models import Author
import csv
import os
class Command(BaseCommand):
    help = 'Management command to read csv and create models'

    def handle(self, *args, **options):
        with open('books.csv', 'r') as table:
            fieldNames = ['authors', 'title', 'average_rating', 'ratings_count', 'image_url', 'isbn', 'isbn13', 'original_publication_year' ]
            reader = csv.DictReader(table)
            i = 0
            for row in reader:
                title = row['title']
                book = Book.objects.create(
                    title=title,
                    isbn=self.get_int(row['isbn']),
                    isbn_13=self.get_int(row['isbn13']),
                    publication_date=self.get_int(row['original_publication_year']),
                    ratings_count=self.get_int(row['ratings_count']),
                    average_ratings=self.get_float(row['average_rating']),
                    cover_image_url=row['image_url']
                )
                authors = row['authors'].split(', ')
                for name in authors:
                    book.authors.get_or_create(name=name)
                i += 1
                print("created item: ", i)


    def get_int(self, val):
        try:
            return int(float(val))
        except ValueError:
            return 0

    def get_float(self, val):
        try:
            return float(val)
        except ValueError:
            return 0.0