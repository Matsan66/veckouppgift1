import pytest
from excursion import Excursion
from item import Item



# Preparing test data and test environment

@pytest.fixture
def excursion():
    """
    Creates an excursion item for testing.
    """
    return Excursion()

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
    Creates backpack item for testing.
    """

    return Item("Backpack", 50, 15)



# Tests to verify Excursion methods

def test_add_get_member(excursion):

    excursion.add_member("Johan Olsson")

    assert excursion.get_members() == ["Johan Olsson"]

def test_add_get_member_many_members(excursion):

    excursion.add_member("Johan Olsson")
    excursion.add_member("Gunilla Jönsson")
    excursion.add_member("Bo Andersson")

    assert excursion.get_members() == ["Johan Olsson", "Gunilla Jönsson", "Bo Andersson"]


def test_remove_member(excursion):

    excursion.add_member("Johan Olsson")
    excursion.remove_member("Johan Olsson")

    assert excursion.get_members() == []


def test_register_item_rented(excursion, compass):

    excursion.add_member("Johan Olsson")

    excursion.register_item_rented("Johan Olsson", compass.name)

    assert excursion.items_rented_list == [["Johan Olsson", "Compass"]]


def test_register_item_returned(excursion, compass):

    excursion.add_member("Johan Olsson")

    excursion.register_item_rented("Johan Olsson", compass.name)
    excursion.register_item_returned("Johan Olsson", compass.name)

    assert excursion.items_rented_list == []


def test_get_all_who_has_not_returned_items_one_member(excursion, compass):

    excursion.add_member("Johan Olsson")

    excursion.register_item_rented("Johan Olsson", compass.name)

    assert excursion.get_all_who_has_not_returned_items() == ["Johan Olsson"]


def test_get_all_who_has_not_returned_items_member_many_items(excursion, compass, hiking_poles):

    excursion.add_member("Johan Olsson")

    excursion.register_item_rented("Johan Olsson", compass.name)
    excursion.register_item_rented("Johan Olsson", hiking_poles.name)

    assert excursion.get_all_who_has_not_returned_items() == ["Johan Olsson"]


def test_get_all_who_has_not_returned_items_member_return_one(excursion, compass, hiking_poles):

    excursion.add_member("Johan Olsson")

    excursion.register_item_rented("Johan Olsson", compass.name)
    excursion.register_item_rented("Johan Olsson", hiking_poles.name)

    excursion.register_item_returned("Johan Olsson", compass.name)

    assert excursion.get_all_who_has_not_returned_items() == ["Johan Olsson"]


def test_get_all_who_has_not_returned_items_member_return_all(excursion, compass, hiking_poles):

    excursion.add_member("Johan Olsson")

    excursion.register_item_rented("Johan Olsson", compass.name)
    excursion.register_item_rented("Johan Olsson", hiking_poles.name)

    excursion.register_item_returned("Johan Olsson", compass.name)
    excursion.register_item_returned("Johan Olsson", hiking_poles.name)

    assert excursion.get_all_who_has_not_returned_items() == []


def test_get_all_who_has_not_returned_items_many_members(excursion, compass, hiking_poles):

    excursion.add_member("Johan Olsson")
    excursion.add_member("Gunilla Jönsson")

    excursion.register_item_rented("Johan Olsson", compass.name)
    excursion.register_item_rented("Gunilla Jönsson", hiking_poles.name)

    assert excursion.get_all_who_has_not_returned_items() == ["Johan Olsson", "Gunilla Jönsson"]


def test_get_all_who_has_not_returned_items_members_many_items(excursion, compass, hiking_poles, backpack):

    excursion.add_member("Johan Olsson")
    excursion.add_member("Gunilla Jönsson")
    excursion.add_member("Bo Andersson")

    excursion.register_item_rented("Johan Olsson", compass.name)
    excursion.register_item_rented("Johan Olsson", hiking_poles.name)
    excursion.register_item_rented("Gunilla Jönsson", compass.name)
    excursion.register_item_rented("Bo Andersson", backpack.name)

    assert excursion.get_all_who_has_not_returned_items() == ["Johan Olsson", "Gunilla Jönsson", "Bo Andersson"]



