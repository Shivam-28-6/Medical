from colorama import Fore, Style
print("WELCOME TO MEDICAL MANAGEMENT SYSTEM\n\n")
Pass = input(Fore.LIGHTRED_EX + "Enter your sql password for user root:")
import mysql.connector
import datetime
import matplotlib.pyplot as plt
from tabulate import tabulate
mycursor = mysql.connector.connect(host="localhost", user="shivam", password=Pass, database="MSMSystem")
if mycursor:
    print("Connection successful")
else:
    print("Connection unsuccessful")
mycon = mycursor.cursor()
def meddata():
    print("PLEASE ENTER THE FOLLOWING DETAILS")
    idno = input("ENTER THE MEDICINE ID NUMBER: ")
    nm = input("ENTER THE MEDICINE NAME: ")
    manu = input("ENTER THE MANUFACTURER'S NAME: ")
    mdate = input("ENTER THE MANUFACTURE DATE(YYYY-MM-DD): ")
    edate = input("ENTER THE EXPIRY DATE(YYYY_MM_DD): ")
    ucost = input("ENTER THE COST PER UNIT: ")
    qstock = int(input("ENTER THE QUANTITY: "))
    qbalance = qstock
    qsold = qstock - qbalance
    mycon.execute("INSERT INTO Medicines(MedID,Medname,Manuf,ManDate,Expdate,Unit_cost,Quan_Stock,Quan_Sold,Quan_Balance) Values(%s,%s,%s,%s,%s,%s,%s,%s,%s)", (idno, nm, manu, mdate, edate, ucost, qstock, qsold, qbalance))
    mycursor.commit()
    if mycon:
        print(Fore.GREEN + nm, "ADDED TO THE TABLE")
    else:
        print(Fore.RED + nm, "NOT ADDED")
def accdata():
    print("PLEASE ENTER THE FOLLOWING DETAILS")
    idno = input("ENTER THE ACCESSORY ID NUMBER: ")
    nm = input("ENTER THE ACCESSORY NAME: ")
    manu = input("ENTER THE MANUFACTURER'S NAME: ")
    mdate = input("ENTER THE MANUFACTURE DATE(YYYY-MM-DD): ")
    ucost = input("ENTER THE COST PER UNIT: ")
    qstock = int(input("ENTER THE QUANTITY: "))
    qbalance = qstock
    qsold = qstock - qbalance
    mycon.execute("INSERT INTO Medical_Accessories(AccID,Accname,Manuf,ManDate,Unit_cost,Quan_Stock,Quan_Sold,Quan_Balance) Values(%s,%s,%s,%s,%s,%s,%s,%s)", (idno, nm, manu, mdate, ucost, qstock, qsold, qbalance))
    mycursor.commit()
    if mycon:
        print(Fore.GREEN + nm, "ADDED TO THE TABLE")
    else:
        print(Fore.RED + nm, "NOT ADDED")
def prodata():
    print("PLEASE ENTER THE FOLLOWING DETAILS")
    idno = input("ENTER THE MEDICINE ID NUMBER: ")
    nm = input("ENTER THE MEDICINE NAME: ")
    manu = input("ENTER THE MANUFACTURER'S NAME: ")
    mdate = input("ENTER THE MANUFACTURE DATE(YYYY-MM-DD): ")
    edate = input("ENTER THE EXPIRY DATE(YYYY_MM_DD): ")
    ucost = input("ENTER THE COST PER UNIT: ")
    qstock = int(input("ENTER THE QUANTITY: "))
    qbalance = qstock
    qsold = qstock - qbalance
    mycon.execute("INSERT INTO Health_Products(ProID,Proname,Manuf,ManDate,Expdate,Unit_cost,Quan_Stock,Quan_Sold,Quan_Balance) Values(%s,%s,%s,%s,%s,%s,%s,%s,%s)", (idno, nm, manu, mdate, edate, ucost, qstock, qsold, qbalance))
    mycursor.commit()
    if mycon:
        print(Fore.GREEN + nm, "ADDED TO THE TABLE")
    else:
        print(Fore.RED + nm, "NOT ADDED")
def disall():
 nm=str(input("Enter the table name whose details are to be displayed:"))
 sql='SELECT * FROM '+nm
 mycon.execute(sql)
 print(tabulate(mycon,headers=['ID','Name','Manufacturer','Manufacturing Date','Expiry Date','Cost','Stock','Sold','Balance'],tablefmt='fancy_grid'))
