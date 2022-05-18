from tkinter import *
from cryptography.fernet import Fernet
import os

def generate():
     # key generation
    key = Fernet.generate_key()

    # string the key in a file
    with open('filekey.key', 'wb') as filekey:
        filekey.write(key)
        print('generated: ',key)

def encrypt(user):
    # opening the key
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()
        print('encrypt key: ',key)
    # using the generated key
    fernet = Fernet(key)

    # opening the original file to encrypt
    with open(user, 'rb') as file:
        original = file.read()
        print('encrypt file read: ',original)
        
    # encrypting the file
    encrypted = fernet.encrypt(original)

    # opening the file in write mode and
    # writing the encrypted data
    with open(user, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

def decrypt(user1):
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()
        print(key)

    fernet = Fernet(key)

    with open(user1, 'rb') as enc_file:
        encrypted = enc_file.read()
        print('decrypt file name: ', encrypted )

    decrypted = fernet.decrypt(encrypted)
    print('decryption file: ', decrypted)

    with open(user1, 'wb') as dec_file:
        dec_file.write(decrypted)

# window for registration
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")
 
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
 
    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()


# window for login 

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
 
# event on register button

def register_user():
 
    username_info = username.get()
    password_info = password.get()
    
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
    
    list_of_files = os.listdir()
    if 'filekey.key' not in list_of_files:  
        generate()
    encrypt(username_info)
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 
    Button(register_screen, text="OK", command=delete_register_success).pack()

#  event on login button 
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        
        decrypt(username1)

        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
            encrypt(username1)
            import TestEmotionDetector

        else:
            password_not_recognised()
            encrypt(username1)
    else:
        user_not_found()
 
# popup for login success
 
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    login_screen.destroy()
    login_success_screen.destroy()
    main_screen.destroy()
 
# popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups
def delete_register_success():
	register_screen.destroy()

def delete_login_success():
	login_screen.destroy()
	login_success_screen.destroy()
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
 
#  Main window
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()
 
    main_screen.mainloop()
 
 
main_account_screen()