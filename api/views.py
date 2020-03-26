from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from .serializers import ItemSerializer
from .models import Item, Cart


@api_view(["POST"])
def add_item_to_cart(request):
    serializer = ItemSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    cart_id = request.COOKIES.get('cart_id', None)
    cart, created = Cart.objects.get_or_create(id=cart_id)
    #
    # print("CART NEW")
    # print(cart)
    # print(created)

    item = get_object_or_404(
        Item, external_id=serializer.validated_data["external_id"]
    )

    if getattr(item, "cart") == cart:
        # print("changing")
        item.name = serializer.validated_data.get("name", item.name)
        item.value = serializer.validated_data.get("value", item.value)
    else:
        # print('add cart')
        item.cart = cart

    item.save()

    response = Response(status=status.HTTP_204_NO_CONTENT)

    if created:
        response.set_cookie('cart_id', cart.id, max_age=60*60*72)

    return response
