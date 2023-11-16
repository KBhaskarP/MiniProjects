num=int(input("Enter the number here"))


def factorial(num):
    fact=num-1
    ans=num
    while fact>0:
        ans*=fact
        fact-=1
    return ans

def count_zeroes(new_num):
    count=0
    str_num=str(new_num)
    for elements in str_num:
        if elements=="0":
            count+=1
            
    return count
print(factorial(num))
print(f"Trailing zeroes are : {count_zeroes(factorial(num))}")