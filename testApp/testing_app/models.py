from django.db import models


# Create your models here.

class Book(models.Model):
   # test_number = models.IntegerField(default=0)  # number question
    #test_question = models.TextField(max_length=200)  # question
    #test_answer_first = models.TextField(max_length=50)  # answer
    #test_answer_second = models.TextField(max_length=50)  # answer
    #test_answer_third = models.TextField(max_length=50)  # answer
    #test_answer_fourth = models.TextField(max_length=50)  # answer
    BOOK_CHOICES = (
        ('1234qwe', 'qwertrtty'),
        ('1234qwe', 'qwertrtty'),
        ('1234qwe', 'qwertrtty'),
        ('1234qwe', 'qwertrtty'),
        ('1234qwe', 'qwertrtty'),
        )

    BOOK1_CHOICES = (
        ('1234qwe', 'qwertrtty'),
        ('1234qwe', 'qwertrtty'),
        ('1234qwe', 'qwertrtty'),
        ('1234qwe', 'qwertrtty'),
        ('1234qwe', 'qwertrtty'),

    )
    title = models.CharField(max_length = 100, choices = BOOK_CHOICES, name = "vasya")
    title1 = models.CharField(max_length=100, choices=BOOK1_CHOICES, name="vasya1")
    class Meta():
        db_table = "Book"

"""class Book1(models.Model):
   # test_number = models.IntegerField(default=0)  # number question
    #test_question = models.TextField(max_length=200)  # question
    #test_answer_first = models.TextField(max_length=50)  # answer
    #test_answer_second = models.TextField(max_length=50)  # answer
    #test_answer_third = models.TextField(max_length=50)  # answer
    #test_answer_fourth = models.TextField(max_length=50)  # answer
    BOOK1_CHOICES = (
        ('1234qwe', 'qwertrtty'),
        ('1234qwe', 'qwertrtty'),
        ('1234qwe', 'qwertrtty'),
        ('1234qwe', 'qwertrtty'),
        ('1234qwe', 'qwertrtty'),

    )
    title = models.CharField(max_length = 100, choices = BOOK1_CHOICES, name = "vasya1")
    class Meta():
        db_table = "Book1" """
