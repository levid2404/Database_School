import pyodbc

import tkinter as tk

cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=LAPTOP-HIA8FRN6;"
                      "Database=datatest;"
                      "Trusted_Connection=yes;")



print("1 : Show ALL Data")
print ("2 : Enter Data")
print("3 : Delete Data")
print("4: Search Data")
print("5: GUI/User Interface")
choice = input("Select Option ")
    
    
cursor = cnxn.cursor()

if choice == '1':
    cursor.execute('SELECT BoxID, LastName, Adres FROM personen')
    
    for table in cursor:
        print('row = %r' % (table,))


if choice == '2':
    BOXID = input("Enter box number ")
    NAME = input("Enter Last Name ")
    ADDRESS = input("Enter Address ")

    #converting into executable sql command
    working = "INSERT INTO Personen VALUES ({}, {}, {})".format(BOXID ,NAME, ADDRESS)
    
    cursor.execute(working)
    cursor.commit()
    

if choice == '3':
    BOXID2 = input("Enter Box Number which you want to delete from database ")
    working2 = "DELETE FROM Personen WHERE BoxID = {}".format(BOXID2)
    cursor.execute(working2)
    cursor.commit()
    print("Box Number {} has succesfully been deleted.".format(BOXID2))


if choice == '4':
    BOXID3 = input("Enter Last Name of customer: ")
    working3 = "SELECT * FROM Personen WHERE LastName = {}".format(BOXID3)
    cursor.execute(working3)
    for table in cursor:
        print('row = %r' % (table,))



if choice == '5':
    root = tk.Tk()
    root.title("Matta Database")
    label = tk.Label(root, text="BoxID")
    label.pack()
    entry = tk.Entry(root)
    label2 = tk.Label(root, text="Last Name")
    entry2 = tk.Entry(root)
    label2.pack()
    entry3 = tk.Entry(root)
    label3 = tk.Label(root, text="ADDRESS")
    label3.pack()
    entry.pack()
    entry2.pack()
    entry3.pack()
    
    def send():
        var1 = entry.get()
        var2 = entry2.get()
        var3 = entry3.get()
        working4 = "INSERT INTO Personen VALUES ({}, {}, {})".format(var1 ,var2, var3)
        print(working4)
        cursor.execute(working4)
        cursor.commit()
        popup = tk.Toplevel()
        labelp2 = tk.Label(popup, text="Added Succesfully.")
        labelp2.pack()
        buttonp2 = tk.Button(popup, text="Close", command=popup.destroy)
        buttonp2.pack()

    def delete():
        delete1 = entry4.get()
        working5 = "DELETE FROM Personen WHERE BoxID = {}".format(delete1)
        cursor.execute(working5)
        cursor.commit()
        popup = tk.Toplevel()
        labelp = tk.Label(popup, text="Deleted Succesfully.")
        labelp.pack()
        buttonp = tk.Button(popup, text="Close", command=popup.destroy)
        buttonp.pack()

    button = tk.Button(root, text="Add to Database", command=send)
    button.pack()

    label4 = tk.Label(root)
    entry4 = tk.Entry(root)
    entry4.pack()
    label4.pack()
    button2 = tk.Button(root, text="Delete from Database (enter boxnumber)", command=delete)
    button2.pack()
    
    root.mainloop()

 
    
