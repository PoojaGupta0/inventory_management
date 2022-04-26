from django_filters.rest_framework import DjangoFilterBackend
from inventory.api.serializers import InventorySerializer
from inventory.models import Inventory
from rest_framework import filters, viewsets


class InventoryApiViewset(viewsets.ModelViewSet):
    """
    API end point returns the inventory list with their suppliers.
    Filter available by name.

    e.g. api/inventory/?name=item or /?search=item
    """
    model = Inventory
    serializer_class = InventorySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name']

    def get_queryset(self):
        return self.model.objects.select_related('supplier')
