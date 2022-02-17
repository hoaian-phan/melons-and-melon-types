############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

        
    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    muskmelon = MelonType("musk", "1998", "green", "True", "True", "Muskmelon")
    muskmelon.add_pairing("mint")
    casaba = MelonType("cas", "2003", "orange", "False", "False", "Casaba")
    casaba.add_pairing("mint")
    casaba.add_pairing("strawberries")
    crenshaw = MelonType("cren", "1996", "green", "False", "False", "Crenshaw")
    crenshaw.add_pairing("prosciutto")
    yellow_watermelon = MelonType("yw", "2013", "yellow", "False", "True", "Yellow Watermelon")
    yellow_watermelon.add_pairing("ice cream")

    all_melon_types = [muskmelon, casaba, crenshaw, yellow_watermelon]

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f"{melon.name} pairs with")
        for pairing in melon.pairings:
            print(f"- {pairing}")


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_dict = {}
    for melon in melon_types:
        melon_dict[melon.code] = melon

    return melon_dict



############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(self, type, shape_rating, color_rating, harvested_from_field, harvested_by):
        """ Initialize a melon."""

        self.type = type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvested_from_field = harvested_from_field
        self.harvested_by = harvested_by


    def is_sellable(self):
        """ Evaluate if a melon is sellable based on 3 criteria:
        shape_rating, color_rating and not from field 3."""
        return self.shape_rating > 5 and self.color_rating > 5 and self.harvested_from_field != 3


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest
    # call make_melon_type_lookup and save it to melons_by_id dict
    melons_by_id = make_melon_type_lookup(melon_types)
    
    # look up type(e.g. 'yw') in dict to get value melon type object
    melon_1 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')
    melon_2 = Melon(melons_by_id['yw'], 3, 4, 2, 'Sheila')
    melon_3 = Melon(melons_by_id['yw'], 9, 8, 3, 'Sheila')
    melon_4 = Melon(melons_by_id['cas'], 10, 6, 35, 'Sheila')
    melon_5 = Melon(melons_by_id['cren'], 8, 9, 35, 'Michael')
    melon_6 = Melon(melons_by_id['cren'], 8, 2, 35, 'Michael')
    melon_7 = Melon(melons_by_id['cren'], 2, 3, 4, 'Michael')
    melon_8 = Melon(melons_by_id['musk'], 6, 7, 4, 'Michael')
    melon_9 = Melon(melons_by_id['yw'], 7, 10, 3, 'Sheila')

    all_melons_list = [melon_1, melon_2, melon_3, melon_4, melon_5, melon_6, melon_7, melon_8, melon_9]

    return all_melons_list

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""
    
    for melon in melons:
        can_be_sold = "NOT SELLABLE"
        if melon.is_sellable():
            can_be_sold = "CAN BE SOLD"
            
        print(f"Harvested by {melon.harvested_by} from Field {melon.harvested_from_field} ({can_be_sold})")
