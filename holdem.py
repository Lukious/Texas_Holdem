# -*- coding: utf-8 -*-

#Toy project [Texas holdom][Reinforcement Poker EnV]

#@author: lukious


import numpy as np
from random import *
from collections import Counter
import operator

global bet
global fold
bet = []
fold = [0,0,0,0]

def betting (player):
    i_bet = []
    for i in range(player):
        if fold[i] != 1:
            bet_cost = input("player"+str(i+1)+" bet : ")
            bet.append(bet_cost)
            if bet_cost == '0':
                fold[i] = 1
        else: print("player"+str(i+1) +"is fold.\n")
    i_bet = list(map(int, bet))
    bet_total = sum(i_bet)
    print("\nTotal bet is : " + str(bet_total) + "\n")

def findbest(player_all_card):
    best_set = 0
    handle=[]
    print(player_all_card)
    for cnt in range(7):
        handle.append(player_all_card[cnt])
    #우선 5개 뽑아
    count = 6
    j = 1
    #test_counter = 0
    for i in range(6):
        for j in range(count):
            j = j+1
            #print("chek1 : "+str(handle[i]))
            #print("chek2 : "+str(handle[i+j]))
            #print (str(test_counter))
            #test_counter = test_counter + 1
            del handle [i]
            del handle [i+(j-1)]
            #print (str(handle))
            newhigh = rank(handle)
            if newhigh>=best_set:
                best_set=newhigh
            #print (str(best_set))
            handle=[]
            cnt = 0
            for cnt in range(7):
                handle.append(player_all_card[cnt])
        count = count -1
    return best_set
    
def rank(hand):
    #check pair
    cardnum = []
    cardshape = []
    for i in range(5):
        process=str(hand[i])
        #print(process)
        cardnum.append(int(process[0:2]))
        cardshape.append(process[2:3])
        #print(str(cardnum[i]))
        #print(str(cardshape[i]))
    cardnum.sort()
    num_result = Counter(cardnum).values()
    shape_result = Counter(cardshape).values()
    #print(str(num_result))
    pair_cnt = 0
    threecard_flag = 0
    fourcard_flag = 0
    if 2 in num_result:
        pair_cnt = pair_cnt +1
    if 3 in num_result:
        threecard_flag = 1
    if 4 in num_result:
        fourcard_flag = 1
    
    straight_cnt = 0
    straight_flag = 0
    flush_flag = 0
    
    for i in range(4):
        if cardnum[i] == (cardnum[i+1]-1):
            straight_cnt = straight_cnt + 1
    if straight_cnt == 4:
        straight_flag = 1
    
    if 5 in shape_result:
        flush_flag = 1
    
    high_rank = 0
    
    if fourcard_flag == 1:
        high_rank = 8
    elif threecard_flag == 1 and pair_cnt == 1:
        high_rank = 7
    elif flush_flag == 1:
        high_rank = 6
    elif straight_flag == 1:
        high_rank = 5
    elif threecard_flag == 1:
        high_rank = 4
    elif pair_cnt == 2:
        high_rank = 3
    elif pair_cnt == 1:
        high_rank = 2
    else:
        high_rank = 1
    
    # 4 card 8
    # full house 7
    #flush 6
    #straight 5
    #triple 4
    #2pair 3
    #1pair 2
    #highcard 1
    return high_rank
    

print ("POKER")

RANKS = np.array(["02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14"])
SUITS = np.array(["H","D","S","C"])

#11 as J
#12 as Q
#13 as K
#14 as A

w = 4
h = 13

deck = [[0 for x in range(w)] for y in range(h)] 
for i in range(13):
    for j in range(4):
        deck[i][j] = RANKS[i] + SUITS[j]
    
player = 4
seq = 0
used_list = []
first_two = []
open_three = []
s1_onemore = []
s2_onemore = []
player_all_card = []
trans = []

player_pocket = [["init","init"],["init","init"],["init","init"],["init","init"]]

player_card= np.zeros((player, 2), dtype='S3')

for i in range(player*2):
     rand_a = randint(0,12)
     rand_b = randint(0,3)
     card = deck[rand_a][rand_b]
     while card == "sold":
         rand_a = randint(0,12)
         rand_b = randint(0,3)
         card = deck[rand_a][rand_b]
     deck[rand_a][rand_b] = "sold"
     first_two.append(card)
     #used_list.append(card)

for i in range(player):
    player_pocket[i][0] = first_two[seq]
    seq=seq+1
    player_pocket[i][1] = first_two[seq]
    seq=seq+1
    
for p in range(player):
    print("Player"+str(p)+"'s card : " + str(player_pocket[p][0]) + " "+ str(player_pocket[p][1]))
    
betting(player)


# 나중에 뽑기 함수화 시켜서 정리------------------------여기부터


for i in range(3):
    rand_a = randint(0,12)
    rand_b = randint(0,3)
    card = deck[rand_a][rand_b]
    while card == "sold":
        rand_a = randint(0,12)
        rand_b = randint(0,3)
        card = deck[rand_a][rand_b]
    deck[rand_a][rand_b] = "sold"
    open_three.append(card)
    
#show open three
print(open_three)
#betting(player)

rand_a = randint(0,12)
rand_b = randint(0,3)
card = deck[rand_a][rand_b]
while card == "sold":
    rand_a = randint(0,12)
    rand_b = randint(0,3)
    card = deck[rand_a][rand_b]
deck[rand_a][rand_b] = "sold"

s1_onemore.append(card)
open_three.append(card)

#show one more
print(open_three)
#betting(player)

rand_a = randint(0,12)
rand_b = randint(0,3)
card = deck[rand_a][rand_b]
while card == "sold":
    rand_a = randint(0,12)
    rand_b = randint(0,3)
    card = deck[rand_a][rand_b]
deck[rand_a][rand_b] = "sold"

s2_onemore.append(card)
open_three.append(card)

#show last
print(open_three)
#betting(player)

# 나중에 뽑기 함수화 시켜서 정리------------------------여기까지

card_result = []

for i in range(4):
    if fold[i] != 1:
        for j in range(5):
            player_all_card.append(open_three[j])
        player_all_card.append(player_pocket[i][0])
        player_all_card.append(player_pocket[i][1])
        card_result.append(findbest(player_all_card))
        player_all_card = []
        
    else: 
        print("player"+str(i+1) +"is fold.")
        card_result.append(0)

for r in range(player):
    if card_result[r] == 8:
        print("player"+str(r+1)+" is Fourcard")
    elif card_result[r] == 7:
        print("player"+str(r+1)+" is Full house")
    elif card_result[r] == 6:
        print("player"+str(r+1)+" is Flush")
    elif card_result[r] == 5:
        print("player"+str(r+1)+" is Straight")
    elif card_result[r] == 4:
        print("player"+str(r+1)+" is Triple")
    elif card_result[r] == 3:
        print("player"+str(r+1)+" is 2pair")
    elif card_result[r] == 2:
        print("player"+str(r+1)+" is 1pair")
    elif card_result[r] == 1:
        print("player"+str(r+1)+" is Nopair")
    elif card_result[r] == 0:
        print("player"+str(r+1)+" is folded")
draw_checker = Counter(card_result).values()

index, value = max(enumerate(card_result), key=operator.itemgetter(1))
if card_result.count(value) != 1:
    print("draw")
else:
    print("Player "+str(index+1)+ " " + "is winner")
        
        
        
        
        
        
        
        
        
        
        