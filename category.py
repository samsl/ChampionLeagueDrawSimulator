class Category:
    def __init__(self):

        self.assciaiton_category = {}

        self.city_category = {}


    def remove_club(self, club):
        self.assciaiton_category[club.association].remove(club)
        self.city_category[club.city].remove(club)

    def add_club(self, club):
        if club.association not in self.assciaiton_category:
            self.assciaiton_category[club.association] = []
        self.assciaiton_category[club.association].append(club)

        if club.city not in self.city_category:
            self.city_category[club.city] = []
        self.city_category[club.city].append(club)



    def add_clubs(self, clubs):
        for club in clubs:
            self.add_club(club)

    def remove_clubs(self, clubs):
        for club in clubs:
            self.remove_club(club)
