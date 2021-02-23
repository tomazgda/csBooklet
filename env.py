#!/usr/bin/env python3


import random

usrScore = 0
comScore = 0
GameEnd = False

choices = ["R", "P", "S"]

def rock():
   print("""
      _______
   ---'   ____)
         (_____)
         (_____)
         (____)
   ---.__(___)
  """)

def paper():
   print("""
        _______
  ---'      ____)____
               ______)
             _______)
            _______)
  ---.__________)
  """)

def scissors():
   print("""
       _______
   ---'   ____)____
            ______)
         __________)
         (____)
   ---.__(___)
  """)



def rAs():
   rock()
   scissors()

def rAp():
   rock()
   paper()

def rAr():
   rock()
   rock()

def pAr():
   paper()
   rock()

def pAp():
   paper()
   paper()

def pAs():
   paper()
   scissors()

def sAr():
   scissors()
   rock()
def sAp():
    scissors()
    paper()

def sAs():
   scissors()
   scissors()

while GameEnd == False:

  if comScore >= 5:
   print("com win")
   GameEnd = True
  elif usrScore >= 5:
   print("usr win")
   GameEnd = True
  else:
    usrInput = input("Rock, Paper, Scissors : R, P, S")
    comInput = random.choice(choices)
    print(comInput)
    if usrInput == "R" and comInput == "R":
      rAr()
      print("draw")
    elif usrInput == "R" and comInput == "P":
      rAp()
      print("player loose")
      comScore += 1
    elif usrInput == "R" and comInput == "S":
      rAs()
      print("player win")
      usrScore += 1
    elif usrInput == "P" and comInput == "R":
      pAr()
      print("player win")
      usrScore += 1
    elif usrInput == "P" and comInput == "P":
      pAp()
      print("draw")
    elif usrInput == "P" and comInput == "S":
      pAs()
      print("player loose")
      comScore += 1
    elif usrInput == "S" and comInput == "R":
      sAr()
      print("player loose")
      comScore += 1
    elif usrInput == "S" and comInput == "P":
      sAp()
      print("player win")
      usrScore += 1
    elif usrInput == "S" and comInput == "S":
      sAs()
      print("draw")
