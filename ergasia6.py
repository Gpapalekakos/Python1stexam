import random

def main():
    print("Give me the length of sideA:\n")
    sideA=input('')
    print("Give me the length of sideB:\n")
    sideB=input('')
    print("Give me the number of the mines:\n")
    mines=input('')
    tablerow=["    "]*sideA
    board=[]
    mines+=1
    for i in range(sideB):
        board.append(tablerow)
    for i in range(len(board)):
        if mines!=0:
            nummines=random.randint(0,mines)
            mines-=nummines
            for i in range(nummines):
                board[i].remove(tablerow[i])
                board[i].append("bomb")
                random.shuffle(board[i])
                i+=1
        else:
            i+=1
    for i in range(len(board)):
        print(board[i])
        #################
#h askhsh einai hmitelhs 
########################
main()
