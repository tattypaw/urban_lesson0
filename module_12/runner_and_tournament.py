class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers
"""all_results = {}
runner1 = Runner('Usane', 10)
runner2 = Runner('Andrew', 9)
runner3 = Runner('Nick', 3)

tour = Tournament(90, runner1, runner2, runner3)
result = tour.start()
print (all_results)
all_results[len(all_results)] = result
print (all_results)"""
#self.assertTrue(TournamentTest.runners[2], 'Nick')
