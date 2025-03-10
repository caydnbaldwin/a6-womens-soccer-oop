# Caydn Baldwin
# IS 303 | Section 4
# A6 - Women's Soccer OOP 1
# Displays information about a soccer team utilizing OOP and loosely implementing inheritance

class Team:
    # Initializes Team object by getting team name and number of games. Then initializes schedule, wins, losses, and evaluation string
    def __init__(self):
        self.teamName = "BYU"
        self.wins = 5
        self.losses = 4
        self.goalsScored = 10
        self.goalsAllowed = 8

    def seasonStatus(self):
        # return the correct message based on the win/loss record, whatever is returned will be printed externally
        win_percentage = self.wins / (self.wins + self.losses)
        if win_percentage >= 0.75:
            return "Qualified for the NCAA Women's Soccer Tournament"
        elif win_percentage >= 0.5:
            return "You had a good season."
        else:
            return "Your team needs to practice!"

# create season, iterate through games, evaluate season, print results
if __name__ == '__main__':
    byu = Team()
    print(byu.seasonStatus())