#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
r=open("/Users/notpranavramane/Work/100_Days_Python/Day_24_Mail_Merge/Input/Letters/starting_letter.txt","r")
invi=open("/Users/notpranavramane/Work/100_Days_Python/Day_24_Mail_Merge/Input/Names/invited_names.txt")
name=(invi.readlines())
print(name)
k=r.read()
for i in range(0,len(name)):
    n=name[i]
    n=n.strip()
    writ=open(f"/Users/notpranavramane/Work/100_Days_Python/Day_24_Mail_Merge/Output/ReadyToSend/{n}.txt","a")
    j=k.replace("[name]",n)
    writ.write(j)
