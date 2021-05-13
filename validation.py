import datetime
import re
from data_base import *
import getpass
from string import punctuation
#Database().FUNCTION NAME
from tkinter import *
from tkinter import messagebox
def emp_emailvalidation(var):
        # ref='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,20}$'
        ref = '\w[a-z_.]\D*@ojas-it[.]com'
        if not (re.search(ref,var)):
            messagebox.showwarning('emailid','enter valid mail')
        else:
            return True
def emp_useridvalidation(var):
        db = read_table('Emp_Creation_Table')
        # usinpt=input("enter userid")
        lst = []
        for i in db:
            lst.append(i[2])
        if var in lst:
            messagebox.showwarning('userid','entered different id')
        else:
            return True
def emp_usernamevalidation(inpt,inpt1):
            if not (inpt.isalpha() and inpt1.isalpha()):
                messagebox.showwarning('username','The first name entered is incorrect')
            else:
                return True
def emp_passwordvalidation(var):
            if ' ' in var:
                messagebox.showwarning('password','there is a space in password')
            if len(var) not in range(8,17):
                messagebox.showwarning('password','password should between in min 8 & max 16 characters')
            special_chars=[True for x in var if x in punctuation]
            if len(special_chars)==0:
                messagebox.showwarning('password','your password should have one special character')
            nums=any(x.isdigit() for x in var)
            if not  nums:
                messagebox.showwarning('password','you should have atleast 1 digit in your password')
            else:
                return True
def emp_salaryvalidation(var):
            try:
                if float(var):
                    return True
            except:
                messagebox.showwarning('salary','enter valid salary')
def emp_pfno_validation(var):
            if var.isalpha():
                messagebox.showwarning('pfno','it has only alphabets')
            if var.isnumeric():
                messagebox.showwarning('pfno','it has only numarics')
            if var.isalnum():
                return True
            else:
                messagebox.showwarning('pfno','it has another characters')
def date_validation(var):
            format = "%Y-%m-%d"
            try:
                    if datetime.datetime.strptime(var, format):
                            return True
            except:
                messagebox.showwarning('joindate','it must be in YYYY-MM-DD')
def panid_validation(var):
            if var.isalpha():
                messagebox.showwarning('pfno','it has only alphabets')
            if var.isnumeric():
                messagebox.showwarning('pfno','it has only numarics')
            if var.isalnum():
                return True
            else:
                messagebox.showwarning('pfno','it has another characters')
def username_validation(self):
        while True:
            username=input("enter username")
            password=input("enter password")
            us_data=read_table("Emp_Creation_Table")
            dic={}
            for i in us_data:
                dic[i[2]]=i[4]
            if username in dic.keys():
                if password == dic[username]:
                    print("success full")
                else:
                    print("entered credentials are wrong")
                    continue
            else:
                print("entered credentials are wrong")
def fromdate_validation(var):
        format = "%Y-%m-%d"
        global from_date
        from_date=""
        date=datetime.datetime.now()
        if datetime.datetime.strptime(var, format):
                if str(datetime.datetime.strptime(var, format))[0:10]>=str(date)[0:10]:
                        from_date=from_date+str(datetime.datetime.strptime(var, format))[0:10]
                        return True         
                else:
                        messagebox.showwarning('leave','enter valid date,it should be more than the current date')
        else:
                messagebox.showwarning('leave','Incorrect data format, should be YYYY-MM-DD')
def todate_validation(var):
        format = "%Y-%m-%d"
        try:
                if datetime.datetime.strptime(var, format):
                        if from_date[0:10]<=str(datetime.datetime.strptime(var, format))[0:10]:
                                return True
                        else:
                                messagebox.showwarning('leeave','enter valid date,it should be more than the current date')
                else:
                        messagebox.showwarning('leave','Incorrect data format, should be YYYY-MM-DD')
        except:
                messagebox.showwarning('leave','enter valid to date')
 
                
#print(emp_emailvalidation("uday@ojas-it.com"))
#obj.fromdate_validation()
#obj.todate_validation()






# password length be min 8 char and max length is 16 in that upper&lower cases &special symbols and numbers
#def changepassword():






# class validation:
#     def __init__(self):
#         pass
#     def emp_usernamevalidation(username):
#
#
#     def emp_salaryvalidation(self):
#
#     def emp_datevalidation(self):
#
#     def emp_leave_request_validation(emp_username, from_date, to_date):
#         print("it is a valid ")
