from tkinter import *
from tkinter import messagebox
from data_base import *
from validation import *
def home_console():
                root = Tk()
                root.title("Admin Console")
                root.geometry("300x200")
                my_label = Label(root, text="Welcome To Employee Management System!").pack()
                my_label = Label(root, text="Login as:").pack()
                frame = LabelFrame(root , text="ADMIN").pack(padx=10,pady=10)
                emp_creation = Button(frame, text = "ADMIN",command = Adminlogin).pack()
                frame = LabelFrame(root , text="Employee", padx=5, pady=5).pack(padx=10,pady=10)
                list_of_emp = Button(frame, text = "Employee",command=Employeelogin).pack()
                root.mainloop()
def adminvalidation():
                username = user_entry.get()
                password = pass_entry.get()
                if username == 'root' and password == 'root':
                    adminconsole()
                else:
                    messagebox.showwarning('Login Page', 'The username or password you entered is incorrect')
def employeevalidation():
                username = user_entry.get()
                password = pass_entry.get()
                data=read_table("emp_creation_table")
                dic={}
                for i in data:
                    dic[i[2]]=i[4]
                if username in dic.keys():
                    if password == dic[username]:
                        loginconsole()
                    else:
                        messagebox.showwarning('Login Page', 'The username or password you entered is incorrect')
                else:
                    messagebox.showwarning('Login Page', 'The username or password you entered is incorrect')
                
def adminconsole():
                    root = Tk()
                    root.title("Admin Console")
                    button = Button(root, text = 'Create Employee Account',command=create_employee_page)
                    button.grid(row=2, column=0, columnspan=2)
                    button = Button(root, text = 'List Employee Details',command=admin_list_emp_details_page)
                    button.grid(row=4, column=0, columnspan=2)
                    button = Button(root, text = 'Employee Leave Requests',command=admin_emp_leave_request_page)
                    button.grid(row=6, column=0, columnspan=2)
                    button = Button(root, text = 'Account Deletion',command=admin_emp_account_del_page)
                    button.grid(row=8, column=0, columnspan=2)
                    root.mainloop()
def loginconsole():
                    root = Tk()
                    root.title("employee Console")
                    button = Button(root, text = 'search for employee',command=employee_emp_search_page)
                    button.grid(row=2, column=0, columnspan=2)
                    button = Button(root, text = 'leave request',command=employee_leave_request_page)
                    button.grid(row=4, column=0, columnspan=2)
                    button = Button(root, text = 'change password ',command=employee_change_password_page)
                    button.grid(row=6, column=0, columnspan=2)
                    root.mainloop()
def Adminlogin():
            global user_entry,pass_entry
            root = Tk(className = 'Admin Login')
            Label(root, text='Username').grid(row=0)
            Label(root, text='Password').grid(row=1)
            user_entry = Entry(root)
            pass_entry = Entry(root,show="*")
            user_entry.grid(row=0, column=1)
            pass_entry.grid(row=1, column=1)
            button = Button(root, text = 'submit',command=adminvalidation)
            button.grid(row=2, column=0, columnspan=2)
            root.mainloop()
def Employeelogin():
            global user_entry,pass_entry
            root = Tk(className = 'Employee Login')
            Label(root, text='Username').grid(row=0)
            Label(root, text='Password').grid(row=1)
            user_entry = Entry(root)
            pass_entry = Entry(root,show="*")
            user_entry.grid(row=0, column=1)
            pass_entry.grid(row=1, column=1)
            button = Button(root, text = 'submit',command=employeevalidation)
            button.grid(row=2, column=0, columnspan=2)
            root.mainloop()
def create_employee_database():
    firstname=firstname_entry.get()
    lastname=lastname_entry.get()
    a1=emp_usernamevalidation(firstname,lastname)
    username=userid_entry.get()
    a2=emp_useridvalidation(username)
    email_id=emailid_entry.get()
    a3=emp_emailvalidation(email_id)
    password=password_entry.get()
    a4=emp_passwordvalidation(password)
    emp_salary=salary_entry.get()
    a5=emp_salaryvalidation(emp_salary)
    emp_pf_no=pfno_entry.get()
    a6=emp_pfno_validation(emp_pf_no)
    join_Date=joindate_entry.get()
    a8=date_validation(join_Date)
    pan_no=panid_entry.get()
    a7=emp_pfno_validation(pan_no)
    print(a1,a2,a3,a4,a5,a6,a7,a8)
    dic={"first_name":firstname,"last_name":lastname,"username":username,"email_id":email_id,"password":password,
             "emp_salary":emp_salary,"emp_pf_no":emp_pf_no,"join_Date":join_Date,"pan_no":pan_no,"leave_balance":6}
    insert_row("Emp_Creation_Table",dic)
    root = Tk()
    root.title("employee creation")
    root.geometry("400x300")
    if (a1==True) and (a2==True) and (a3==True) and (a4==True) and (a5==True) and (a6==True) and (a7==True) and (a8==True):
        my_label = Label(root, text="employee details are created ").pack()
        
