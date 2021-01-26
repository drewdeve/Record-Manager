from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
from tkinter import ttk
import pymysql

def artistRegister():

    first_name = atrInf2.get()
    last_name = atrInf3.get()
    sex = atrInf4.get()
    b_day = atrInf5.get()


    insertPerson = "insert into" + personTable+" values('"+first_name+"','"+last_name+"','"+sex+"', '"+b_day+"')"
    try:
        cur.execute(insertPerson)
        con.commit()
        messagebox.showinfo('Success',"Artist added successfully")
    except:
        messagebox.showinfo("Error","Can't add data into Database")




    print(f_name)
    print(l_name)
    print(sex)
    print(b_day)



    root.destroy()


def addArtist():

    global  atrInf2, atrInf3, atrInf4, atrInf5, root

    root = Tk()
    root.title("Actors Record Management System")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    # Add database
    mypass = "12345qwerty"
    mydb = "artists"

    con = pymysql.connect(host="localhost", user="root", password = mypass, database=mydb)

    cur = con.cursor()

    # Enter Table Names here
    artistTable = "person"

    Canvas1 = Canvas(root)

    Canvas1.config(bg="#c73934")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame = Frame(root,bg="#17209c",bd=7)
    headingFrame.place(relx=0.2,rely=0.2,relwidth=0.6,relheight=0.16)
    headingLabel = Label(headingFrame, text="Add Artist", bg='black', fg='white', font=('arial', 20, 'bold'))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)


    ArtInfo2 = StringVar()
    ArtInfo3 = StringVar()
    ArtInfo4 = StringVar()
    ArtInfo5 = StringVar()

    # Artist f name
    lb2 = Label(labelFrame,text="First name : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    atrInf2 = Entry(labelFrame, textvariable = ArtInfo2)
    atrInf2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
        
    # Artist l name
    lb3 = Label(labelFrame,text="Last Name : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
    atrInf3 = Entry(labelFrame, textvariable = ArtInfo3)
    atrInf3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)
        
    # Artist sex
    lb4 = Label(labelFrame,text="Sex (F/M) : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.65, relheight=0.08)
        
    atrInf4 = Entry(labelFrame, textvariable = ArtInfo4)
    atrInf4.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)

    # Artist b-day
    lb5 = Label(labelFrame,text="Birthday : ", bg='black', fg='white')
    lb5.place(relx=0.05,rely=0.80, relheight=0.08)
        
    atrInf5 = Entry(labelFrame, textvariable = ArtInfo5)
    atrInf5.place(relx=0.3,rely=0.80, relwidth=0.62, relheight=0.08)


    #Button
    AddBtn = Button(root,text="Add",bg='#d1ccc0', fg='black',command=artistRegister)
    AddBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    ExitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    ExitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()

    

    







    
