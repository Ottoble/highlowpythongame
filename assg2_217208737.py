import random

points = 100

def getCardValue():
    card = random.randint(2,14)
    return card

def getCardStr(cardValue):
    if cardValue < 10:
        return str(cardValue)
    elif cardValue == 10:
        return "T"
    elif cardValue == 11:
        return "J"
    elif cardValue == 12:
        return "Q"
    elif cardValue == 13:
        return "K"
    elif cardValue == 14:
        return "A"

def getHLGuess():
    guess = input("High or Low (H/L)?:");
    
    while(guess != "l" and guess != "L" and guess != "h" and guess != "H"):
        guess = input("Incorrect input. Please guess High or Low (H/L)?:");

    guess = guess.lower()
    
    if guess == "l":
        return "LOW"
    elif guess == "h":
        return "HIGH"

def getBetAmount(maximum):
    bet = int(input("Input bet amount: "))
    
    while(bet > maximum or bet <= 0):
        bet = int(input("Input bet amount: "))
    return bet

def playerGuessCorrect(card1, card2, betType):
    if card1 > card2 and betType == "LOW":
        return True
    elif card1 > card2 and betType == "HIGH":
        return False
    elif card1 < card2 and betType == "LOW":
        return False
    elif card1 < card2 and betType == "HIGH"
        return True
    elif card1 == card2
        return False