def disacc():
    sql = 'SELECT * FROM Medical_Accessories'
    mycon.execute(sql)
    print(tabulate(mycon,headers=['ID', 'Name', 'Manufacturer', 'Manufacturing Date', 'Cost', 'Stock', 'Sold', 'Balance'], tablefmt='fancy_grid'))
def disdis():
    sql = 'SELECT * FROM Dispose'
    mycon.execute(sql)
    print(tabulate(mycon, headers=['ID_No', 'Name', 'ExpDate', 'Amount_Disposed'], tablefmt='fancy_grid'))
def Search_by_Name():
    ph = input('\nENTER THE MEDICINE NAME TO SEARCH:')
    sql = "Select * from Medicines where MedName=%s"
    value = (ph, )
    mycon.execute(sql, value)
    rec= mycon.fetchone()
    if(rec==None):
        print(Fore.RED + ph,'IS NOT AVAILABLE')
    else:
        print(Fore.LIGHTGREEN_EX + "The Details are: ")
        print('BATCH NUMBER:\t',rec[0])
        print('MEDICINE NAME:\t',rec[1])
        print('MANUFACTURER:\t',rec[2])
        print('DATE OF MANUFACTURE:\t',rec[3])
        print('DATE OF EXPIRY:\t',rec[4])
        print('UNIT COST:\t',rec[5])
        print('QUANTITY STOCK:\t', rec[6])
        print('QUANTITY SOLD:\t', rec[7])
        print('QUANTITY BALANCE:\t', rec[8])
def Search_by_AccName():
    ph = input('\nENTER THE ACCESSORY NAME TO SEARCH:')
    sql = "Select * from medical_accessories where AccName=%s"
    value = (ph, )
    mycon.execute(sql, value)
    rec = mycon.fetchone()
    if(rec==None):
        print(Fore.RED + ph, 'IS NOT AVAILABLE')
    else:
        print(Fore.LIGHTGREEN_EX + "The Details are: ")
        print('BATCH NUMBER:\t', rec[0])
        print('MEDICINE NAME:\t', rec[1])
        print('MANUFACTURER:\t', rec[2])
        print('DATE OF MANUFACTURE:\t', rec[3])
        print('UNIT COST:\t', rec[4])
        print('QUANTITY STOCK:\t', rec[5])
        print('QUANTITY SOLD:\t', rec[6])
        print('QUANTITY BALANCE:\t', rec[7])
def Search_by_ProName():
    ph = input('\nENTER THE PRODUCT NAME TO SEARCH:')
    sql = "Select * from health_products where ProName=%s"
    value = (ph, )
    mycon.execute(sql, value)
    rec= mycon.fetchone()
    if(rec==None):
        print(Fore.RED + ph, 'IS NOT AVAILABLE')
    else:
        print(Fore.LIGHTGREEN_EX + "The Details are: ")
        print('BATCH NUMBER:\t',rec[0])
        print('MEDICINE NAME:\t',rec[1])
        print('MANUFACTURER:\t',rec[2])
        print('DATE OF MANUFACTURE:\t',rec[3])
        print('DATE OF EXPIRY:\t',rec[4])
        print('UNIT COST:\t',rec[5])
        print('QUANTITY STOCK:\t',rec[6])
        print('QUANTITY SOLD:\t', rec[7])
        print('QUANTITY BALANCE:\t', rec[8])
def Search_by_Manuf():
    ph = input('\nENTER THE MANUFACTURER\'S NAME TO SEARCH:')
    sql = "Select * from Medicines where Manuf=%s"
    value = (ph, )
    mycon.execute(sql, value)
    rec= mycon.fetchone()
    if(rec==None):
        print(Fore. LIGHTRED_EX + ph, 'IS NOT AVAILABLE')
    else:
        print(Fore.LIGHTGREEN_EX + "The Details are: ")
        print('BATCH NUMBER:\t',rec[0])
        print('MEDICINE NAME:\t',rec[1])
        print('MANUFACTURER:\t',rec[2])
        print('DATE OF MANUFACTURE:\t',rec[3])
        print('DATE OF EXPIRY:\t',rec[4])
        print('UNIT COST:\t',rec[5])
        print('QUANTITY STOCK:\t',rec[6])
        print('QUANTITY SOLD:\t', rec[7])
        print('QUANTITY BALANCE:\t', rec[8])
