import random

deck = []
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['S', 'C', 'H', 'D']
tens = ['J', 'Q', 'K']
userWinCount = 0
dealerWinCount = 0
userBJCount = 0
dealerBJCount = 0
insuranceWinCount = [0, 0]

def deckMake(): 
    for card in cards:
        for suit in suits:
            x = card + "-" + suit
            deck.append(x)

def dealDeck(n):
    for i in range(n):
        deckMake()
    random.shuffle(deck)
    
dealDeck(2) # 3 decks made

random.shuffle(deck)

dealer = []
user = []

def reshuffle():
    print("--------------------------")
    print("Deck out of cards!")
    userInput = int(input("Type the number of decks you want shuffled in. 0 to Exit.\n"))
    if userInput == 0:
        exit()
    else:
        deck.clear()
        dealDeck(userInput)
        print("Shuffled " + str(userInput) + " decks.")

def deal():
    if len(deck) < 4:
        deck.clear()
        reshuffle()
        
    user.append(deck.pop())
    dealer.append(deck.pop())
    user.append(deck.pop())
    dealer.append(deck.pop())     
        
def count(player):
    count = 0
    number = 0


    for card in player:
        arr = card.split('-')
        if arr[0] in tens:
            number = 10
            count += number
        elif arr[0] == 'A':
            if count + 11 > 21:
                count += 1
            else:
                count += 11 # need work
        else:
            count +=  int(arr[0])

    return count

def hitPerson(player):
    try:
        player.append(deck.pop())
    except:
        reshuffle()
        player.append(deck.pop())

def reset():
    dealer.clear()
    user.clear()

def checkWinner():
    global userWinCount, dealerWinCount, userBJCount, dealerBJCount

    dealerCount = count(dealer)
    userCount = count(user)
    print(dealer, " = ", dealerCount, " = Dealer")
    print(user, " = ", userCount, " = Player")
    print("---------------")
    while count(dealer) < 17:
        hitPerson(dealer)
        dealerCount = count(dealer)
        userCount = count(user)
        print(dealer, " = ", dealerCount, " = Dealer")
        print(user, " = ", userCount, " = Player")
        print("---------------")
        if count(dealer) > 21:
            print("User wins!")
            userWinCount += 1
            return
    
    dealerFinal = count(dealer)
    userFinal = count(user)
    if userFinal > dealerFinal:
        userWinCount += 1
        print("User wins!")
    elif userFinal == dealerFinal:
        print("Push!")
    else:
        dealerWinCount += 1
        print("!")
    reset()

def start():
    global userWinCount, dealerWinCount, userBJCount, dealerBJCount

    deal()
    while True:
        print("----------------------------------------------------------------------")
        tempArray = [dealer[0], dealer[1]]
        bjDealer = count(tempArray) == 21
        tempArray = [user[0], user[1]]
        bjUser = count(tempArray) == 21

        if bjUser and not bjDealer:
            userBJCount += 1
            userWinCount += 1
            dealerCount = count(dealer)
            userCount = count(user)
            print(dealer, " = ", dealerCount, " = Dealer")
            print(user, " = ", userCount, " = Player")
            print("---------------")
            print("User wins! - BlackJack")
            print("Player wins = " + str(userWinCount) + " | Dealer wins = " + str(dealerWinCount))
            print("Player blackjacks = " + str(userBJCount) + " | Dealer blackjacks = " + str(dealerBJCount))
            print("Insurance wins and losses w/l " + str(insuranceWinCount[0]) + "|" + str(insuranceWinCount[1]))
            reset()
            deal()
            continue

        if bjUser and bjDealer:
            userBJCount += 1
            dealerBJCount += 1
            dealerCount = count(dealer)
            userCount = count(user)
            print(dealer, " = ", dealerCount, " = Dealer")
            print(user, " = ", userCount, " = Player")
            print("---------------")
            print("Push! - BlackJack")
            print("Player wins = " + str(userWinCount) + " | Dealer wins = " + str(dealerWinCount))
            print("Player blackjacks = " + str(userBJCount) + " | Dealer blackjacks = " + str(dealerBJCount))
            print("Insurance wins and losses w/l " + str(insuranceWinCount[0]) + "|" + str(insuranceWinCount[1]))
            reset()
            deal()
            continue

        firstCard = [dealer[0]]
        print(firstCard)
        firstCardCount = []
        firstCardCount.append(dealer[0])
        print("Dealer = " + str(count(firstCardCount)))
        print(user)
        print("Player = " + str(count(user)))
        if dealer[0][0] == 'A':
            userInput = int(input("Would you like insurance? 1 = Yes, 0 = No\n"))
            if userInput == 1:
                if dealer[1] in tens:
                    insuranceWinCount[0] += 1
                else:
                    insuranceWinCount[1] += 1
            if userInput == 0:
                pass
            
            if bjDealer: # needs work when dealer gets A A A K, MAKES HIM GO BUST, ALSO FIX THE WIN COUNTS
                dealerWinCount += 1
                dealerBJCount += 1
                dealerCount = count(dealer)
                userCount = count(user)
                print(dealer, " = ", dealerCount, " = Dealer")
                print(user, " = ", userCount, " = Player")
                print("---------------")
                print("Dealer wins! - Blackjack")
                print("Player wins = " + str(userWinCount) + " | Dealer wins = " + str(dealerWinCount))
                print("Player blackjacks = " + str(userBJCount) + " | Dealer blackjacks = " + str(dealerBJCount))
                print("Insurance wins and losses w/l " + str(insuranceWinCount[0]) + "|" + str(insuranceWinCount[1]))
                reset()
                deal()
                continue

        if count(user) > 21:
            print("----------------------------------------------------------------------")
            print(dealer)
            print("Dealer = " + str(count(dealer)))
            print(user)
            print("Player = " + str(count(user)))
            print("Dealer wins! - Bust")
            reset()
            deal()
            print("Player wins = " + str(userWinCount) + " | Dealer wins = " + str(dealerWinCount))
            print("Player blackjacks = " + str(userBJCount) + " | Dealer blackjacks = " + str(dealerBJCount))
            print("Insurance wins and losses w/l " + str(insuranceWinCount[0]) + "|" + str(insuranceWinCount[1]))
            continue

        userInput = int(input("1 = Hit, 0 = Stand\n"))
        if userInput == 1:
            hitPerson(user)
        elif userInput == 0:
            print("----------------------------------------------------------------------")
            checkWinner()
            reset()
            deal()
            print("Player wins = " + str(userWinCount) + " | Dealer wins = " + str(dealerWinCount))
            print("Player blackjacks = " + str(userBJCount) + " | Dealer blackjacks = " + str(dealerBJCount))
            print("Insurance wins and losses w/l " + str(insuranceWinCount[0]) + "|" + str(insuranceWinCount[1]))
            continue
    
start()