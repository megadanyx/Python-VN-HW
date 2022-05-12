from os import system

def clear():
    system("cls")

def controls():
    print("\nuse a, d, s, w - for direction ")
    key = input(">>> ")
    return key