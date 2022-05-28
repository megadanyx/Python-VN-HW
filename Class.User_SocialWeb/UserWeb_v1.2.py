
# Hw5:
# * Create the messade class: body , fromUser , toUser , status
#    
# 
# 
# 


############### Provider ##################


class User:
    
    def __init__(self, nickname, password):
        self.nickname = nickname
        self.password = password
        self.online   = False
        self.friends  = []
        self.posts    = []
        self.sent_messages  = []
        self.inbox_messages = []
        self.message_statys = "unseen"
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
        if  type(friend) != User:
            return
        friend_exists = False
        for existing_friend in self.friends:
            if existing_friend.nickname == friend.nickname:
                friend_exists = True
                break
        if not friend_exists:
            self.friends.append(friend)

    def post(self, title, body):
        if type(title) == str and type(body) == str:
            new_post = Post(title,body)
            self.posts.append(new_post)
            new_post.author = self

        return new_post
    def send(self, body , toUser):

        message = Message(self.nickname ,body ,toUser )       
        self.sent_messages.append(message)
        toUser.inbox_messages.append(message) 
        return message

    def read(self, index):
        status = self.inbox_messages[index]
        self.inbox_messages.pop(index)
        status.status = "seen"
        self.inbox_messages.insert(index, status)

        return status



class Post:

    def __init__(self, title , body):
        self.title = title
        self.body  = body

    def __str__(self):
        return f"{self.title}"
    
    def __repr__(self):
        return self.__str__()
    

class Message:

    def __init__(self, fromUser, body , toUser ):
        self.status = "unseen"
        self.fromUser = fromUser
        self.body = body
        self.toUser = toUser
    def __str__(self):
        return f"From: {self.fromUser:<5} > | {self.body} |({self.status}) - to > :{self.toUser.nickname:>6}"
    
    def __repr__(self):
        return self.__str__()
        

           
############### Provider ##################


############## Consumer #####################


user_1 = User("Mihai", "qwerty1234")
user_2 = User("Petr", "qwerty1234")
user_3 = User("John", "qwerty1234")
user_4 = User("Marry", "qwerty1234")
user_5 = User("Lory", "qwerty1234")

user_1.send("Hi My friend How are you?" , user_2)
user_2.send("Hi, im fine thank you , you?", user_1)
# user_2.read(0)

print(user_1.sent_messages[0])
print()
print(user_2.sent_messages[0])
print("---------------------------------------")
print(user_1.read(0))
print()
print(user_2.read(0))
print("---------------------------------------")
# user_1.auth("Mihai", "qwerty1234")

# post_1 = user_1.post("My Posts" , " My text for body posts ")

# post_1 = user_1.post("My Posts 2" , " My text for body posts ")

# post_1 = user_1.post("My Posts 3" , " My text for body posts ")
# user_1.post(user_3)


# print(" The post :",  user_1.posts," The author of post :" , post_1.author)
#print(f"User{user_2} has friends {user_2.friends}")
# print(f"User{user_3} has friends {user_3.friends}")


############## Consumer #####################