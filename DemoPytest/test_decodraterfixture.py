import pytest

# this file has 1 fixture decorator related testcase

# setup and teardown function handling through fixture function
# in this file, going to explore setup function using fixture decorator
class Fruit:
    def __init__(self,name):
        self.name = name
        self.cubed = False
    def cube(self):
        self.cubed = True

class FruitSalad:
    def __init__(self,*fruit_bowl):
        self.fruit = fruit_bowl
        self._cube_fruit()
    def _cube_fruit(self):
        for fruit in self.fruit:
            fruit.cube()

#Arrange
@pytest.fixture
def fruit_bowl():
    """function definition for fixture decorator sample """
    print("\n Prerequisite steps prior to run the test case execution...")
    print("\n In this case, we have keep the fruits details in the list data type...")
    return [Fruit("apple"),Fruit("banana")]

def test_fruit_salad(fruit_bowl):
    """this test case indicate fixture function usage"""
    #Act
    fruit_salad = FruitSalad(*fruit_bowl)
    #Assert
    assert all(fruit.cubed for fruit in fruit_salad.fruit)


