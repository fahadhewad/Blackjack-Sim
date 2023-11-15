import random

deck = []
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['S', 'C', 'H', 'D']
tens = ['J', 'Q', 'K']
def deckMake(): 
    for card in cards:
        for suit in suits:
            x = card + "-" + suit
            deck.append(x)

for i in range(3): # 3 decks made
    deckMake()


random.shuffle(deck)

dealer = []
user = []

def deal():
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
    player.append(deck.pop())

def reset():
    dealer.clear()
    user.clear()

def checkWinner():
    dealerCount = count(dealer)
    userCount = count(user)
    print(dealer, " = ", dealerCount, " = Dealer")
    print(user, " = ", userCount, " = Player")
    print("---------------")
    tempCount = count(dealer)
    while tempCount < 17:
        hitPerson(dealer)
        dealerCount = count(dealer)
        userCount = count(user)
        print(dealer, " = ", dealerCount, " = Dealer")
        print(user, " = ", userCount, " = Player")
        print("---------------")
        if count(dealer) > 21:
            print("User wins!")
            return
    
    dealerFinal = count(dealer)
    userFinal = count(user)
    if userFinal > dealerFinal:
        print("User wins!")
    elif userFinal == dealerFinal:
        print("Push!")
    else:
        print("Dealer wins!")
    reset()

def start():
    deal()
    while True:
        print("----------------------------------------------------------------------")
        tempArray = [dealer[0], dealer[1]]
        bjDealer = count(tempArray) == 21
        tempArray = [user[0], user[1]]
        bjUser = count(tempArray) == 21

        if bjUser and not bjDealer:
            dealerCount = count(dealer)
            userCount = count(user)
            print(dealer, " = ", dealerCount, " = Dealer")
            print(user, " = ", userCount, " = Player")
            print("---------------")
            print("User wins! - BlackJack")
            reset()
            deal()
            continue

        if bjUser and bjDealer:
            dealerCount = count(dealer)
            userCount = count(user)
            print(dealer, " = ", dealerCount, " = Dealer")
            print(user, " = ", userCount, " = Player")
            print("---------------")
            print("Push! - BlackJack")
            reset()
            deal()
            continue

        temp = [dealer[0]]
        print(temp)
        tempArr = []
        tempArr.append(dealer[0])
        print("Dealer = " + str(count(tempArr)))
        print(user)
        print("Player = " + str(count(user)))
        if count(user) > 21:
            print("----------------------------------------------------------------------")
            print(dealer)
            print("Dealer = " + str(count(dealer)))
            print(user)
            print("Player = " + str(count(user)))
            print("Dealer wins! - Bust")
            reset()
            deal()
            continue

        userInput = int(input("1 = Hit, 0 = Stand\n"))
        if userInput == 1:
            hitPerson(user)
        elif userInput == 0:
            print("----------------------------------------------------------------------")
            checkWinner()
            reset()
            deal()
            continue
    
start()