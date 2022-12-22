from tkinter import *
import string
import secrets

##########     Password Generator     ##########
password_chars = string.ascii_letters + string.digits + string.punctuation

def password_generator():
    password_field.delete(0, END)
    length = int(char_input.get())
    password = "".join([secrets.choice(password_chars) for _ in range(length)])
    password_field.insert(0, password)

##########     User Interface     ##########
root = Tk()
root.title('Password Generator')
root.iconbitmap('password-76.ico')
root.config(padx=50, pady=50)

label_title = Label(text="Strong Password Generator",
                    
                    
                    font=("Arial", 35, "bold"))
label_title.grid(row=0, column=0, columnspan=3, pady=30)

label_before_input = Label(text="Choose a number for your password length",
                           
                           
                           font=("Arial", 15, "bold"))
label_before_input.grid(row=1, column=0)

char_input = Entry()
char_input.grid(row=1, column=1)
char_input.insert(0, "12")
char_input.focus()

generate_password_button = Button(text="Generate Password",font=('Arial',15,'bold'),
                                  height=2,
                                  width=20,
                                  bg= 'black',
                                  fg= 'white',
                                  command=password_generator)
generate_password_button.grid(row=2, column=0, columnspan=3, padx=50, pady=50)

password_field = Entry(
                       font=("Arial", 15, "bold"), width=40)
password_field.grid(row=3, column=0, columnspan=3)

root.mainloop()