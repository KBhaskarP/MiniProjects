# def add(*args):
#     sum=0
#     for items in args:
#         sum+=items
#     return sum        

# print(add(5,3,4,5))



def calculator(n,**kwargs):
    ls=[]
    for keys in kwargs.keys():
        if keys=="add":
            ls.append(n+kwargs[keys])
        elif keys=="sub":
            ls.append(n-kwargs[keys])
        elif keys=="mul":
            ls.append(n*kwargs[keys])
        else:
            ls.append(n%kwargs[keys])
    return ls


print(calculator(5,add=5,sub=1,mul=5,div=3))