from django.shortcuts import render, get_object_or_404
from ninja import NinjaAPI
from .models import Order
from .schema import OrderSchema, OrderCreateSchema

api = NinjaAPI()


@api.get("/orders", response=list[OrderSchema])
def list_orders(request):
    user_id = request.user.id
    return Order.objects.filter(user_id=user_id)


@api.get("/orders/{order_id}", response=OrderSchema)
def get_order(request, order_id: int):
    order = get_object_or_404(Order, id=order_id)
    return order


@api.post("/orders", response=OrderSchema)
def create_order(request, payload: OrderCreateSchema):
    user_id = request.user.id
    order = Order.objects.create(user_id=user_id, **payload.dict())
    return order


@api.put("/orders/{order_id}", response=OrderSchema)
def update_order(request, order_id: int, payload: OrderCreateSchema):
    order = get_object_or_404(Order, id=order_id)
    for attr, value in payload.dict().items():
        setattr(order, attr, value)
    order.save()
    return order


@api.delete("/orders/{order_id}", response={204: None})
def delete_order(request, order_id: int):
    order = get_object_or_404(Order, id=order_id)
    order.delete()
    return 204


# Add the API to your Django project
from django.urls import path

urlpatterns = [
    path("", api.urls),
]
