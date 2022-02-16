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
    elif card1 < card2 and betType == "HIGH":
        return True
    elif card1 == card2:
        return False

def printLn():
    print("-" * 50)

def playGame():
    gameOver = False
    round = 1

    while(not gameOver):
        card1 = getCardValue()
        card2 = getCardValue()
        print("First card is a[" + getCardStr(card1) + "]")
        guess = getHLGuess()
        bet = getBetAmount(points)
        print("Second card is a [" + card2 + "]")
        cardsStr = "Card 1:[" + getCardStr(card1) + "], Card 2: [" + getCardStr(card2) + "]" \
            "You bet '" + guess + "' for " + bet + " -" 
        if(playerGuessCorrect(card1,card2,guess)):
            cardsStr = cardsStr + "YOU WIN"
            points = points + bet
        else:
            cardStr = cardsStr + "YOU LOSE"
            
        print(cardsStr)
        printLn()
        round = round + 1
    return False

print("--- Welcome to High-Low ---\n" \
    "Start with 100 points. Each round a card will be drawn and shown.\n" \
    "Select whether you think the 2nd card will be Higher or Lower than the 1st card.\n" \
    "Then enter the amount you want to bet.\n"\
    "If you are right, you win the amount you bet, otherwise you lose.\n"\
    "Try to make it to 500 points within 10 tries.")
printLn()
playGame()