def Search_by_AccManuf():
    ph = input('\nENTER THE MANUFACTURER TO SEARCH:')
    sql = "Select * from medical_accessories where Manuf=%s"
    value = (ph, )
    mycon.execute(sql, value)
    rec = mycon.fetchone()
    if(rec==None):
        print(Fore.LIGHTRED_EX + ph, 'IS NOT AVAILABLE')
    else:
        print(Fore.LIGHTGREEN_EX + "The Details are: ")
        print('BATCH NUMBER:\t', rec[0])
        print('MEDICINE NAME:\t', rec[1])
        print('MANUFACTURER:\t', rec[2])
        print('DATE OF MANUFACTURE:\t', rec[3])
        print('UNIT COST:\t', rec[4])
        print('QUANTITY STOCK:\t', rec[5])
        print('QUANTITY SOLD:\t', rec[6])
        print('QUANTITY BALANCE:\t', rec[7])
def Search_by_ProManuf():
    ph = input('\nENTER THE MANUFACTURER\'S NAME TO SEARCH:')
    sql = "Select * from Health_Products where Manuf=%s"
    value = (ph, )
    mycon.execute(sql, value)
    rec= mycon.fetchone()
    if(rec==None):
        print(Fore.LIGHTRED_EX + ph, 'IS NOT AVAILABLE')
    else:
        print(Fore.LIGHTGREEN_EX + "The Details are: ")
        print('BATCH NUMBER:\t',rec[0])
        print('MEDICINE NAME:\t',rec[1])
        print('MANUFACTURER:\t',rec[2])
        print('DATE OF MANUFACTURE:\t',rec[3])
        print('DATE OF EXPIRY:\t',rec[4])
        print('UNIT COST:\t',rec[5])
        print('QUANTITY STOCK:\t',rec[6])
        print('QUANTITY SOLD:\t', rec[7])
        print('QUANTITY BALANCE:\t', rec[8])
def Cost_medupd():
    sql="Update Medicines set Unit_Cost= %s where MedName = %s"
    ph=input('\nENTER THE MEDICINE NAME TO CHANGE COST:')
    addr= int(input('\nENTER THE NEW COST PER UNIT:'))
    value = (addr, ph)
    try:
        mycon.execute(sql, value)
        mycursor.commit()
        print(Fore.MAGENTA + 'NEW COST OF', ph, 'IS = RS.', addr)
    except:
        print(Fore.RED + 'UNABLE TO CHANGE COST!!!!')
    if mycon:
        print(Fore.MAGENTA + "SUCCESSFUL!!\nTHANK YOU\n")
    else:
        print(Fore.RED + "UNABLE TO UPDATE!")
def Cost_accupd():
    sql="Update Medical_Accessories set Unit_Cost= %s where AccName = %s"
    ph=input('\nENTER THE ACCESSORY NAME TO CHANGE COST:')
    addr= int(input('\nENTER THE NEW COST PER UNIT:'))
    value = (addr, ph)
    try:
        mycon.execute(sql, value)
        mycursor.commit()
        print(Fore.MAGENTA + 'NEW COST OF', ph, 'IS = RS.', addr)
    except:
        print(Fore.RED + 'UNABLE TO CHANGE COST!!!!')
    if mycon:
        print(Fore.MAGENTA + "SUCCESSFUL!!\nTHANK YOU\n")
    else:
        print(Fore.RED + "UNABLE TO UPDATE!")
def Cost_proupd():
    sql="Update health_products set Unit_Cost= %s where ProName = %s"
    ph=input('\nENTER THE PRODUCT NAME TO CHANGE COST:')
    addr= int(input('\nENTER THE NEW COST PER UNIT:'))
    value = (addr, ph)
    try:
        mycon.execute(sql, value)
        mycursor.commit()
        print(Fore.MAGENTA + 'NEW COST OF', ph, 'IS = RS.', addr)
    except:
        print(Fore.RED + 'UNABLE TO CHANGE COST!!!!')
    if mycon:
        print(Fore.MAGENTA + "SUCCESSFUL!!\nTHANK YOU\n")
    else:
        print(Fore.RED + "UNABLE TO UPDATE!")
