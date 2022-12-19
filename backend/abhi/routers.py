from rest_framework.routers import DefaultRouter
from products.viewsets import productviewset

router = DefaultRouter()
router.register('product-abc',productviewset, basename ='products')

#print(router.urls)

urlpatterns = router.urls
# this routers.py does that automatically route the link without or skip the process whome we
#  do manaully go and set url.py and for me view.py is better then viewsets.py