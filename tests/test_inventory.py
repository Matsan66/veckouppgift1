import pytest
from inventory import Inventory
from item import Item

# Preparing test data and test environment

@pytest.fixture
def inventory():
    """
    Creates an inventory item for testing.
    """
    return Inventory()


@pytest.fixture
def compass():
    """
    Creates a compass item for testing.
    """
    return Item("Compass", 25, 30)


@pytest.fixture
def hiking_poles():
    """
    Creates hiking_poles item for testing.
    """
    return Item("Hiking poles", 40, 20)


@pytest.fixture
def backpack():
    """
    Creates a backpack item for testing.
    """
    return Item("Backpack", 50, 15)


# Tests to verify Inventory methods

def test_set_get_item(inventory, compass):
    """
    Tests set_item() and get_amount_left() methods basically
    """
    inventory.set_item(compass.name, compass.rent_price, compass.amount)

    assert inventory.get_amount_left(compass.name) == 30


def test_get_amount_left(inventory, compass):
    """
    Tests get_amount_left() method with full stock
    """
    inventory.set_item(compass.name, compass.rent_price, compass.amount)

    assert inventory.get_amount_left(compass.name) == 30


def test_rent(inventory, compass):
    """
    Tests rent() method by renting one item
    """
    inventory.set_item(compass.name, compass.rent_price, compass.amount)

    inventory.rent(compass.name)

    assert inventory.get_amount_left(compass.name) == 29

def test_rent_no_items(inventory, compass):
    """
    Tests rent() method with no items to rent
    """
    inventory.set_item(compass.name, compass.rent_price, 0)

    inventory.rent(compass.name)

    assert inventory.get_amount_left(compass.name) == 0

def test_rent_multiple_same_items(inventory, compass):
    """
    Tests rent() method when renting multiple items
    """

    inventory.set_item(compass.name, compass.rent_price, compass.amount)

    inventory.rent(compass.name)
    inventory.rent(compass.name)
    inventory.rent(compass.name)

    assert inventory.get_amount_left(compass.name) == 27

def test_rent_correct_item_from_multiple_items(inventory, compass, hiking_poles, backpack):
    """
    Tests rent() method that renting one item does not affect other items in the inventory.
    """
    inventory.set_item(compass.name, compass.rent_price, compass.amount)
    inventory.set_item(hiking_poles.name, hiking_poles.rent_price, hiking_poles.amount)
    inventory.set_item(backpack.name, backpack.rent_price, backpack.amount)

    inventory.rent(compass.name)

    assert inventory.get_amount_left(compass.name) == 29
    assert inventory.get_amount_left(hiking_poles.name) == 20
    assert inventory.get_amount_left(backpack.name) == 15


def test_rent_multiple_different_items(inventory, compass, hiking_poles, backpack):
    """
    Tests rent() method when multiple different items are rented
    """
    inventory.set_item(compass.name, compass.rent_price, compass.amount)
    inventory.set_item(hiking_poles.name, hiking_poles.rent_price, hiking_poles.amount)
    inventory.set_item(backpack.name, backpack.rent_price, backpack.amount)

    inventory.rent(compass.name)
    inventory.rent(hiking_poles.name)
    inventory.rent(backpack.name)

    assert inventory.get_amount_left(compass.name) == 29
    assert inventory.get_amount_left(hiking_poles.name) == 19
    assert inventory.get_amount_left(backpack.name) == 14


def test_rent_non_existing_item(inventory, compass):
    """
    Tests rent() method that renting a non-existing item does not affect the inventory.
    """
    inventory.set_item(compass.name, compass.rent_price, compass.amount)

    inventory.rent("Boots")

    assert inventory.get_amount_left(compass.name) == 30