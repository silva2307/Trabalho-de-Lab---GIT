import os
import random

decks = input("\033[1;35;40mIntroduz o número de baralhos a usar \033[1;37;40m↓\n\033[1;36;40m[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] \033[1;37;40m: ")

# o utilizador escolhe o número de baralhos a usar
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*(int(decks)*4)

# inicialização da pontuação
wins = 0
losses = 0

def deal(deck):
    hand = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        if card == 11:card = "J"
        if card == 12:card = "Q"
        if card == 13:card = "K"
        if card == 14:card = "A"
        hand.append(card)
    return hand

def play_again():
    again = input("Queres jogar novamente? [Sim / Não] (S/N) : ").lower()
    if again == "s":
        dealer_hand = []
        player_hand = []
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
        game()
    else:
        print("Adeus!")
        exit()

def total(hand):
    total = 0
    for card in hand:
        if card == "J" or card == "Q" or card == "K":
            total+= 10
        elif card == "A":
            if total >= 11: total+= 1
            else: total+= 11
        else: total += card
    return total

def hit(hand):
    card = deck.pop()
    if card == 11:card = "J"
    if card == 12:card = "Q"
    if card == 13:card = "K"
    if card == 14:card = "A"
    hand.append(card)
    return hand

def clear():
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')

def print_results(dealer_hand, player_hand):
    clear()

    print("\n    \033[1;34;40mBEM-VINDO AO BLACKJACK!\n")
    print("\033[1;33;40m-"*30+"\n")
    print("    \033[1;32;40mVITÓRIAS: \033[1;37;40m%s    \033[1;31;40mDERROTAS: \033[1;37;40m%s\n" % (wins, losses))
    print("\033[1;33;40m-"*30+"\n\033[1;37;40m")
    print ("O Dealer está a mostrar " + str(dealer_hand) + " ou seja, ele tem o total de " + str(total(dealer_hand)))
    print ("Tu tens " + str(player_hand) + " ou seja, tens o total de " + str(total(player_hand)))

def blackjack(dealer_hand, player_hand):
    global wins
    global losses
    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        print ("Parabéns! Tens Blackjack!\n")
        wins += 1
        play_again()
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)
        print ("Desculpa, perdeste... O Dealer tem Blackjack.\n")
        losses += 1
        play_again()

def score(dealer_hand, player_hand):
        # Função que vai atualizar a pontuação das vitorias/derrotas
        global wins
        global losses
        if total(player_hand) == 21:
            print_results(dealer_hand, player_hand)
            print ("Parabéns! Tens Blackjack!\n")
            wins += 1
        elif total(dealer_hand) == 21:
            print_results(dealer_hand, player_hand)
            print ("Desculpa, perdeste... O Dealer tem Blackjack.\n")
            losses += 1
        elif total(player_hand) > 21:
            print_results(dealer_hand, player_hand)
            print ("Desculpa 'arrebentaste'. Tu perdeste...\n")
            losses += 1
        elif total(dealer_hand) > 21:
            print_results(dealer_hand, player_hand)
            print ("O Dealer 'arrebentou'. Tu ganhaste!\n")
            wins += 1
        elif total(player_hand) < total(dealer_hand):
            print_results(dealer_hand, player_hand)
            print ("Desculpa. A tua pontuação não é maior que a do Dealer. Tu perdeste...\n")
            losses += 1
        elif total(player_hand) > total(dealer_hand):
            print_results(dealer_hand, player_hand)
            print ("Parabéns. A tua pontuação é maior que a do Dealer. Tu ganhaste\n")
            wins += 1
        elif total(player_hand) == total(dealer_hand):
            print_results(dealer_hand, player_hand)
            print ("Temos um empate!\n")
            wins += 0

def game():
    global wins
    global losses
    choice = 0
    clear()
    print("\n    \033[1;34;40mBEM-VINDO AO BLACKJACK!\n")
    print("\033[1;33;40m-"*30+"\n")
    print("    \033[1;32;40mVITÓRIAS:  \033[1;37;40m%s   \033[1;31;40mDERROTAS:  \033[1;37;40m%s\n" % (wins, losses))
    print("\033[1;33;40m-"*30+"\n\033[1;37;40m")
    dealer_hand = deal(deck)
    player_hand = deal(deck)
    print ("O Dealer está a mostrar " + str(dealer_hand[0]))
    print ("Tu tens " + str(player_hand) + " ou seja, tens o total de " + str(total(player_hand)))
    blackjack(dealer_hand, player_hand)
    quit=False
    while not quit:
        choice = input("Queres [P]edir, [F]icar, ou [S]air: ").lower()
        if choice == 'p':
            hit(player_hand)
            print(player_hand)
            print("Total: " + str(total(player_hand)))
            if total(player_hand)>21:
                print("Desculpa 'arrebentaste'. Tu perdeste...\n")
                losses += 1
                play_again()
        elif choice=='f':
            while total(dealer_hand)<17:
                hit(dealer_hand)
                print(dealer_hand)
                if total(dealer_hand)>21:
                    print("O Dealer 'arrebentou'. Tu ganhaste!\n")
                    wins += 1
                    play_again()
            score(dealer_hand,player_hand)
            play_again()
        elif choice == "s":
            print("Adeus!")
            quit=True
            exit()


if __name__ == "__main__":
   game()
