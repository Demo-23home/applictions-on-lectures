
from tkinter import N
from turtle import goto


class Game:
    def __init__(self):
        while True:
            print('''
        --- Welcome Pick One Of Our Games...---
            1:sentence remove duplicates
            2:multiplication table
            3:divided by numbers
            4:to Exit
            ''')
            userChoice=int(input("enter your choice : "))
            if userChoice==4:
                print("goodBye")
                break 
            elif userChoice==1:
                self.SentenceRemoveDublicates()
            elif userChoice==2:
                self.multiplicationTable()
            elif userChoice==3:
                self.dividedByNumbers()
            else:
                print('invalid input !!!')
            play_again=input('press y to play agian and n to exit: ')
            if play_again=='n':
                break
       
    def SentenceRemoveDublicates(self):
        sentence=input("enter the sentence : ")
        new_sentence=sentence.split(' ')
        mySentence=[]
        for word in new_sentence:
            if word in mySentence:
                continue
            else:
                mySentence.append(word)
        final_Sentence=' '.join(mySentence)
        print(final_Sentence)

    def multiplicationTable(self):
        x=int(input("plz enter first number: "))
        y=int(input("plz enter second number: "))
        for i in range(x,y+1):
            for j in range(1,13):
                print(f'{i}X{j}={i*j}')
            print("---------------------")

    def dividedByNumbers(self):
        x=int(input('plz enter first number: '))
        y=int(input('plz enter second number: '))
        for i in range(101):
            if i%y==0 and i%x==0:
                print(i)
    
#g1=Game()






# new_nummbers=[]
# numbers=[1,2,3,4,5,6,7]
# for i in numbers:
#     new_numbers.append(i**3)
# new_numbers2=[number**3 for number in numbers]
# new_numbers2

# numbers=range(1,101)
# even =[number for number in numbers if number%2==0]
# even 


def SentenceRemoveDublicates():
        sentence=input("enter the sentence : ")
        new_sentence=sentence.split(' ')
        mySentence=[]
        mySentence=[word for word in new_sentence if word not in mySentence]
        print(mySentence)
        final_Sentence=' '.join(mySentence)
        print(final_Sentence)
#SentenceRemoveDublicates()



def multiplicationTable():
    x=int(input("plz enter first number: "))
    y=int(input("plz enter second number: "))
    mul=[print(f'{i}X{j}={i*j}') for i in range(x,y+1) for j in range(1,13) ]
    
#multiplicationTable()

def dividedByNumbers():
    x=int(input('plz enter first number: '))
    y=int(input('plz enter second number: '))
    result=[i for i in range(101) if i%y==0 and i%x==0]
    print(result)
#dividedByNumbers()
        
        
