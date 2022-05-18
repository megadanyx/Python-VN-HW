######### EXTRAGEM DIN FAIL #####
num_int = []
file = open("num.txt", "r")
num_int = file.read().split(" ")
######### EXTRAGEM DIN FAIL #####
######### TRANSFORMAM IN INT #####
my_num = []
for row in num_int:
    my_num.append(int(row))
print("Maxim: ",max(my_num),"\nMinim: ",min(my_num))

######### TRANSFORMAM IN INT #####