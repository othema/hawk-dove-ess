import random
from itertools import zip_longest
from collections import defaultdict, Counter

STARTING_POPULATION = {
    "dove": 10,
    "hawk": 1
}
FOOD = 20


class Simulation:
    def __init__(self):
        self.creatures = []
        for species, count in STARTING_POPULATION.items():
            self.creatures.extend([species] * count)
        
    def step(self):
        contests = assign_to_food(self.creatures)

        new_populations = defaultdict(int)

        for contest in contests:
            if len(contest) == 1:  # No contest
                species = contest[0]
                new_populations[species] += 2

            else:  # Contest
                s1 = contest[0]
                s2 = contest[1]
                result = compete(s1, s2)
                new_populations[s1] += result[0]
                new_populations[s2] += result[1]
        
        self.creatures.clear()
        for species, count in new_populations.items():
            self.creatures.extend([species] * count)

    def get_total_creatures(self):
        return len(self.creatures)

    def get_species_total(self):
        return Counter(self.creatures)


def compete(s1, s2):
    def rand():
        return random.randint(0, 1)

    if s1 == "dove":
        if s2 == "dove":
            return (1, 1)
        elif s2 == "hawk":
            return (rand(), 1+rand())

    elif s1 == "hawk":
        if s2 == "dove":
            return (1+rand(), rand())
        elif s2 == "hawk":
            return (0, 0)


def assign_to_food(creatures):
    shuffled = creatures[:]
    random.shuffle(shuffled)
    spots = []

    i = 0
    for _ in range(FOOD):
        if i >= len(shuffled):
            break  # no more creatures to assign
        # 50% chance this spot has 2 animals, else 1
        if i + 1 < len(shuffled) and random.random() < 0.5:
            spots.append([shuffled[i], shuffled[i + 1]])
            i += 2
        else:
            spots.append([shuffled[i]])
            i += 1

    # Remaining creatures did not get food; they "die" (ignored in contests)
    return spots

