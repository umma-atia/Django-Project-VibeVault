from django.urls import path, include
from product.views import ProductViewSet, CategoryViewSet, ReviewViewSet
from order.views import CartViewSet, CartItemViewSet, OrderViewset, WishlistViewSet, initiate_payment, payment_success, payment_cancel, payment_fail, HasOrderedProduct
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('products', ProductViewSet, basename='products')
router.register('categories', CategoryViewSet)
router.register('carts', CartViewSet, basename='carts')
router.register('orders', OrderViewset, basename='orders')
router.register('Wishlists', WishlistViewSet, basename='wishlist')

product_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
product_router.register('reviews', ReviewViewSet, basename='product-review')

cart_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
cart_router.register('items', CartItemViewSet, basename='cart-item')


urlpatterns = [
    path('', include(router.urls)),
    path('', include(product_router.urls)),
    path('', include(cart_router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path("payment/initiate/", initiate_payment, name="initiate-payment"),
    path("payment/success/", payment_success, name="payment-success"),
    path("payment/fail/", payment_fail, name="payment-fail"),
    path("payment/cancel/", payment_cancel, name="payment-cancel"),
    path('orders/has-ordered/<int:product_id>/', HasOrderedProduct.as_view()),
]