# Draw this pattern : # * # * # * # * # *
# 10 size pattern
# HW1 : Draw this pattern : # * * # * * # * * # * * 

symbol = 1
stars  = 0
patt_size = int(input("Enter paterns size: " ))
print("\n")

while symbol <= patt_size:
    if symbol <= patt_size and stars != 0:
        print("*", end = " " )
        stars += 1
    else:
        print("#", end = " " )
        stars +=1
    if stars == 3 :
        stars = 0
    symbol +=1






print("\n")