def Sellmed():
    sql = "Update Medicines set Quan_Sold=%s,Quan_Balance=%s where MedName=%s"
    ph = input('\nENTER THE MEDICINE NAME TO SELL:')
    addr = int(input('\nENTER THE QUANTITY TO SELL:'))
    sql2 = 'select Quan_Balance,Quan_Sold,Unit_Cost from Medicines where MedName=%s'
    value2 = (ph,)
    mycon.execute(sql2, value2)
    rec = mycon.fetchone()
    sold = rec[1]
    no = rec[2]
    if (addr > rec[0]):
        print('INSUFFICIENT STOCK IN HAND!!!!!!')
        return
    else:
        balance = rec[0] - addr
        value = (addr + sold, balance, ph)
        try:
            mycon.execute(sql, value)
            mycursor.commit()
            print(addr, 'UNITS OF', ph, 'SOLD')
            print(balance, 'UNITS LEFT')
            print("THE TOTAL COST OF MEDICINES SOLD IS RS.", no * addr)
        except:
            print('UNABLE TO SELL MEDICINE!!!!')
def Sellacc():
    sql = "Update Medical_Accessories set Quan_Sold=%s,Quan_Balance=%s where AccName=%s"
    ph = input('\nENTER THE ACCESSORY NAME TO SELL:')
    addr = int(input('\nENTER THE QUANTITY TO SELL:'))
    sql2 = 'select Quan_Balance,Quan_Sold,Unit_Cost from Medical_Accessories where AccName=%s'
    value2 = (ph,)
    mycon.execute(sql2, value2)
    rec = mycon.fetchone()
    sold = rec[1]
    no = rec[2]
    if (addr > rec[0]):
        print('INSUFFICIENT STOCK IN HAND!!!!!!')
        return
    else:
        balance = rec[0] - addr
        value = (addr + sold, balance, ph)
        try:
            mycon.execute(sql, value)
            mycursor.commit()
            print(addr, 'UNITS OF', ph, 'SOLD')
            print(balance, 'UNITS LEFT')
            print("THE TOTAL COST OF ACCESSORIES SOLD IS RS.", no * addr)
        except:
            print('UNABLE TO SELL ACCESSORY!!!!')
def Sellpro():
    sql = "Update Health_Products set Quan_Sold=%s,Quan_Balance=%s where ProName=%s"
    ph = input('\nENTER THE PRODUCT NAME TO SELL:')
    addr = int(input('\nENTER THE QUANTITY TO SELL:'))
    sql2 = 'select Quan_Balance,Quan_Sold,Unit_Cost from Health_Products where ProName=%s'
    value2 = (ph,)
    mycon.execute(sql2, value2)
    rec = mycon.fetchone()
    sold = rec[1]
    no = rec[2]
    if (addr > rec[0]):
        print('INSUFFICIENT STOCK IN HAND!!!!!!')
        return
    else:
        balance = rec[0] - addr
        value = (addr + sold, balance, ph)
        try:
            mycon.execute(sql, value)
            mycursor.commit()
            print(addr, 'UNITS OF', ph, 'SOLD')
            print(balance, 'UNITS LEFT')
            print("THE TOTAL COST OF PRODUCTS SOLD IS RS.", no * addr)
        except:
            print('UNABLE TO SELL PRODUCT!!!!')
def graphmed():
    nm = input('Enter the medicine name:')
    sql='Select * from Medicines where MedName=%s'
    value = (nm,)
    mycon.execute(sql, value)
    a = mycon.fetchone()
    b = [a[6], a[7], a[8]]
    c = ['Stock', 'Sold', 'Balance']
    d = ('green', 'red', 'blue')
    print(a[7], ' units of ',nm, ' have been sold!!')
    plt.bar(c, b, color=d)
    plt.xlabel('Medicine Stats')
    plt.ylabel('Values')
    plt.title('GRAPHICAL REPRESENTATION')
    plt.show()
def graphacc():
    nm = input('Enter the medicine name:')
    sql='Select * from Medical_Accessories where AccName=%s'
    value = (nm,)
    mycon.execute(sql, value)
    a = mycon.fetchone()
    b = [a[5], a[6], a[7]]
    c = ['Stock', 'Sold', 'Balance']
    d = ('green', 'red', 'blue')
    plt.bar(c, b, color=d)
    plt.xlabel('Accessory Stats')
    plt.ylabel('Values')
    plt.title('GRAPHICAL REPRESENTATION')
    plt.show()
