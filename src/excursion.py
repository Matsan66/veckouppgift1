

class Excursion:
    """
        Class excursion represents an excursion with members and items rented
    """
    def __init__(self):
        """
        Creates a new empty excursion
        """
        self.members_list = []
        self.items_rented_list = []


    def get_members(self):
        """
        Returns the members enrolled in the excursion
        """
        return self.members_list


    def add_member(self, name):
        """
        Adds a member to the excursion
        """
        self.members_list.append(name)


    def remove_member(self, name):
        """
        Removes a member from the excursion
        """
        for member in self.members_list:
            if member == name:
                self.members_list.remove(member)


    def register_item_rented(self, member_name, item_name):
        """
        Registers an item rented by a member
        """
        self.items_rented_list.append([member_name, item_name])


    def register_item_returned(self, member_name, item_name):
        """
        Registers a rented item returned by a member
        """
        for item in self.items_rented_list:
            if item[0] == member_name and item[1] == item_name:
                self.items_rented_list.remove(item)

    def get_all_who_has_not_returned_items(self):
        """
        Returns the names of all members who have not return their items rented
        """
        not_returned_names_list = []

        for item in self.items_rented_list:
            if item[0] not in not_returned_names_list:
                not_returned_names_list.append(item[0])

        return not_returned_names_list






