class Club:
    def __init__(self, name, association, city, top_two, pot):
        self._name = name
        self._association = association
        self._city = city
        self._top_two = top_two
        self._pot = pot

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def association(self):
        return self._association

    @association.setter
    def association(self, association):
        self._association = association

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        self._city = city

    @property
    def top_two(self):
        return self._top_two

    @top_two.setter
    def top_two(self, top_two):
        self._top_two = top_two

    @property
    def pot(self):
        return self._pot

    @pot.setter
    def pot(self, pot):
        self._pot = pot

    def __hash__(self):
        return hash(self.name + self.association + str(self.top_two) + self.city + str(self.pot))

    def __eq__(self, other):
        if self.city == other.city and self.top_two == other.top_two and self.pot == other.pot and self.name == other.name and self.association == other.association:
            return True
        return False
