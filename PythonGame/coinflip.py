from lib2to3.pytree import _Results
import random\

from unittest import result
def coin_flip():
    return random.choice(["heads", "tails"])

def say_hello(name):
    print("hello" + name)
    
def multi_flip(num):
    h=0
    t=0
    while num>0:
    
        if(coin_flip()=="heads"):
            h=h+1
        else:
            t=t+1
        num= num-1

    print("You flipped "+str(h)+" heads and "+str(t)+" tails")
    print("precentage of heads:" + str(100 * h/num)+ "%")
    print("Percentage of Tails:" + str(100 * t/num)+ "%")

    def predict():
        preditcion = input("Do you think the coin will flip Heads or Tails?")
        result = coin_flip()
        if (preditcion == result):
            print("You were right! The coin flipped " + result)
        else:
            print("You were wrong :( the coin fipped " + result)

def predict():
    num_guesses = 0
    while True:
        prediction = input("Do you think the coin flip Heads or Tails?")
        result = coin_flip()
        if (prediction == result):
            print("You were right! The coin flipped" + result)
            num_guesses = num_guesses + 1
        else:
            print("You were wrong :( The coin flipped " + result)
            break
        print("You guessed right" + str(num_guesses) + " times")

            