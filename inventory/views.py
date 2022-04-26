from django.views.generic.detail import DetailView

from .models import Inventory


class InventoryDetailView(DetailView):
    queryset = Inventory.objects.select_related('supplier')
