ALL_BALLS_IN_FRAME = 10
NUMBER_OF_FRAMES_IN_GAME = 10

class Bowling:
    def __init__(self):
        self.pins = []

    def roll(self, pins):
        self.pins.append(pins)

    def isSpare(self, first_in_frame):
        return self.pins[first_in_frame] + self.pins[first_in_frame + 1] == ALL_BALLS_IN_FRAME

    def isStrike(self, first_in_frame):
        return self.pins[first_in_frame] == ALL_BALLS_IN_FRAME

    def scroreForPinsInFrame(self, first_in_frame):
        return self.pins[first_in_frame] + self.pins[first_in_frame + 1]

    def scroeForSpareOfFrame(self, first_in_frame):
        return 10 + self.pins[first_in_frame + 2]

    def scoreForStrike(self, first_in_frame):
        return 10 + self.pins[first_in_frame + 1] + self.pins[first_in_frame + 2]

    def score(self):
        game_score = 0
        first_in_frame = 0

        for x in range(NUMBER_OF_FRAMES_IN_GAME):
            if (self.isStrike(first_in_frame)):
                game_score += self.scoreForStrike(first_in_frame)
                first_in_frame += 1
            elif (self.isSpare(first_in_frame)):
                game_score += self.scroeForSpareOfFrame(first_in_frame)
                first_in_frame += 2
            else:
                game_score += self.scroreForPinsInFrame(first_in_frame)
                first_in_frame += 2

        return game_score

