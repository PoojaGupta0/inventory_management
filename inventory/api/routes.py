from inventory.api.views import InventoryApiViewset

from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register(r'inventory', InventoryApiViewset, basename='api-inventory')

urlpatterns = router.urls
