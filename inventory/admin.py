from django.contrib import admin

from .models import Inventory, Supplier


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    
    def get_supplier(self, inst):
        return inst.name

    list_display = ('name', 'description', 'stock', 'availability', 'supplier')


@admin.register(Supplier)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

