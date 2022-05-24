############### Provider ##################


class User:
    
    def __init__(self, nickname, password):
        self.nickname = nickname
        self.password = password
        self.online   = False
        self.friends  = []
    
    def __str__(self):
        return f"User <{self.nickname}>"
    
    def __repr__(self):
        return self.__str__()
    
    # User specific LogIn (autentific)
    def auth(self , nickname , password):
        if nickname == self.nickname and password == self.password:
            self.online = True 
            return True
        else:
            return False
    def addFriend(self ,friend):
        if  type(friend) == type(self) :
            if len(self.friends) == 0:
                self.friends.append(friend.nickname)     
            else:
                index = 0
                for row in self.friends:
                    index = index + 1
                    if friend.nickname != row:
                        if len(self.friends) == index:
                           self.friends.append(friend.nickname)  
                    else:
                        return False

############### Provider ##################


############## Consumer #####################


user_1 = User("Mihai", "qwerty1234")
user_2 = User("Petr", "qwerty1234")
user_3 = User("John", "qwerty1234")
user_4 = User("Marry", "qwerty1234")
user_5 = User("Lory", "qwerty1234")


print(user_1.friends)
print(user_2.friends)
print(user_3.friends)
user_1.auth("Mihai", "qwerty1234")

user_1.addFriend(user_2)
user_1.addFriend(user_3)
user_1.addFriend(user_4)
user_1.addFriend(user_5)


print(f"\nUser {user_1.nickname} has friends {user_1.friends}")
#print(f"User{user_2} has friends {user_2.friends}")
# print(f"User{user_3} has friends {user_3.friends}")


############## Consumer #####################