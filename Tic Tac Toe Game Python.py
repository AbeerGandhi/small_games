#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def printBoard(xstate, zstate):
    zero = 'X' if xstate[0] else ('0' if zstate[0] else 0)
    one = 'X' if xstate[1] else ('0' if zstate[1] else 1)
    two = 'X' if xstate[2] else ('0' if zstate[2] else 2)
    three = 'X' if xstate[3] else ('0' if zstate[3] else 3)
    four = 'X' if xstate[4] else ('0' if zstate[4] else 4)
    five = 'X' if xstate[5] else ('0' if zstate[5] else 5) 
    six = 'X' if xstate[6] else ('0' if zstate[6] else 6)
    seven= 'X' if xstate[7] else ('0' if zstate[7] else 7)
    eight= 'X' if xstate[8] else ('0' if zstate[8] else 8)
    print(f"{zero} | {one} | {two}")
    print("--|---|--")
    print(f"{three} | {four} | {five}")
    print("--|---|--")
    print(f"{six} | {seven} | {eight}")
    print("--|---|--")
def checkWin(xstate, zstate):
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if(sum(xstate[win[0]], xstate[win[1]], xstate[win[2]]) == 3):
            print("X wins !")
            return 1

        if(sum(zstate[win[0]], zstate[win[1]], zstate[win[2]]) == 3):
            print("O wins !")
            return 0
    return -1

def sum(a, b ,c):
    return a+b+c

if __name__ == "__main__":
    xstate = [0,0,0,0,0,0,0,0,0]
    zstate = [0,0,0,0,0,0,0,0,0]
    turn = 1 
    #1 = x,0 = O
    selected_numbers = set()  # To keep track of selected numbers
    while(True):
        printBoard(xstate , zstate)
        if(turn == 1):
            print("X Turn ")
            space = int(input("Enter the number:"))
            if space in selected_numbers:
                print("Invalid move! Number already selected.")
                continue
            xstate[space] = 1
            selected_numbers.add(space)
            print("--------------------")
        else:
            print("O Turn ")
            space = int(input("Enter the number:"))
            if space in selected_numbers:
                print("Invalid move! Number already selected.")
                break
            zstate[space] = 1
            selected_numbers.add(space)
            print("--------------------")
        win = checkWin(xstate, zstate)
        
        if(win != -1):
            print("Game Over")
            break
            
        turn = 1-turn


# In[ ]:




