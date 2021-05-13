from data_base import Database
from validation import *
class Adminconsole:
    def create_emp_account(self):
        #self.username=Validation().emp_usernamevalidation()
        #self.userid=Validation().emp_useridvalidation()
        x=emp_emailvalidation("vinod@ojas-it.com")
        print(x)
        """self.password=Validation().emp_passwordvalidation()
        self.emp_salary=Validation().emp_salaryvalidation()
        self.emp_pf_no=Validation().emp_pfno_validation()
        self.join_date=Validation().date_validation()
        self.pan_id=Validation().panid_validation()
        self.leave_balance=6
        dic={"first_name":self.username[0],"last_name":self.username[1],"username":self.userid,"email_id":self.email_id,"password":self.password,
             "emp_salary":self.emp_salary,"emp_pf_no":self.emp_pf_no,
             "join_Date":self.join_date,"pan_no":self.pan_id,"leave_balance":self.leave_balance,}
        Database().insert_row("Emp_Creation_Table",dic)
    def list_emp_details(self):
        username=input("enter username to know the employee details")
        if username:
            print(Database().read_table("emp_creation_table",username))
        else:
            print(Database().read_table("emp_creation_table"))
    def emp_leave_request(self):
        Database().read_table("Leave_Request_Table")
        self.username=input("enter username")
        self.status=input("enter status")
        Database().update_table("Leave_Request_Table",self.username,'status',self.status)
    def emp_account_del(self):
        del_row=input("enter username to delete")
        Database().delete_row("emp_creation_table",del_row)"""
    def par(self):
        pas=Database().particular_col_details("Emp_Creation_Table",'username','password')
        print(pas)
obj=Adminconsole()
obj.par()
#obj.emp_account_del()
#obj.list_emp_details()
#obj.emp_leave_request()
