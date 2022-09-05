import random as r
#from tkinter.tix import DirSelectDialog

n=int(input("Enter a number of Tickets"))
tickets=[]
temp=0
num=[0,1,2,3,4,5,6,7,8]

for i in range(n):
    if i%6==0:
        numbers=[[90,1,2,3,4,5,6,7,8,9],[10,11,12,13,14,15,16,17,18,19],[20,21,22,23,24,25,26,27,28,29],[30,31,32,33,34,35,36,37,38,39],[40,41,42,43,44,45,46,47,48,49],[50,51,52,53,54,55,56,57,58,59],[60,61,62,63,64,65,66,67,68,69],[70,71,72,73,74,75,76,77,78,79],[80,81,82,83,84,85,86,87,88,89]]
    a=[]
    line=[]
    for j in range(15):
        if temp%9==0:
            num=[0,1,2,3,4,5,6,7,8]
        temp=temp+1
        if j==10 or j==5 or j==0:
            line=[]
        k = num.pop(r.randint(0, len(num)-1))
        if (k in line):
            q=k
            k = num.pop(r.randint(0, len(num) - 1))
            num.append(q)
            line.append(k)
        m=r.randint(0,len(numbers[k])-1)
        a.append(numbers[k].pop(m))
        tickets.append(a)

   # print(tickets)

for i in range(n):
    print("--------Ticket:->", i+1)

ticket=[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]

row=0

for j in range(15):
    if(j==5):
        row=1
    if(j==10):
        row=2
    col=int(tickets[i][j]/10)
    if col==9:
        col=8
    ticket[row][col]=tickets[i][j]

    for a in range(3):
        for b in range(9):
            if(ticket[a][b]==0):
                print(" ",end=' ')
            else:
                if (ticket[a][b]<10):
                    print(ticket[a][b],end='  ')
                else:
                    print(ticket[a][b],end=' ')
print()
