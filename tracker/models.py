from django.db import models

CATEGORY_CHOICES = (
    ('Food', 'Food'),
    ('Travel', 'Travel'),
    ('Shopping', 'Shopping'),
    ('Bills', 'Bills'),
)

class Expense(models.Model):

    title = models.CharField(max_length=100)

    amount = models.FloatField()

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title