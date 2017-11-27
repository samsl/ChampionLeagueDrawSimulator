import random
import time

from club import Club
from half import Half

class Group:


    def __init__(self, clubs):

        half = Half(clubs)
        self.clubs = half.classify(clubs)
        self.group_candidate = half.full_permutation(self.clubs)

        self.upper_group = ['A', 'B', 'C', 'D']
        self.bottom_group = ['E', 'F', 'G', 'H']




    def draw(self):
        for i in range(1, 5):
            for j in range(0, 8):
                club = group.pick_one_club(i)
                group.pick_one_group(club)
            self.upper_group = ['A', 'B', 'C', 'D']
            self.bottom_group = ['E', 'F', 'G', 'H']

    def pick_one_club(self, pot):
        if pot > 4 or pot < 1:
            print('Pot should be in range 1..4')
        candidates = self.clubs[pot]
        club = random.choice(candidates)
        print('Club %s is picked' % club.name)
        candidates.remove(club)
        return club

    def find_group_candidate(self, club):
        candidate = []

        for chance in self.group_candidate:
            candidate = list(set(candidate + chance[club.name]))
            if set(candidate) == set(self.upper_group + self.bottom_group):
                break



        for group in candidate.copy():

            for chance in self.group_candidate:
                no_answer = False
                for other_club in self.clubs[club.pot]:
                    if group in chance[other_club.name]:
                        if len(chance[other_club.name]) == 1:
                            no_answer = True
                            break
                if not no_answer:
                    break
            if no_answer:
                candidate.remove(group)

        print('Group candidates are %s' % candidate)
        return candidate

    def oppsite_association(self, association1, association2):
        if {association1, association2} == {'Ukraine', 'Russia'}:
            return True

        return False

    def pick_one_group(self, club):
        group_candidates = self.find_group_candidate(club)
        group = random.choice(group_candidates)
        print('to Group %s' % group)

        self.refine_result(club, group)


    def refine_result(self, club, group):

        # Remove when club in different half
        self.group_candidate[:] = [x for x in self.group_candidate if group in x[club.name]]

        for chance in self.group_candidate:
            # Remove the possibility other club with the same pot into the same group
            for not_picked_club in self.clubs[club.pot]:
                if group in chance[not_picked_club.name]:
                    chance[not_picked_club.name].remove(group)
            # Remove the possibility other club with different pot but the same association or conflict into the same group
            for pot in range(club.pot+1, 5):
                for not_picked_club in self.clubs[pot]:
                    if group in chance[not_picked_club.name]:
                        if not_picked_club.association == club.association:
                            chance[not_picked_club.name].remove(group)
                        if self.oppsite_association(not_picked_club.association, club.association):
                            chance[not_picked_club.name].remove(group)

        for chance in self.group_candidate.copy():
            for pot in range(club.pot, 5):
                for not_picked_club in self.clubs[pot]:
                    if not len(chance[not_picked_club.name]):
                        self.group_candidate.remove(chance)


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
    time_start = time.time()
    group = Group(clubs)
    group.draw()
    time_end = time.time()
    print(time_end - time_start)