def graphpro():
    nm = input('Enter the product name:')
    sql='Select * from Health_Products where ProName=%s'
    value = (nm,)
    mycon.execute(sql, value)
    a = mycon.fetchone()
    b = [a[6], a[7], a[8]]
    c = ['Stock', 'Sold', 'Balance']
    d = ('green', 'red', 'blue')
    plt.bar(c, b, color=d)
    plt.xlabel('Medicine Stats')
    plt.ylabel('Values')
    plt.title('GRAPHICAL REPRESENTATION')
    plt.show()
def delmed():
    nm = input("ENTER THE NAME OF A MEDICINE TO BE DISPOSED: ")
    dl2 = "Select MedID, MedName, Expdate, Quan_Balance from Medicines where MedName = %s and %s >= ExpDate"
    dt = datetime.date.today()
    vl2 = (nm, dt)
    mycon.execute(dl2, vl2)
    dis = mycon.fetchone()
    if dis is not None:
        i = dis[0]
        n = dis[1]
        ed = dis[2]
        ad = dis[3]
        mycon.execute("INSERT INTO Dispose(ID_No, Name, ExpDate, Amount_Disposed)values(%s, %s, %s, %s)",
                      (i, n, ed, ad))
        mycursor.commit()
        p = int(input(Fore.BLUE + "PLEASE PRESS 1 TO PROCEED AND DISPOSE - "))
        if p == 1:
            mycon.execute("DELETE From Medicines Where MedName = %s", (nm,))
            mycursor.commit()
            if mycon:
                print(Fore.LIGHTBLUE_EX + "THE MEDICINE IS EXPIRED AND DISPOSED.")
            else:
                print(Fore.LIGHTRED_EX + "UNABLE TO DISPOSE THE MEDICINE!")
        else:
            print("PROGRAM CLOSED")
    else:
        print(Style.BRIGHT + Fore.GREEN + "THE MEDICINE IS NOT EXPIRED!")
    mycursor.commit()
def delpro():
    nm = input("ENTER THE NAME OF A PRODUCT TO BE DISPOSED: ")
    dl2 = "Select ProID, ProName, Expdate, Quan_Balance from Health_Products where ProName = %s and %s >= ExpDate"
    dt = datetime.date.today()
    vl2 = (nm, dt)
    mycon.execute(dl2, vl2)
    dis = mycon.fetchone()
    if dis is not None:
        i = dis[0]
        n = dis[1]
        ed = dis[2]
        ad = dis[3]
        mycon.execute("INSERT INTO Dispose(ID_No, Name, ExpDate, Amount_Disposed)values(%s, %s, %s, %s)",
                      (i, n, ed, ad))
        mycursor.commit()
        p = int(input(Fore.BLUE + "PLEASE PRESS 1 TO PROCEED AND DISPOSE - "))
        if p == 1:
            mycon.execute("DELETE From Health_Products Where ProName = %s", (nm,))
            mycursor.commit()
            if mycon:
                print(Fore.LIGHTBLUE_EX + "THE PRODUCT IS EXPIRED AND DISPOSED.")
            else:
                print(Fore.LIGHTRED_EX + "UNABLE TO DISPOSE THE PRODUCT!")
        else:
            print("PROGRAM CLOSED")
    else:
        print(Style.BRIGHT + Fore.BLUE + "THE PRODUCT IS NOT EXPIRED!")
    mycursor.commit()
def sdispose():
    print("The Dispose Medicines are: ")
    s = "Select Name from Dispose"
    mycon.execute(s)
    r=mycon.fetchall()
    for i in r:
        print(i)
    nm = input("ENTER THE NAME TO DISPLAY DETAILS: ")
    inp = (nm,)
    op = "Select * from Dispose where Name = %s"
    mycon.execute(op, inp)
    op = mycon.fetchall()
    if op == None:
       print(Fore.RED + nm, "DOES NOT EXIST!")
    else:
        for r in op:
            print("ID: ", r[0])
            print("NAME: ", r[1])
            print("EXPIRY DATE: ", r[2])
            print("QUANTITY DISPOSED: ", r[3])