def create_employee_page():
            global firstname_entry,lastname_entry,userid_entry,emailid_entry,password_entry,salary_entry,pfno_entry,joindate_entry,panid_entry
            root = Tk(className = 'employee creation page')
            Label(root, text='firstname').grid(row=0)
            Label(root, text='lastname').grid(row=1)
            Label(root, text='userid').grid(row=2)
            Label(root, text='emailid').grid(row=3)
            Label(root, text='password').grid(row=4)
            Label(root, text='salary').grid(row=5)
            Label(root, text='pfno').grid(row=6)
            Label(root, text='joindate').grid(row=7)
            Label(root, text='panid').grid(row=8)
            
            firstname_entry = Entry(root)
            lastname_entry = Entry(root)
            userid_entry = Entry(root)
            emailid_entry = Entry(root)
            password_entry = Entry(root)
            salary_entry = Entry(root)
            pfno_entry = Entry(root)
            joindate_entry = Entry(root)
            panid_entry = Entry(root)
            
            firstname_entry.grid(row=0, column=1)
            lastname_entry.grid(row=1, column=1)
            userid_entry.grid(row=2, column=1)
            emailid_entry.grid(row=3, column=1)
            password_entry.grid(row=4, column=1)
            salary_entry.grid(row=5, column=1)
            pfno_entry.grid(row=6, column=1)
            joindate_entry.grid(row=7, column=1)
            panid_entry.grid(row=8, column=1)
            
            button = Button(root, text = 'submit',command=create_employee_database)
            button.grid(row=9, column=0, columnspan=2)
            root.mainloop()
def admin_list_emp_details_page():
                global username_entry
                root = Tk(className = 'employee details')
                Label(root, text='Username').grid(row=0)
                username_entry = Entry(root)
                username_entry.grid(row=0, column=1)
                button = Button(root, text = 'submit',command=admin_list_emp_details)
                button.grid(row=9, column=0, columnspan=2)
                root.mainloop()
def admin_list_emp_details():
    username=username_entry.get()
    list=["first_name","last_name","username","email_id","password",
             "emp_salary","emp_pf_no","join_Date","pan_no","leave_balance"]
    if username:
        Data_dic=read_table("emp_creation_table",username)
        root = Tk()
        root.title("employee datails")
        root.geometry("400x300")
        my_label = Label(root, text="empoyee datails are!").pack()
        for i in range(len(list)):
            my_label = Label(root, text=f"{list[i]} : {Data_dic[0][i]}").pack()
    else:
        all_emp_details=read_table("emp_creation_table")
        root = Tk()
        root.title("employee datails")
        root.geometry("400x300")
        my_label = Label(root, text="all empoyee datails are!").pack()
        for i in range(len(all_emp_details)):
            for j in range(len(list)):
                my_label = Label(root, text=f"{list[j]} : {all_emp_details[i][j]}").pack()
            my_label = Label(root, text="*"*50).pack()
def admin_emp_leave_request_page():
                global user_name_entry,status_entry
                root = Tk(className = 'emp leave request')
                Label(root, text='Username').grid(row=0)
                Label(root, text='status').grid(row=1)
                user_name_entry = Entry(root)
                status_entry = Entry(root)
                user_name_entry.grid(row=0, column=1)
                status_entry.grid(row=1, column=1)
                button = Button(root, text = 'submit',command=admin_emp_leave_request)
                button.grid(row=9, column=0, columnspan=2)
                root.mainloop()
def admin_emp_leave_request():
    username=user_name_entry.get()
    status=status_entry.get()
    update_table("Leave_Request_Table",username,'status',status)
    root = Tk()
    root.title("leave request")
    root.geometry("400x300")
    my_label = Label(root, text="employee leave request is updated").pack()
