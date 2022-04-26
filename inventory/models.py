from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=200, help_text="Supplier Name")

    def __str__(self) -> str:
        return self.name

class Inventory(models.Model):
    name = models.CharField(max_length=200, help_text='Product Name')
    description = models.CharField(max_length=300)
    note = models.CharField(max_length=200, null=True, blank=True)
    stock = models.IntegerField(default=0)
    availability = models.BooleanField(default=False)
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        related_name='inventories'
    )

    def __str__(self) -> str:
        return self.name