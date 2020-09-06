# importing required modules
from tkinter import *
from tkinter import simpledialog
import mysql.connector

# Front end UI Drsign

class Employee:
    def __init__(self, root):

        p = Database
        p.conn(self)


        self.root = root
        self.root.title('EMPOLYEE DATABASE MANAGEMENT')
        self.root.geometry('1180x650')
        self.root.config(bg = 'orange')

        # Frames for UI 
        # This is main frame of application 
        MainFrame  = Frame(self.root, bg = 'orange')
        MainFrame.grid()
        
        # This is the Title frame
        TitleFrame = Frame(MainFrame, bd = 2, padx = 60, pady = 20, bg = 'yellow', relief = RIDGE)
        TitleFrame.pack(side = TOP)
        
        self.ITitle = Label(TitleFrame, font = ('times', 40, 'bold'), text = ' EMPLOYEES DATABASE MANAGEMENT ', fg = 'green', bg = 'yellow')
        self.ITitle.grid()
        
   

        # This is the Data frame
        DataFrame = Frame(MainFrame, bd = 2, width = 1200, height = 80, padx = 60, pady = 20, bg = 'lightblue')
        DataFrame.pack()
        
        DataLabelFrame = LabelFrame(DataFrame, bd = 2, width = 800, height = 400, font = ('times', 12, 'bold'), text = '  VIEW EMPLOYEES DEATAILS  ')
        DataLabelFrame.pack(side = LEFT)

        # Adding listbox and scroll bar to tha data frame
        scroll = Scrollbar(DataLabelFrame)
        scroll.grid(row = 0, column = 1, sticky = 'ns')

        DataList = Listbox(DataLabelFrame, width = 150, height = 20, yscrollcommand = scroll.set)
        DataList.grid(row = 0, column = 0)
        scroll.config(command = DataList.yview)


        # This is the options frame  
        OptionFrame = Frame(MainFrame, bd = 2, width = 1200, height = 50, padx = 60, pady = 20, bg = 'red', relief = RIDGE)
        OptionFrame.pack(side = BOTTOM)
        
        # These are the button functions

        # This function is for formatting the strings before insetion to listbox
        def format(emp_id, emp_name, emp_sal, emp_dept, emp_email):
            idStr = "EMPLOYEE ID: {0}".format(emp_id)
            nameStr = "EMPLOYEE NAME: {0}".format(emp_name)
            saleryStr = "EMPLOYEE SALERY: {0}".format(emp_sal)
            deptStr = "EMPLOYEE DEPARTMENT: {0}".format(emp_dept)
            emailStr = "EMPLOYEE EMAIL: {0}".format(emp_email)
            return(idStr, nameStr, saleryStr, deptStr, emailStr)

        # This function is to add data to the listbox 
        def add():
            emp_id = simpledialog.askinteger('INPUT ID', ' PLEASE ENTER EMPLOYEE ID')
            emp_name = simpledialog.askstring('INPUT NAME', 'PLEASE ENTER EMPLOYEE NAME')
            emp_sal = simpledialog.askinteger('INPUT SALERY', 'PLEASE ENTER EMPLOYEE SALERY')
            emp_dept = simpledialog.askstring('INPUT DEPARMENT', 'PLEASE ENTER EMPLOYEE DEPARTMENT')
            emp_email = simpledialog.askstring('INPUT EMAIL', 'PLEASE ENTER EMPLOYEE EMAIL')
            p.insert(emp_id, emp_name, emp_sal, emp_dept, emp_email)
            DataList.delete(0, END)
            idStr, nameStr, saleryStr, deptStr, emailStr = format(emp_id, emp_name, emp_sal, emp_dept, emp_email)
            DataList.insert(END, idStr, nameStr, saleryStr, deptStr, emailStr)
            DataList.insert(END, '!!!!!!!!!THIS USER DATA ADDED SUCCESSFULLY!!!!!!!!!')
            print('finished1')


        #This function is for show data to listbox
        def get():
            emp_id = simpledialog.askinteger('INPUT ID', ' PLEASE ENTER EMPLOYEE ID')
            rows = p.get(emp_id)
            DataList.delete(0, END)
            emp_id = rows[0][0]
            emp_name = rows[0][1]
            emp_sal = rows[0][2]
            emp_dept = rows[0][3]
            emp_email = rows[0][4]
            idStr, nameStr, saleryStr, deptStr, emailStr = format(emp_id, emp_name, emp_sal, emp_dept, emp_email)
            DataList.insert(END, idStr, nameStr, saleryStr, deptStr, emailStr)
            return(emp_id)

        #This function is to delete data and show the deleted message
        def delete():
            DataList.delete(0,END)
            emp_id = simpledialog.askinteger('INPUT ID', ' PLEASE ENTER EMPLOYEE ID WHOSE RECORD NEEDS TO BE DELETED')
            p.delete(emp_id)
            delId = "!!!!!!!!!!EMPLOYEE ID: {0} HAS BEEN REMOVED SUCCESSFULLY!!!!!!!".format(emp_id)
            DataList.insert(END, delId)

        #This function is for showing all the current records
        def show():
            DataList.delete(0, END)
            DataList.insert(END, 'EMPID  EMPNAME  EMPSAL  EMPDEPT EMPEMAIL')
            record = p.show()
            for i in record:
                DataList.insert(END, i)

        #This function is for showing data between salery range
        def salery():
            DataList.delete(0, END)
            MinSal = simpledialog.askinteger('INPUT MINIMUM SALERY', ' PLEASE ENTER MINIMUM SALERY OF EMPLOYEES')
            MaxSal = simpledialog.askinteger('INPUT MAXIMUM SALERY', ' PLEASE ENTER MAXIMUM SALERY OF EMPLOYEES')
            DataList.insert(END, 'EMPID  EMPNAME  EMPSAL  EMPDEPT EMPEMAIL')
            record = p.salery(MinSal, MaxSal)
            for i in record:
                DataList.insert(END, i)

        #This function is for updating the salery of any employee
        def update():
            emp_id = get()
            SetSal = simpledialog.askinteger('INPUT SALERY', 'PLEASE ENTER EMPLOYEE SALERY TO BE UPDATED')
            if SetSal < 0:
                SetSal = simpledialog.askinteger('INPUT SALERY', 'ERROR....PLEASE ENTER SALERY GRATER THAN 0')
            p.update(emp_id, SetSal)
            rows = p.get(emp_id)
            DataList.insert(END, 'THE UPDATED EMPLOYEE DETAILS ARE:')
            emp_id = rows[0][0]
            emp_name = rows[0][1]
            emp_sal = rows[0][2]
            emp_dept = rows[0][3]
            emp_email = rows[0][4]
            idStr, nameStr, saleryStr, deptStr, emailStr = format(emp_id, emp_name, emp_sal, emp_dept, emp_email)
            DataList.insert(END, idStr, nameStr, saleryStr, deptStr, emailStr)


        # Now adding button to our option frame
        self.buttonAdd = Button(OptionFrame, text = 'ADD', font = ('times', 12, 'bold'), height= 2, width = 8, bd = 4, bg = 'lightgreen',  command = add)
        self.buttonAdd.grid(row = 0, column = 0)

        self.buttonDelete = Button(OptionFrame, text = 'DELETE', font = ('times', 12, 'bold'), height= 2, width = 8, bd = 4, bg = 'lightgreen', command = delete)
        self.buttonDelete.grid(row = 0, column = 1)

        self.buttonUpdate = Button(OptionFrame, text = 'UPDATE', font = ('times', 12, 'bold'), height= 2, width = 8, bd = 4, bg = 'lightgreen', command = update)
        self.buttonUpdate.grid(row = 0, column = 2)

        self.buttonShow = Button(OptionFrame, text = 'SHOW', font = ('times', 12, 'bold'), height= 2, width = 8, bd = 4, bg = 'lightgreen', command = show)
        self.buttonShow.grid(row = 0, column = 3)

        self.buttonGet = Button(OptionFrame, text = 'GET', font = ('times', 12, 'bold'), height= 2, width = 8, bd = 4, bg = 'lightgreen', command = get)
        self.buttonGet.grid(row = 0, column = 4)

        self.buttonSalery = Button(OptionFrame, text = 'SALERY', font = ('times', 12, 'bold'), height= 2, width = 8, bd = 4, bg = 'lightgreen', command = salery)
        self.buttonSalery.grid(row = 0, column = 5)


