from inventory.models import Inventory
from rest_framework import serializers


class InventorySerializer(serializers.ModelSerializer):
    supplier_name = serializers.SerializerMethodField()

    def get_supplier_name(self, inst):
        return getattr(inst.supplier, 'name', '')

    class Meta:
        model = Inventory
        fields = ['id', 'name', 'stock', 'availability', 'supplier', 'supplier_name']
