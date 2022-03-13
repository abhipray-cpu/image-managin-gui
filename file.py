import tkinter as tk
from tkinter import ttk
from windows import set_dpi_awareness
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
set_dpi_awareness()
import mysql.connector
from mysql.connector import errorcode
from mysql.connector import Error


def insert_values(path):
    try:
        cnx = mysql.connector.connect(user='root', password='kamalanita1@',
                                      host='localhost',
                                      database='images')
        data_login = (path,)
        query = "INSERT INTO location (Path) VALUES (%s)"
        cursor = cnx.cursor()
        cursor.execute(query, data_login)
        print("Abhi toe aur chlega")
        cnx.commit()
        print("Abhi bhi chl rha hai")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        print("Insert operation failed tu toe lut gya re gotiya")
#build a better ui upon this and then merge the two
# create the root window
root = tk.Tk()
root.title('Tkinter Open File Dialog')
root.resizable(False, False)
root.geometry('300x150')


def select_file():
    filetypes = (
        ('Image', '.png'),
        ('text files', '*.txt'),
        ('All files', '*.*'),

    )

    filename = fd.askopenfilenames(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)


    filename=filename
    paths=[]


    for name in filename:
        data = name.split('/')
        path=f"./{data[-2]}/{data[-1]}"
        paths.append(path)


    print(paths)


    for path in paths:
        insert_values(path)





    showinfo(
        title='Selected File',
        message=filename
    )


# open button
open_button = ttk.Button(
    root,
    text='Open a File',
    command=select_file
)

open_button.pack(expand=True)


# run the application
root.mainloop()
