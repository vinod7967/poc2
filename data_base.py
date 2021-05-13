import pymysql

conn = pymysql.connect(user='root',password='root',host="localhost")

cur = conn.cursor()
cur.execute("create database if not exists Employee_leave_management_system")
cur.execute("use Employee_leave_management_system")             
def create_table():       
        cur.execute('create table Emp_Creation_Table(first_name varchar(20),last_name varchar(20),username varchar(20) not null primary key,email_id varchar(50),password varchar(20),emp_salary varchar(15),emp_pf_no varchar(20),join_Date varchar(20),pan_no varchar(10),leave_balance varchar(10))')
        print(cur)
        cur.execute('create table Leave_Request_Table(username varchar(20) not null primary key,from_date varchar(20),to_date varchar(20),no_of_days varchar(20),leave_balance varchar(20),status varchar(20))')
        print(cur)

def insert_row(table_name,column):
        if table_name == 'Emp_Creation_Table':
            query = f"insert into {table_name} (first_name,last_name,username,email_id,password,emp_salary,emp_pf_no,join_Date,pan_no,leave_balance) values('{column['first_name']}','{column['last_name']}','{column['username']}','{column['email_id']}','{column['password']}','{column['emp_salary']}','{column['emp_pf_no']}','{column['join_Date']}','{column['pan_no']}','{column['leave_balance']}')"
        elif table_name == 'Leave_Request_Table':
            query = f"insert into {table_name} (username,from_date,to_date,no_of_days,leave_balance,status) values('{column['username']}','{column['from_date']}','{column['to_date']}','{column['no_of_days']}','{column['leave_balance']}','{column['status']}')"
        cur.execute(query)
        conn.commit() 
         
def read_table(table_name,username=None):
        if username == None:
            query = f"select * from {table_name}"
            cur.execute(query)
            conn.commit()
            return cur.fetchall()
            
            
        else:
            query = f"select * from {table_name} where username = '{username}'"
            cur.execute(query)
            conn.commit()  
            return cur.fetchall()


def update_table(table_name,username,column,data):
        query = f"update {table_name} set {column} = '{data}' where username='{username}'"
        cur.execute(query)
        conn.commit()

def delete_row(table_name,username):

        qurey = f"delete from {table_name} where username = '{username}' "
        cur.execute(qurey)
        conn.commit()
def particular_col_details(table_name,username,column):
        query = f"select {column} from {table_name} where username = '{username}'"
        cur.execute(query)
        conn.commit()
        return cur.fetchall()
# column1 = {'username':'lol','from_date':'05-04-2021','to_date':'07-04-2021','no_of_days':'2','approval':'Pending'}  
# column2 = {'first_name':'sample','last_name':'123','username':'lol','email_id':'sample','password':'123456','emp_salary':10000,'emp_pf_no':12355,'join_Date':'03-02-2021','pan_no':'ADGJ4568','leave_balance':2}  
# column3 = {'first_name':'sample','last_name':'123','username':'vinod','email_id':'sample','password':'123456','emp_salary':10000,'emp_pf_no':12355,'join_Date':'03-02-2021','pan_no':'ADGJ4568','leave_balance':2}  
#obj = Database()
#print(particular_col_details("Emp_Creation_Table",'salma123','password')[0][0])