#This class is for the backend database operations
class Database:
    def conn(self):
        con = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'abhinav11', database = 'employee')
        cur = con.cursor()
        query = "CREATE TABLE if not exists emp (empid int NOT NULL UNIQUE, empname varchar(45), empsal BIGINT, empdept varchar(45), empemail varchar(60))"
        cur.execute(query)
        con.commit()
        con.close()
        print('finished')


    def insert(emp_id, emp_name, emp_sal, emp_dept, emp_email):
        con = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'abhinav11', database = 'employee')
        cur = con.cursor()
        query = "insert into employee.emp (empid, empname, empsal, empdept, empemail) values (%s, %s, %s, %s, %s)"
        cur.execute(query, (emp_id, emp_name, emp_sal, emp_dept, emp_email))
        con.commit()
        con.close()
        print('finished')

    def get(emp_id):
        con = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'abhinav11', database = 'employee')
        cur = con.cursor()  
        query = "SELECT * FROM employee.emp where empid = %s"
        cur.execute(query, (emp_id,))
        rows = cur.fetchall()
        con.commit()
        con.close()
        print('finished')
        return(rows)


    def delete(emp_id):
        con = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'abhinav11', database = 'employee')
        cur = con.cursor()
        query = "delete from employee.emp where empid = %s"
        cur.execute(query, (emp_id,))
        con.commit()
        con.close()
        print('finished')
        


    def show():
        con = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'abhinav11', database = 'employee')
        cur = con.cursor()
        query = "SELECT * FROM employee.emp"
        cur.execute(query)
        record = cur.fetchall()
        con.commit()
        con.close()
        print('finished')
        return(record)


    def salery(MinSal, MaxSal):
        con = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'abhinav11', database = 'employee')
        cur = con.cursor()
        query = "SELECT * FROM employee.emp where empsal >= %s and empsal <= %s"
        cur.execute(query, (MinSal, MaxSal))
        record = cur.fetchall()
        con.commit()
        con.close()
        print('finished')
        return(record)



    def update(emp_id, SetSal):
        con = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'abhinav11', database = 'employee')
        cur = con.cursor()  
        query = "UPDATE employee.emp SET empsal = %s WHERE empid = %s"
        cur.execute(query, (SetSal, emp_id))
        con.commit()
        con.close()
        print('finished')    


if __name__ == "__main__":
    root = Tk()
    application = Employee(root)
    root.mainloop()