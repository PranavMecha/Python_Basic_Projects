alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
k=1
print("""
         ░█▀▀░█▀█░█▀▀░█▀▀░█▀█░█▀▄░░░█▀▀░▀█▀░█▀█░█░█░█▀▀░█▀▄
         ░█░░░█▀█░█▀▀░▀▀█░█▀█░█▀▄░░░█░░░░█░░█▀▀░█▀█░█▀▀░█▀▄
         ░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀░▀░▀░▀░░░▀▀▀░▀▀▀░▀░░░▀░▀░▀▀▀░▀░▀ 
      """)
def ceaser(original_text,shift_no,imp):
  display1="" 
  display="" 
  for letter in original_text:
    if letter in alphabets:
        if imp=="encode":
            shifted_no=alphabets.index(letter)+shift_no
        else:
            shifted_no=alphabets.index(letter)-shift_no
        if shifted_no>25:
            shifted_no=shifted_no%26
        display+=alphabets[shifted_no]
    else:
        display1+=letter
  if imp=="encode":
    print(f"Your code is {display+display1}")
  else:
    print(f"Your code says {display+display1}")

while k==1:
    command=input("Enter 'encode' for Encryption and 'decode' for decryption : ").lower()
    text=input("Enter your text : ").lower()
    shifts=int(input("Enter no of shifts : ")) 
    ceaser(original_text=text,shift_no=shifts,imp=command)
    print("-------------------------------------------------------------------------------------------------")
    Ask1=input("Do you want to continue? [Y/N] :").lower()
    if Ask1=="n":
        print("Thanks :)")
        break
