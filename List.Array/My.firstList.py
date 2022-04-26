# empty list


friends = []

while len (friends) < 100:
    name = input("Add frind name: ")
    if name == "" or name == "Watch":
        break
    if name in friends:
        print("This name exist in your list")
        print("If you want watch you friend list:(Hit Enter)/(Watch)\n")
        continue
    friends.append(name)

print("You have", len(friends), "friends")
for i in range(len(friends)):
    print("   ",i ,">>>", friends[i])