def close():
    print(Style.BRIGHT + Fore.GREEN + "THANK YOU FOR USING THIS SYSTEM! ")
    print(Style.BRIGHT + Fore.GREEN + "SUCCESSFULLY CLOSED!")
    quit()
while (True):
    print('-----------------------------------------------------------------------------')
    print(Fore.MAGENTA + Style.BRIGHT + 'WELCOME TO THE MENU!')
    print('1. Add New Data')
    print('2. Displaying all records:')
    print('3. Search by name')
    print('4. Search by manufacturer')
    print('5. Updating the cost')
    print('6. Sell')
    print('7. Graph of the sales')
    print('8. Delete the expired medicines')
    print('9. Search in the dispose table')
    print('10. Close the program')
    print('------------------------------------------------------------------------------')
    nm=int(input(Fore.BLUE + 'Enter the corresponding value of process to be performed:- '))
    print('------------------------------------------------------------------------------')
    if nm==1:
        print('------------------------------')
        print('Press 1 to add new medicine')
        print('Press 2 to add new accessory')
        print('Press 3 to add new product')
        print('------------------------------')
        choice=int(input(Fore.BLUE + 'Enter your choice: '))
        print('------------------------------')
        if choice==1:
            meddata()
        elif choice==2:
            accdata()
        else:
            prodata()
    if nm==2:
        print('\n')
        print("Press 1 to display Medicines and Health_Products")
        print("Press 2 to display Medical_Accessories")
        print("Press 3 to display Dispose")
        print('-------------------------------------------------')
        choice=int(input(Fore.BLUE + "Enter your choice: "))
        if choice==1:
            disall()
        if choice==2:
            disacc()
        if choice==3:
            disdis()

    if nm==3:
        print('\n')
        print('Press 1 to search a medicine by name')
        print('Press 2 to search a accessory by name')
        print('Press 3 to search a product by name')
        print('--------------------------------------')
        choice = int(input(Fore.BLUE + 'Enter your choice'))
        if choice==1:
            Search_by_Name()
        elif choice==2:
            Search_by_AccName()
        else:
            Search_by_ProName()
    if nm==4:
        print('\n')
        print('Press 1 to search a medicine by a manufacturer')
        print('Press 2 to search a accessory by manufacturer')
        print('Press 3 to search a product by manufacturer')
        print('----------------------------------------------')
        choice = int(input(Fore.BLUE + 'Enter your choice'))
        if choice==1:
            Search_by_Manuf()
        elif choice==2:
            Search_by_AccManuf()
        else:
            Search_by_ProManuf()
    if nm==5:
        print('\n')
        print('Press 1 to update the cost of a medicine')
        print('Press 2 to update the cost of a accessory')
        print("Press 3 to update the cost of the product")
        print('-------------------------------------------')
        choice = int(input(Fore.BLUE + 'Enter your choice: '))
        if choice==1:
            Cost_medupd()
        elif choice==2:
            Cost_accupd()
        else:
            Cost_proupd()
    if nm==6:
        print('\n')
        print('Press 1 to sell Medicines')
        print('Press 2 to sell Accessories')
        print('Press 3 to sell Products')
        print('-----------------------------')
        choice = int(input(Fore.BLUE + 'Enter your Choice: '))
        if choice ==1:
            Sellmed()
        elif choice==2:
            Sellacc()
        else:
            Sellpro()
    if nm==7:
        print('\n')
        print("Press 1 for the sales of Medicines")
        print("Press 2 for the sales of Medical Accessories")
        print("Press 3 for the sales of Health Products")
        print('----------------------------------------------')
        choice = int(input(Fore.BLUE + "Enter your choice: "))
        if choice==1:
            graphmed()
        elif choice==2:
            graphacc()
        else:
            graphpro()
    if nm==8:
        print('\n')
        print('Press 1 to delete medicine from Medicines table')
        print('Press 2 to delete products from Health Products table')
        print('--------------------------------------------------------')
        choice = int(input(Fore.BLUE + 'Enter your choice'))
        if choice==1:
         delmed()
        if choice==2:
         delpro()
    if nm==9:
        print('\n')
        print(Fore.BLUE + "Search in Dispose initiated!")
        sdispose()
    if nm==10:
        close()
