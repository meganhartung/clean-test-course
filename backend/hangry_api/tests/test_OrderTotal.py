from api.controllers import Delivery, Subtotal, Tax, Total
from django_mock_queries.query import MockSet, MockModel


def test_OrderWithDefaultDeliveryFee():
  order = MockSet(MockModel(quantity=3, item=MockModel(price=5.0)))

  delivery_fee = Delivery.calculate(order, 2)

  assert delivery_fee == 3.50
  assert Tax.calculate(Subtotal.calculate(order), delivery_fee) == 1.53
  assert Total.calculate(order, delivery_fee) == 20.03
