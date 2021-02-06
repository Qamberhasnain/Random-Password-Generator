import random
import string

def rand_pass_gen():
    try:
        leng = int(input(">>>> Enter the length of password to be generated: \n>>>> "))
        rpg=[]
        letters = string.ascii_letters + string.digits + string.punctuation
        i = 0
        while i < leng:
            rpg.append(random.choice(letters))
            i += 1
        global result_str
        result_str = ''.join(rpg)
        save = input('>>>> If you want to save password write "save": \n>>>> ')
        if save == 'save':
            save_password()
        else:
            print('>>>> Invalid input. Generate new password')
    except ValueError:
        print('>>>> Invalid input, Please provide integer value for length.')


def save_password():
    f = open("pass_file.txt", "w")
    f.write('>>>> Your new password generated: '+ result_str)
    f.close()
    open_f = input('>>>> If you want to open file write "open": \n>>>> ')
    if open_f == 'open':
        open_file()
    else:
        print('>>>> Invalid input. You have to open "pass_file.txt" by yourself.')
    

def open_file():
    f = open("pass_file.txt","r")
    fh = f.read()
    print(fh)
    f.close()


def new_pass():
    new =  input('>>>> If you want to create new password write "new": \n>>>> ')
    if new == 'new':
        rand_pass_gen()
    else:
        print('>>>> Invalid input. Generate new password')


print("*"*40,'WELCOME TO RANDOM PASSWORD GENERATOR',"*"*40)
print()
print("RULES FOR GENERATING A NEW PASSWORD:-\n    This application will give you a new password every time you run this application.\n    1. Application is command line user interface <<so be carefull while giving an input>>.\n    2. It will ask you to write \"new\" in order to create new password.\n    3. Then it will ask you to give the length of which the password would be generated.\n    4. It will ask you to write \"save\" in order to save your password in a file <<pass_file.txt>>. \n    4. Lastly it will ask you to write open to see your newly generated password.\n")
new_pass()
print()
print("*"*40,"Thank you for using our Random Password Generator :)","*"*40)