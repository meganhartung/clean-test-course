from api.controllers import Delivery
from django_mock_queries.query import MockSet, MockModel
import pytest

def test_LotsOfItems():
  #Arrange
  order = MockSet()
  order.add(MockModel(quantity=5))
  order.add(MockModel(quantity=5))
  order.add(MockModel(quantity=5))
  delivery_distance = 6
  #Act
  cost = Delivery.calculate(order,delivery_distance)
  #Assert
  assert cost == 7.5

def test_MiddleOfTheRoadItems():
  #Arrange
  order = MockSet()
  order.add(MockModel(quantity=2))
  order.add(MockModel(quantity=2))
  order.add(MockModel(quantity=2))
  delivery_distance = 4
  #Act
  cost = Delivery.calculate(order,delivery_distance)
  #Assert
  assert cost == 5

def test_LittleItems():
  #Arrange
  # TODO: Arrange the items to run the test
  order = MockSet()
  order.add(MockModel(quantity=3))
  order.add(MockModel(quantity=1))
  del_dist = 2
  #Act
  # TODO: Call the function that will be tested
  cost = Delivery.calculate(order, del_dist)
  #Assert
  # TODO: replace the pass with an assert to test the value returned.
  assert cost == 3.50

@pytest.mark.parametrize('quantity,distance', [
  (0, 0),
  (5, 6),
  (6, 3),
  (11, 3),
])
def test_DefaultFeeAtTierBoundaries(quantity, distance):
  order = MockSet(MockModel(quantity=quantity))

  assert Delivery.calculate(order, distance) == 3.50
