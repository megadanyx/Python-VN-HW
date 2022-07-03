# to hide the password we will use HASING
# python bibliotec for hasing password : haslib ,bcrypt, ... 


import hashlib

def MakeTransMail(email):
    mail   ="@gmaileho.co"
    nonmail="*/[]'$%^&*(^"
    mytableemail= email.maketrans(mail,nonmail)
    email = email.translate(mytableemail)        
    return email



def MyHasher(password,Email): # ADDed in Client.__init__ ---> self.password = MyHasher(password,Email)
    lastEmail = MakeTransMail(Email)
    firstPass=password+lastEmail
    hasher = hashlib.md5(firstPass.encode())
    prefixpass  = hasher.hexdigest()
    passwordhash = hashlib.sha3_384(str(prefixpass).encode())
    final_pass = passwordhash.hexdigest()
    return final_pass
