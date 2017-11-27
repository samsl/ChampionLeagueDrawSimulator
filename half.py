import time

from math import ceil

from club import Club
from category import Category
class Half:

    def __init__(self, clubs):
        self.category = Category()
        self.category.add_clubs(clubs)


    def toss(self, clubs, size):
        result = []
        if size == 0:
            result.append([])
            return result
        if len(clubs) == size:
            result.append(clubs)
            return result
        result_out = self.toss(clubs[1:], size)
        result_in = self.toss(clubs[1:], size-1)
        for i in result_in:
            i.insert(0, clubs[0])

        return result_in + result_out
    def toss_result(self, clubs):
        results = self.toss(clubs, len(clubs)/2)
        toss_result = []
        for result in results:
            toss_result.append([result, list(set(clubs).difference(set(result)))])
        return toss_result

    def full_permutation(self, clubs):
        results = []


        pot1_toss = self.toss_result(clubs[1])
        pot2_toss = self.toss_result(clubs[2])
        pot3_toss = self.toss_result(clubs[3])
        pot4_toss = self.toss_result(clubs[4])

        for i in pot1_toss:
            half_category = Category()
            half_category.add_clubs(i[0])
            if not self.rough_filter(half_category):

                continue
            for j in pot2_toss:
                half_category.add_clubs(j[0])
                if not self.rough_filter(half_category):
                    half_category.remove_clubs(j[0])
                    continue
                for p in pot3_toss:
                    half_category.add_clubs(p[0])
                    if not self.rough_filter(half_category):
                        half_category.remove_clubs(p[0])
                        continue
                    for q in pot4_toss:
                        result = {}
                        half_category.add_clubs(q[0])
                        upper_half_full_set = [i[0], j[0], p[0], q[0]]
                        bottom_half_full_set = [i[1], j[1], p[1], q[1]]
                        if self.filter(half_category):
                            for pot in upper_half_full_set:
                                for club in pot:
                                    result[club.name] = ['A', 'B', 'C', 'D']
                            for pot in bottom_half_full_set:
                                for club in pot:
                                    result[club.name] = ['E', 'F', 'G', 'H']
                            results.append(result)
                        half_category.remove_clubs(q[0])
                    half_category.remove_clubs(p[0])
                half_category.remove_clubs(j[0])


        return results
#todo: refactor
    def classify(self, clubs):
        pots = {}
        for club in clubs:
            if club.pot not in pots:
                pots[club.pot] = []
            pots[club.pot].append(club)
        return pots

    def rough_filter(self, half_category):
        # for key, value in self.category.assciaiton_category.items():
        #     count = 0
        #     if len(value) > 1 and key in half_category.assciaiton_category:
        #
        #         if len(half_category.assciaiton_category[key]) > ceil(len(value) / 2):
        #             return False
        #         for club in half_category.assciaiton_category[key]:
        #             if club.top_two:
        #                 count += 1
        #         if count == 2:
        #             return False
        # return True
        for key, value in half_category.assciaiton_category.items():
            count = 0
            if len(value) > ceil(len(self.category.assciaiton_category[key]) / 2):
                return False
            for club in value:
                if club.top_two:
                    count += 1
            if count == 2:
                return False
        return True

    def filter(self, half_category):

        for key, value in self.category.assciaiton_category.items():
            count = 0
            if len(value) > 1:

                if key not in half_category.assciaiton_category or abs(len(half_category.assciaiton_category[key]) - len(value)/2) >= 1:
                    return False
                for club in half_category.assciaiton_category[key]:
                    if club.top_two:
                        count += 1
                if count == 2:
                    return False
        for key, value in self.category.city_category.items():
            if len(value) > 1:

                if key not in half_category.city_category or abs(len(half_category.city_category[key]) - len(value)/2) >= 1:
                    return False

        return True

if __name__ == '__main__':

    clubs = [
        Club('Juventus', 'Italy', 'Torino', True, 1), Club('Real Madrid', 'Spain', 'Madrid', True, 1),
        Club('Bayern', 'German', 'Munchen', True, 1), Club('Benfica', 'Portugal', 'Lisboa', True, 1),
        Club('Chelsea', 'England', 'London', True, 1), Club('Monaco', 'France', 'Monaco', True,1),
        Club('Spartak, Moskva', 'Russia', 'Moscow', True, 1), Club('Shakhtar Donetsk', 'Ukraine', 'Donetsk', True, 1),
        Club('Manchester United', 'England', 'Manchester', False, 2), Club('Paris', 'France', 'Paris', True, 2),
        Club('Atletico', 'Spain', 'Madrid', False, 2), Club('Barcelona', 'Spain', 'Barcelona', True, 2),
        Club('Sevilla', 'Spain', 'Sevilla', False, 2), Club('Man City', 'England', 'Manchester', True, 2),
        Club('Porto', 'Portugal', 'Porto', True, 2), Club('Dortmund', 'German', 'Dortmund', True, 2),
        Club('Basel', 'Switzerland', 'Basel', True, 3), Club('Anderlecht', 'Belgium', 'Anderlecht', True, 3),
        Club('Roma', 'Italy', 'Roma', False, 3), Club('Olympiacos', 'Greece', 'Piraeus', True, 3),
        Club('Liverpool', 'England', 'Liverpool', False, 3), Club('Napoli', 'Italy', 'Napoli', True, 3),
        Club('Besiktas' , 'Turnkey', 'Besiktas', True, 3), Club('Tottenham Hotspur', 'England', 'London', False, 3),
        Club('CSKA Moskva', 'Russia', 'Moscow', True, 4), Club('Celtic', 'Scotland', 'Glasgow', True, 4),
        Club('Qarabag', 'Azerbaijan', 'Baku', True, 4), Club('Sporting CP', 'Portugal', 'Lisboa', False, 4),
        Club('Maribor', 'Slovenia', 'Maribor', True, 4), Club('Feyenoord','Netherland', 'Rotterdam', True, 4),
        Club('RB Leipzig', 'German', 'Leipzig', False, 4), Club('APOEL', 'Cyprus', 'Nicosia', True, 4)
             ]
    half = Half(clubs)
    pots = half.classify(clubs)
    result = half.full_permutation(pots)
