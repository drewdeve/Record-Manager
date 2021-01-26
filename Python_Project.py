# importing all the necessary packages
from PIL import ImageTk
from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from AddPerson import *
import pymysql

# defining of the function to creat the frame using tkinter library.
def main():
    root = Tk()
    app = Login(root)
    root.mainloop()

# Below code represent the creation of the Login Frame to the Management System.
class Login:
    def __init__(self, master):
        self.master = master
        # self.master.attributes('-fullscreen', True)
        # addign a background image to the Login Frame using PIL (Pillow) package.
        self.image = ImageTk.PhotoImage(file = "C:/Users/roven/3.jpg")
        self.label = Label(self.master, image = self.image).place(x = 0, y = 0, relwidth = 1, relheight = 1)
        # Replacing a Login frame name form tk to Actors Record Management System 
        self.master.title("Actors Record Management System")
        self.master.geometry('1199x600+100+50')

        # Creating a frame and setting the background color to blue
        self.headingFrame = Frame(self.master,bg="#17209c",bd=7)
        # Defining the place of the blue frame
        self.headingFrame.place(x = 300, y = 200, height = 304, width = 535)

        # Addign a label to the headingFrame,  definign the backroung color, font and color of the letter. 
        self.LabelTitle = Label(self.headingFrame, text = 'Actors Record Management System', bg='black', fg='white', font = ('arial', 20, 'bold'))
        self.LabelTitle.place(x = 6, y = 5, height = 70, width = 510) 

        # Creating of 2 more frames. Later they will be used for Password and Login insert frames and buttons.
        self.frame1 = Frame(self.headingFrame, bd = 15, bg='black')
        self.frame1.place(x = 6, y = 75, width = 510, height = 140 )

        self.frame2 = Frame(self.headingFrame, bd = 15, bg='black')
        self.frame2.place(x = 6, y = 215, width = 510, height = 70)

        
        #defining variables Username and Password in order to save the string values and use them to enter the system. Later this variables will be used in Login_function.
        self.Username = StringVar()
        self.Password = StringVar()

        # Adding Text fields and labels to the frame1.
        self.LabelUsername = Label(self.frame1, text = 'Username', bg='black', fg='white', font = ('arial', 20, 'bold'))
        self.LabelUsername.grid(row = 0, column = 0)
        # Definign textvariable in order to retrieve a string saved under Esername variable. 
        self.EntryUsername = Entry(self.frame1, text = 'Password', bg='black', fg='white', font = ('arial', 20, 'bold'),
                                 textvariable = self.Username,                                )
        self.EntryUsername.grid(row = 0, column = 1)

        self.LabelPassword = Label(self.frame1, text = 'Password', bg='black', fg='white', font = ('arial', 20, 'bold'), )
        self.LabelPassword.grid(row = 1, column = 0)
        # Definign textvariable in order to retrieve a string saved under Password variable.
        self.TextPassword = Entry(self.frame1, text = 'Password', bg='black', fg='white', show = '*', font = ('arial', 20, 'bold'),
                                 textvariable = self.Password,                                )
        self.TextPassword.grid(row = 1, column = 1)

        
        # Creating buttons for Login and Exit and placing the on earlier created frame2.
        self.ButtonLogin = Button(self.frame2, text = "Login", bg = 'black', fg='white', width = 19, font = ('arial', 15, 'bold'),
                               command = self.Login_function)
        self.ButtonLogin.grid(row = 0, column = 0)
        
        self.ButtonExit = Button(self.frame2, text = "Exit", bg = 'black', fg='white', width = 19, font = ('arial', 15, 'bold'),
                               command = self.Exit_function)
        self.ButtonExit.grid(row = 0, column = 1)

    # Creating of the Login_function which will be used to login to the system. 
    def Login_function(self):
        user = (self.Username.get()) # retrieving the string saved as Username 
        pas = (self.Password.get())  # retrieving the string saved as Password

        if (user == str(1234)) and (pas == str(2345)):   # cheking of if the inserted strings are equal to the admin password and username.
            self.Management_window() # if the conition is met, user is logged in to the system
        else:
            tkinter.messagebox.askyesno("Actors Management System", "You do not have access to Management System") # Message the user gets when the password or username is not correct.
            self.Username.set('')
            self.Password.set('')

    # Defining of the exit function       
    def Exit_function (self):
        self.Exit_function = tkinter.messagebox.askyesno("Actors Management System", "Are you sure you want to exit?")
        if self.Exit_function > 0:
            self.master.destroy()
            return
        
        #=============================================================================================

    # Function to open a new window called Management_window after clicking on the Login button.
    def Management_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Management_system(self.newWindow)


# Creating of the Management system window.
class Management_system:
    
    def __init__(self, master):
        self.master = master
        # Adding a background picture.
        self.image = ImageTk.PhotoImage(file = "C:/Users/roven/4.jpg")
        self.label = Label(self.master, image = self.image).place(x = 0, y = 0, relwidth = 1, relheight = 1)
        self.master.title("Management System")
        self.master.geometry('1199x600+100+50')

        # Creating a frame for Main title 
        self.headingFrame = Frame(self.master,bg="#17209c",bd=7)
        self.headingFrame.place(relx=0.2,rely=0.2,relwidth=0.6,relheight=0.16)
        self.headingLabel = Label(self.headingFrame, text="Management System", bg='black', fg='white', font=('arial', 20, 'bold'))
        self.headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

        # Creating of the buttons.
        Button_Add = Button(self.master,text="Add",bg='black', fg='white', font = ('arial', 12, 'bold'), command=addArtist())
        Button_Add.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
        Button_Delete = Button(self.master,text="Delete",bg='black', fg='white',font = ('arial', 12, 'bold'), command=self.Delete())
        Button_Delete.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
        Button_Search = Button(self.master,text="Search",bg='black', fg='white', font = ('arial', 12, 'bold'), command=self.Search())
        Button_Search.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    
        Button_Update = Button(self.master,text="Update",bg='black', fg='white', font = ('arial', 12, 'bold'), command = self.Update())
        Button_Update.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)
    
        Button_Exit = Button(self.master,text="Exit",bg='black', fg='white', font = ('arial', 12, 'bold'), command = self.Update())
        Button_Exit.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)




if __name__ == '__main__':
    main()
                        
                                


        

                                

        
    
