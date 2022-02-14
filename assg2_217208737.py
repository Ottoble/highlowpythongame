points = 100

def getCardValue():
    card = 0

def getCardStr(cardValue):
    card = cardValue   

def getHLGuess():
    guess = input();

def getBetAmount(maximum):
    bet = input()
    if bet > maximum:
        print("You don't have that much")

def playerGuessCorrect(card1, card2, betType):
    if card1 > card2:
        return True