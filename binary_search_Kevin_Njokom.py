#Author: Kevin Tah Njokom
#Binary search
#Complexity Calculation: N ,  N/2  , N/4 , N/8   ---->    N /2^2  thus O(ln N)   time complexity
#Space complexity is constant
#Cards are arranged in descending order
#Find a card (query) in as few steps as possible
#Implement a test case
import math



def find_card(cards,query):
    ending      = len(cards)
    starting    = 0
    position    = math.floor((ending - starting)/2)
    
    while cards[position] != query:
        if cards[position] == query:
            print(position)
        elif cards[position] > query:
            starting  = position
            ending = len(cards)
            position = math.ceil((ending - starting)/2)
        elif cards[position] < query:
             ending      = position
             starting    = 0
             position    = math.ceil((ending - starting)/2)
    print(position)

test = {
     'input':{'cards':[19,12,9,7,6,5,4,3,2,1], 'query':7
      },
      'output': 3
}

find_card(test['input']['cards'], test['input']['query'])