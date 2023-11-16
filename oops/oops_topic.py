class User: #class
    def __init__(self,user_id,user_name) -> None:
        # print("new_user created")  
        self.id=user_id
        self.name=user_name
        self.followers=0
        self.following=0
        
    def follow(self,user):
        user.followers+=1
        self.following+=1


user_1=User("1","Bhaskar")#object
user_2=User("2","Nitisha")#object
user_1.follow(user_2)
# print(user_1)
print(user_1.followers)
print(user_1.following)

print(user_2.followers)
print(user_2.following)