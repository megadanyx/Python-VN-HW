### HW add var name to func ,

def HelloMy(lang,name):
    if lang == "en":
        print(f"Hello {name}")
    elif lang == "ro":
        print(f"Salut {name}")
    elif lang == "ru":
        print(f"Привет {name}")

lang = str(input("Tast you lang en/ro/ru >>>  "))
name = str(input("Tast you Name:  >>>  "))
HelloMy(lang,name)

## HW2 func * , / , + , - || rewrite r = 1+2*3/4

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

r = div(add(mul(2, 3),1),4)
print(r)