def admin_emp_deletion():
    user=username_delete_entry.get()
    delete_row("emp_creation_table",user)
    root = Tk()
    root.title("employee deletion")
    root.geometry("400x300")
    my_label = Label(root, text="employee details are deleted ").pack()
def admin_emp_account_del_page():
                global username_delete_entry
                root = Tk(className = 'employee deletion')
                Label(root, text='Username').grid(row=0)
                username_delete_entry = Entry(root)
                username_delete_entry.grid(row=0, column=1)
                button = Button(root, text = 'submit',command=admin_emp_deletion)
                button.grid(row=9, column=0, columnspan=2)
                root.mainloop()
def login_emp_details():
                user=search_username_entry.get()
                Data=read_table('Emp_Creation_Table',username = user)
                Data_dic={'first_name':Data[0][0],'last_name':Data[0][1],'username':Data[0][2],'join_date':Data[0][7]}
                root = Tk()
                root.title("employee datails")
                root.geometry("400x300")
                my_label = Label(root, text="empoyee datails are!").pack()
                my_label = Label(root, text=f"firstname : {Data_dic['first_name']}").pack()
                my_label = Label(root, text=f"lastname  : {Data_dic['last_name']}").pack()
                my_label = Label(root, text=f"username  : {Data_dic['username']}").pack()
                my_label = Label(root, text=f"joindate  : {Data_dic['join_date']}").pack()
def employee_emp_search_page():
                global search_username_entry
                root = Tk(className = 'employee search')
                Label(root, text='Username').grid(row=0)
                search_username_entry = Entry(root)
                search_username_entry.grid(row=0, column=1)
                button = Button(root, text = 'submit',command=login_emp_details)
                button.grid(row=9, column=0, columnspan=2)
                root.mainloop()
def employee_updated_password():
    username=user_entry.get()
    curent_password=current_password_entry.get()
    new_password=new_password_entry.get()
    confirm_password=confirm_password_entry.get()
    pas=particular_col_details("Emp_Creation_Table",username,'password')[0][0]
    if pas == curent_password:
        if new_password == confirm_password:
            update_table('Emp_Creation_Table',username,'password',new_password)
            root = Tk()
            root.title("employee change password")
            root.geometry("400x300")
            my_label = Label(root,text="password is updated ").pack()
        else:
            messagebox.showwarning('password','new_password not same as confirm_password')
    else:
        messagebox.showwarning('password','wrong current password')
def employee_change_password_page():
    global current_password_entry,new_password_entry,confirm_password_entry
    root = Tk(className = 'password change')
    Label(root, text='current password').grid(row=0)
    Label(root, text='new password').grid(row=1)
    Label(root, text='confirm password').grid(row=2)
    
    current_password_entry = Entry(root)
    new_password_entry = Entry(root)
    confirm_password_entry = Entry(root)
    
    current_password_entry.grid(row=0, column=1)
    new_password_entry.grid(row=1, column=1)
    confirm_password_entry.grid(row=2, column=1)

    button = Button(root, text = 'submit',command=employee_updated_password)
    button.grid(row=9, column=0, columnspan=2)
    root.mainloop()
def employee_leave_request():
    username=user_entry.get()
    fromdate=fromdate_entry.get()
    fromdate_validation(fromdate)
    todate=to_entry.get()
    todate_validation(todate)
    from datetime import date
    date1=date(int(fromdate[0:4]),int(fromdate[5:7]),int(fromdate[8:10]))
    date2=date(int(todate[0:4]),int(todate[5:7]),int(todate[8:10]))
    leave_balance=6
    dic={"username":username,"from_date":fromdate,"to_date":todate,"no_of_days":date2-date1,"leave_balance":leave_balance,"status":"pending"}
    insert_row("Leave_Request_Table",dic)
    root = Tk()
    root.title("employee leave request")
    root.geometry("400x300")
    if (fromdate==True) and (todate==True):
        my_label = Label(root,text="leave request applied").pack()
def employee_leave_request_page():
    global fromdate_entry,to_entry
    root = Tk(className = 'employee search')

    Label(root, text='fromdate').grid(row=0)
    Label(root, text='todate').grid(row=1)
    
    fromdate_entry = Entry(root)
    to_entry = Entry(root)
    
    fromdate_entry.grid(row=0, column=1)
    to_entry.grid(row=1, column=1)

    button = Button(root, text = 'submit',command=employee_leave_request)
    button.grid(row=9, column=0, columnspan=2)
    root.mainloop()
home_console()

