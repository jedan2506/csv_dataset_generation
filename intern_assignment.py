import csv
import time
import pandas as pd
from faker import Faker
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import tkinter as tk
from random import randint

class assignment:
    
    def __init__(self):
        self.check=0
        self.arr=[]   
        self.fake = Faker()
        self.win=0
        self.ent=0
    
        
    def choose(self):
        Tk().withdraw()
        self.fileadd = askopenfilename()
        if (len(self.fileadd) != 0):
            self.pos=self.fileadd.rfind('/')
            self.fileadd=self.fileadd[0:self.pos+1]+"users.csv"
            print(self.fileadd)
            self.check=1
    
    
    def layout(self):
        self.win = tk.Tk()
        self.win.geometry("326x300")
        self.win.title("Internship Assignment")
        self.win.configure(bg='cyan')
        
        Label(self.win, text="Welcome to the Dashboard", font="Times 18 underline bold", bg='cyan').place(x=20, y=20)
        Label(self.win, text="Internship Assignment", font="Times 14", bg='cyan').place(x=80, y=60)
        btn1 = Button(self.win, text="CHOOSE", width=14, height=2, command=self.choose).place(x=40, y=140)
        btn2 = Button(self.win, text="START", width=14, height=2, command=self.collect_data).place(x=176, y=140)
        btn3 = Button(self.win, text="SEARCH", width=14, height=2, command=self.retrieve).place(x=40, y=210)
        btn4 = Button(self.win, text="SORT", width=14, height=2, command=self.sort).place(x=176, y=210)
        
        self.win.mainloop()
    
    def storing(self):
        file = open(self.fileadd, "w", newline='')
        csvwriter = csv.writer(file)
        csvwriter.writerow(["ID","First Name", "Last Name", "Email ID", "Address", "Country", "Job"])
        csvwriter.writerows(self.arr)
        file.close()
        self.arr=[]
        
        
    def collect_data(self):
        count=0
        self.arr = []
        if(self.check==0):
            messagebox.showinfo("PROBLEM", "Please Choose a File")
        else:
            while(count<20):
                details = [randint(2000, 2100),self.fake.first_name(), self.fake.last_name(), self.fake.email(), self.fake.address(), self.fake.country(), self.fake.job()]
                print(details)
                print(self.arr)
                self.arr.append(details)
                count=count+1
                time.sleep(1)
                
            self.storing()
        
    def sort(self):
        if(self.check==0):
            messagebox.showinfo("PROBLEM", "Please Choose a File")
        else:
            self.reading()
            for i in range(1,len(self.arr)-1):
                for j in range(i+1,len(self.arr)):
                        if(self.arr[i][1]>self.arr[j][1]):
                            list=self.arr[i]
                            self.arr[i]=self.arr[j]
                            self.arr[j]=list
                            
            file = open(self.fileadd[0:self.pos+1]+"users-sorted.csv", "w", newline='')
            csvwriter = csv.writer(file)
            csvwriter.writerows(self.arr)
            if(len(self.arr)>1):
                messagebox.showinfo("Information", "The Data Retrieved from 'users.csv' has been successfully sorted (as per First Name) and Stored in 'users-sorted.csv'!!")
            else:
                messagebox.showinfo("PROBLEM", "Due to some Issue the Data has not been Retrieved Successfully!!")
            file.close()
      
    def reading(self):
        self.arr = []
        rfile = open(self.fileadd, "r", newline='')
        self.csvreader = csv.reader(rfile)
        for data in self.csvreader:
            self.arr.append(data)

        print(self.arr)
        
        
    def retrieve(self):
        if(self.check==0):
            messagebox.showinfo("PROBLEM", "Please Choose a File")
        else:
            self.reading()
            nwin=Toplevel(self.win)
            nwin.geometry("300x100")
            nwin.title("SEARCH")
            nwin.configure(bg='cyan')
            
            lab = Label(nwin, text="Enter the ID to Search:: ",
                        bg='cyan').place(x=16, y=20)
            self.ent=Entry(nwin)
            self.ent.place(x=146, y=22)
            but=Button(nwin, text="Start Search",command=self.search).place(x=146,y=60)
            
    def search(self):
        point = 0
        print(self.ent.get())
        for i in range(1, len(self.arr)):
            if (self.arr[i][0] == self.ent.get()):
                point = i
                break

        if(point!=0):
            messagebox.showinfo("Information", "ID:: "+self.arr[point][0]+"\nFirst Name:: "+self.arr[point][1] +
                                "\nLast Name:: "+self.arr[point][2]+"\nEmail ID:: "+self.arr[point][3]+"\nAddress:: "+self.arr[point][4]+"\nCountry:: "+self.arr[point][5]+"\nJob:: "+self.arr[point][6])
        else:
            messagebox.showinfo("PROBLEM", "The Name '"+self.ent.get()+"' cannot be Found")
            
        
        
ob=assignment()
ob.layout()   

