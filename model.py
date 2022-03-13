# creating all the python canvas widgets

from tkinter import  ttk
import tkinter as tk
from PIL import Image,ImageTk
from windows import set_dpi_awareness

import mysql.connector
from mysql.connector import errorcode
from mysql.connector import Error



set_dpi_awareness()

class mainFrame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.frame = tk.Frame(self, width=1200, height=10000)
        self.frame.pack(expand=True, fill='both')
        self.canvas = tk.Canvas(self.frame, bg='#FFFFFF', width=300, height=300, scrollregion=(0, 0, 1200, 10000))
        self.hbar = tk.Scrollbar(self.frame, orient='horizontal')
        self.hbar.pack(side='bottom', fill='x')
        self.hbar.config(command=self.canvas.xview)
        self.vbar = tk.Scrollbar(self.frame, orient='vertical')
        self.vbar.pack(side='right', fill='y')
        self.vbar.config(command=self.canvas.yview)
        self.canvas.config(width=1200, height=10000)
        self.canvas.config(xscrollcommand=self.hbar.set, yscrollcommand=self.vbar.set)
        self.canvas.pack(side='left', expand=True, fill='both')
        self.cnx = mysql.connector.connect(user='root', password='kamalanita1@',
                                      host='localhost',
                                      database='images')
        self.place_images()

        # we will dividing the entire canvas into 10 sections 1000px each and then draw different bodies
        # drawing shapes
        line1 = self.canvas.create_line(0,1000,1200,1000,width=4)
        line2 = self.canvas.create_line(0, 2000, 1200, 2000,width=4)
        line3 = self.canvas.create_line(0, 3000, 1200, 3000,width=4)
        line4 = self.canvas.create_line(0, 4000, 1200, 4000,width=4)
        line5 = self.canvas.create_line(0, 5000, 1200, 5000,width=4)
        line6 = self.canvas.create_line(0, 6000, 1200, 6000,width=4)
        line7 = self.canvas.create_line(0, 7000, 1200, 7000,width=4)
        line8 = self.canvas.create_line(0, 8000, 1200, 8000,width=4)
        line9 = self.canvas.create_line(0, 9000, 1200, 9000,width=4)
        # for each quarter creating images and adding a description
        for i in [0,1000,2000,3000,4000,5000,6000,7000,8000,9000]:
            j=i;
            while j<i+1000:
                self.canvas.create_line(0,j+200,1200,j+200,width=1)
                j=j+200
        for i in [300,600,900,1200]:
            self.canvas.create_line(i,0,i,10000,width=1)



    def fetch_values(self):
        try:

            query = "SELECT * from location"
            cursor = self.cnx.cursor()
            cursor.execute(query)
            result = cursor.fetchall()

            return result  # this is a list of tuple therfore for each value extraced you can gain further access to other two values of tuple
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            print("Insert operation failed tu toe lut gya re gotiya")

    def place_images(self):
        arr = self.fetch_values()
        result = []
        for val in arr:
            result.append(val[0])
        images = []
        for value in result:
            image = Image.open(value).resize((280,180))
            images.append(image)
        self.photos = []
        for image in images:
            self.photo = ImageTk.PhotoImage(image)
            self.photos.append(self.photo)


        i=0
        index = 0
        while i < 10000 and index < len(self.photos)-2:
            for j in [0,300,600,900]:
                self.canvas.create_image(j+10,i+10,image = self.photos[index],anchor='nw')
                index = index + 1
            i = i + 200

















root=mainFrame()
root.columnconfigure(0,weight=1)
root.mainloop()