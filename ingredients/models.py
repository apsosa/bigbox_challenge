from django.db import models

# Create your models here.
# cookbook/ingredients/models.py

class CategoryI(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField()
    category = models.ForeignKey(
        CategoryI, related_name="ingredients", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name