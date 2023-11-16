import pandas
df=pandas.read_csv(r"C:\Users\HP\Desktop\AI\NATO-alphabet-start\nato_phonetic_alphabet.csv")
letter_dict={rows.letter:rows.code for (index,rows) in df.iterrows()} #This is used to iterate over rows in pandas dataframe
# print(letter_dict)

name_input=input("What is Your name? ")
# nato=[letter_dict.get(items.upper()) for items in name_input ] 
# print(nato)
nato=[]
for items in name_input:
    try:
        nato.append(letter_dict.get(items.upper()))
    except KeyError:
        print("Only Words please!")
print(nato)