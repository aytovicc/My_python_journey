#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

name_list = []

with open("/Users/Ben/Python Projects/mailmerge/Input/Names/invited_names.txt", 'r') as names_txt:
    names = names_txt.readlines()
    for name in names:
        _name = name.strip("\n")
        name_list.append(_name)


for x in name_list:
    with open("/Users/Ben/Python Projects/mailmerge/Input/Letters/starting_letter.txt", 'r') as starting_letter:
        letter = starting_letter.read()
        letter2 = letter.replace("[name]", f"{x}")
        with open(f"/Users/Ben/Python Projects/mailmerge/Output/{x}.txt", 'w') as new_letter:
            final = new_letter.write(letter2) 
            
        


#with open("/Users/Ben/Python Projects/mailmerge/Input/Letters/starting_letter.txt", 'r') as pattern:

    
