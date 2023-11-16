# numbers=[1,2,3]
# new_list=[items + 1 for items in numbers]

# print(new_list)

# numbers=[12,13,14,15,16,17,18,19,20]
# squared_list=[num**2 for num in numbers]
# print(squared_list)

# name="Bhaskar"
# new_list=[letters for letters in name]

# print(new_list)

# new_list=[num*2 for num in range(1,5)]
# print(new_list)

# names=["alex","bravo","chap","doof","giganto","mani","chimp","chip"]
# short_names=[items.upper() for items in names if len(items)>=5]
# print(short_names)

import random
# names=["alex","bravo","chap","doof","giganto","mani","chimp","chip"]

# name_score={items:random.randint(25,100) for items in names}
# print(name_score)


scores={'alex': 49, 'bravo': 27, 'chap': 74, 'doof': 49, 'giganto': 70, 'mani': 68, 'chimp': 46, 'chip': 79}

passed_stu={items:f"pass with {scores.get(items)}" for items in scores.keys() if scores.get(items)>50}
print(passed_stu)
