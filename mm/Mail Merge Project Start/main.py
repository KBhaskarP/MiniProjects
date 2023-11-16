#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
ls=[]
with open(r"mm\Mail Merge Project Start\Input\Names\invited_names.txt") as names:
    new_ls=names.readlines(33)#This is used to read line in a file
    for items in new_ls:
        ls.append(items[:-1])
        
with open("mm/Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter:
    content=letter.read()
    for items in ls:
        invite=content.replace("[name]",items)
        with open(f"mm\Mail Merge Project Start\Output\ReadyToSend\Invited_{items}.txt","w") as invitation:
            invitation.write(invite)