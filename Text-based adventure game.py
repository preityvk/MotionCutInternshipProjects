answer_yes = ["Yes", "Y", "yes", "y"]
answer_no = ["No", "N", "no", "n"]
print("Enter any key to start the game")
start=input(">>")
print("""
WELCOME! LET'S START THE ADVENTURE!
You are currently living in your mansion with your family...
Someone knocks on your front door

Do you wish to open the door? (Yes/No)""")

ans=input(">>")

if ans in answer_yes:
    print("\nAn old man in tattered clothes is standing outside your house and asks if he can get into your house for sometime.")
    print("\nWill you provide shelter to him? (Yes/No)")
    ans1=input(">>")

    if ans1 in answer_yes:
        print("\nThe man enters your house")
        print("\nAfter 2 minutes, the police came to your house and ask whether an old man entered?")
        print("Will you tell the police that he is in the house? (Yes/No)")
        ans2=input(">>")

        if ans2 in answer_yes:
            print("\nYou are an honest person. He was a thief")
            print("\nThe thief was caught by the police")
            print("\nYou won the game!")
        elif ans2 in answer_no:
            print("\nYou helped a thief. You will go to jail")
            print("\nYou lose! Game Over")
        else:
            print("Enter the valid option (Yes/No)")
            
    elif ans1 in answer_no:
        print("\nNow, the man is trying to kill you!")
        print("\nWill you knock him down/ (Yes/No)")
        ans3=input(">>")

        if ans3 in answer_yes:
            print("\nHe was a thief and you helped the police catch the thief")
            print("\nYou won the game")
        elif ans3 in answer_no:
            print("\nYou died. He was a thief and he killed you!")
            print("\nYou lose! Game Over")
            
    else:
        print("Enter the valid option (Yes/No)")
        
elif ans in answer_no:
    print("\nThe thief was caught by the police")
    print("\nYou won the game!")
    
else:
    print("Enter the valid option (Yes/No)")
