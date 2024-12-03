"""
Author: daiji Kuriakose
Date:3-12-2024
Title:Python program of stick game
"""
print("wellcome to the stick play")
player1=input("Enter the 1 st player name")
player2=input("Enter the 2 nd player name")
stick_remaining=16
while stick_remaining>0:
    player = player1
    print("stick remaining=",stick_remaining)
    n=int(input(f"{player} pick 1,2 or 3 sticks"))
    stick_remaining=stick_remaining-n
    if stick_remaining==0:
        print(f"{player},  picks the last stick and loses the game")
    else:
        player=player2
        print(f"stick remaining",stick_remaining)
        i=int(input(f"{player} pick 1,2 or 3 sticks"))
        stick_remaining=stick_remaining-i
        if stick_remaining==0:
           print(f"{player} picks the last stick and loses the game")
print()