import pymysql as sql
import sys
con = sql.connect(host="127.0.0.1",user="root",password="sql", database="bugtrackingsystem",charset="utf8")
def addmanager():
    print("\n")
    empcode=int(input("Enter employee code:"))
    empname=input("Enter the Employee Name:")
    empemail=input("Enter employee email:")
    emppassword=input("Enter the Password:")
    gender=input("Enter gender:")
    dob=input("Enter dob:")
    mob=int(input("Enter your mobile no:"))
    role='Manager'
    cur=con.cursor()
    qry=f"insert into employees values({empcode},'{empname}','{empemail}','{emppassword}','{gender}','{dob}',{mob},'{role}')"
    cur.execute(qry)
    if cur.rowcount==1:
        print("Record Inserted Successfully !!!!")
    else:
        print("Error in inserting the record !!!!")
    con.commit()

def viewmanager():
    print("\n")
    qry = f"select * from employees where role='Manager'"
    cur = con.cursor()
    cur.execute(qry)
    if cur.rowcount!=0:
        for i in cur.fetchall():
            print(i)
    else:
        print("No Record Found !!!!")
def deletemanager():
    print("\n")
    id = int(input("Enter Manager Employee Id : "))
    qry=f"delete from employees where empcode={id}"
    cur = con.cursor()
    cur.execute(qry)
    con.commit()
    if cur.rowcount==1:
        print("Record Deleted Successfully !!!!")
    else:
        print("Error in deleteing the record !!!!")
def updatemanager():
    print("\n")
    empcode = int(input("Enter Manager Employee Id you want to update: "))
    cur = con.cursor()
    cur.execute(f"select * from employees where empcode={empcode}")
    if cur.rowcount==1:
        print("Press 1 to update name")
        print("Press 2 to update email")
        print("Press 3 to update password")
        print("Press 4 to update gender")
        print("Press 5 to update DOB")
        print("Press 6 to update mobile no")
        print("Press 7 to back to previous menu")
        ch=int(input("Enter Your Choice:"))
        if ch==1:
            empname=input("Enter the Employee Name:")
            qry = f"update employees set empname='{empname}' where empcode={empcode}"
        elif ch==2:
            empemail=input("Enter Manager email:")
            qry = f"update employees set empemail='{empemail}' where empcode={empcode}"
        elif ch==3:
            emppassword=input("Enter the Password:")
            qry = f"update employees set emppassword='{emppassword}' where empcode={empcode}"
        elif ch==4:
            gender=input("Enter Manager gender:")
            qry = f"update employees set gender='{gender}' where empcode={empcode}"
        elif ch==5:
            dob=input("Enter dob:")
            qry = f"update employees set dob='{dob}' where empcode={empcode}"
        elif ch==6:
            mob=int(input("Enter your mobile no:"))
            qry = f"update employees set mobileNO='{mob}' where empcode={empcode}"
        else:
            pass
        if ch <7:
            cur.execute(qry)
            con.commit()
            if cur.rowcount==1:
                print("Record Updated Successfully !!!!")
            else:
                print("Error in updating the record!!!!")
    else:
        print("Invalid employee id !!!!!")

def updatemanager1(empcode):
    print("\n")
    print("Press 1 to update name")
    print("Press 2 to update email")
    print("Press 3 to update password")
    print("Press 4 to update gender")
    print("Press 5 to update DOB")
    print("Press 6 to update mobile no")
    print("Press 7 to back to previous menu")
    ch=int(input("Enter Your Choice:"))
    if ch==1:
        empname=input("Enter the Name you want to update to:")
        qry = f"update employees set empname='{empname}' where empcode={empcode}"
    elif ch==2:
        empemail=input("Enter the email you want to update to:")
        qry = f"update employees set empemail='{empemail}' where empcode={empcode}"
    elif ch==3:
        emppassword=input("Enter the Password:")
        qry = f"update employees set emppassword='{emppassword}' where empcode={empcode}"
    elif ch==4:
        gender=input("Enter Manager gender:")
        qry = f"update employees set gender='{gender}' where empcode={empcode}"
    elif ch==5:
        dob=input("Enter dob:")
        qry = f"update employees set dob='{dob}' where empcode={empcode}"
    elif ch==6:
        mob=int(input("Enter your mobile no:"))
        qry = f"update employees set mobileNO='{mob}' where empcode={empcode}"
    else:
        pass
    if ch <7:
        cur=con.cursor()
        cur.execute(qry)
        con.commit()
        if cur.rowcount==1:
            print("Record Updated Successfully !!!!")
        else:
            print("Error in updating the record!!!!")
    else:
        print("Invalid employee id !!!!!")
        
def manager():
    print("\n")
    print("You have successfully Entered the Manager Section")
    print("Enter 1 to Add manager Account")
    print("Enter 2 to View Mangager Details")
    print("Enter 3 to Delete Manager Record")
    print("Enter 4 to Update Manager Record")
    print("Enter 5 to Exit Session")
    ch=int(input("Enter your choiche:"))
    if ch==1:
        addmanager()
    elif ch==2:
        viewmanager()
    elif ch==3:
        deletemanager()
    elif ch==4:
        updatemanager()
    elif ch==5:
        sys.exit()
    else:
        print("Invalid Choice")
        sys,exit()

def addemployees():
    print("\n")
    empcode=int(input("Enter employee code:"))
    empname=input("Enter the Employee Name:")
    empemail=input("Enter employee email:")
    emppassword=input("Enter the Password:")
    gender=input("Enter gender:")
    dob=input("Enter dob:")
    mob=int(input("Enter your mobile no:"))
    role=input("Enter employee role:")
    cur=con.cursor()
    qry=f"insert into employees values({empcode},'{empname}','{empemail}','{emppassword}','{gender}','{dob}',{mob},'{role}')"
    cur.execute(qry)
    if cur.rowcount==1:
        print("Record Inserted Successfully !!!!")
    else:
        print("Error in inserting the record !!!!")
    con.commit()

def viewemployees():
    print("\n")
    qry = f"select * from employees where role !='Manager'"
    cur = con.cursor()
    cur.execute(qry)
    if cur.rowcount!=0:
        for i in cur.fetchall():
            print(i)
    else:
        print("No Record Found !!!!")
def deleteemployees():
    print("\n")
    id = int(input("Enter Employee Id : "))
    qry=f"delete from employees where empcode={id} and role !='Manager'"
    cur = con.cursor()
    cur.execute(qry)
    con.commit()
    if cur.rowcount==1:
        print("Record Deleted Successfully !!!!")
    else:
        print("Error in deleteing the record !!!!")
def updateemployees():
    print("\n")
    empcode = int(input("Enter Employee Id you want to update: "))
    cur = con.cursor()
    cur.execute(f"select * from employees where empcode={empcode} and role !='Manager'")
    if cur.rowcount==1:
        print("Press 1 to update name")
        print("Press 2 to update email")
        print("Press 3 to update password")
        print("Press 4 to update gender")
        print("Press 5 to update DOB")
        print("Press 6 to update mobile no")
        print("Press 7 to back to previous menu")
        ch=int(input("Enter Your Choice:"))
        if ch==1:
            empname=input("Enter the Employee Name:")
            qry = f"update employees set empname='{empname}' where empcode={empcode}"
        elif ch==2:
            empemail=input("Enter employee email:")
            qry = f"update employees set empemail='{empemail}' where empcode={empcode}"
        elif ch==3:
            emppassword=input("Enter the Password:")
            qry = f"update employees set emppassword='{emppassword}' where empcode={empcode}"
        elif ch==4:
            gender=input("Enter Manager gender:")
            qry = f"update employees set gender='{gender}' where empcode={empcode}"
        elif ch==5:
            dob=input("Enter dob:")
            qry = f"update employees set dob='{dob}' where empcode={empcode}"
        elif ch==6:
            mob=int(input("Enter your mobile no:"))
            qry = f"update employees set mobileNO='{mob}' where empcode={empcode}"
        elif ch==7:
            role=int(input("Enter Employee role:"))
            qry = f"update employees set role='{role}' where empcode={empcode}"
        else:
            pass
        if ch <8:
            cur.execute(qry)
            con.commit()
            if cur.rowcount==1:
                print("Record Updated Successfully !!!!")
            else:
                print("Error in updating the record!!!!")
    else:
        print("Invalid employee id !!!!! or you are trying to update manager details")

def employees():
    print("\n")
    print("You have successfully Entered the Manager Section")
    print("Enter 1 to Add Employees")
    print("Enter 2 to View Employees Details !!! Other than Manger")
    print("Enter 3 to Delete Employee Record")
    print("Enter 4 to Update Employees Record")
    print("Enter 5 to Exit Session")
    ch=int(input("Enter your choiche:"))
    if ch==1:
        addemployees()
    elif ch==2:
        viewemployees()
    elif ch==3:
        deleteemployees()
    elif ch==4:
        updateemployees()
    elif ch==5:
        sys.exit()
    else:
        print("Invalid Choice")
        sys.exit()
    
def project():
    print("\n")
    qry = f"select * from project"
    cur = con.cursor()
    cur.execute(qry)
    if cur.rowcount!=0:
        for i in cur.fetchall():
            print(i)
    else:
        print("No Record Found !!!!")
def bugreport():
    print("\n")
    qry = f"select * from bugreport"
    cur = con.cursor()
    cur.execute(qry)
    if cur.rowcount!=0:
        for i in cur.fetchall():
            print(i)
    else:
        print("No Record Found !!!!")
    
def AdminModule():
    print("\n")
    print("You have successfully Entered the Admin Module")
    print("Enter 1 to Enter Manager Section")
    print("Enter 2 to Enter Employees Section")
    print("Enter 3 to view all project")
    print("Enter 4 to view Bugreport")
    print("Enter 5 to to terminate session")
    ch=int(input("Enter your choiche:"))
    if ch==1:
        manager()
    elif ch==2:
        employees()
    elif ch==3:
        project()
    elif ch==4:
        bugreport()
    elif ch==5:
        print("Thanks")
        sys.exit()
    else:
        print("Invalid Choice")
        sys.exit()
def addproject():
    print("\n")
    pid=int(input("Please Enter the projectID:"))
    pname=input("Please Enter the projectName:")
    sdate=input("Please Enter the project start date:")
    edate=input("Please Enter the project end date:")
    pdec=input("Please Enter the project Description:")
    cur=con.cursor()
    qry=f"insert into values ({pid},'{pname}','{sdate}','{edate}','{pdec}')"
    cur.execute(qry)
    cur.commit()
    
def deleteproject():
    print("\n")
    pid = int(input("Enter Project Id you want to delete: "))
    cur=con.cursor()
    qw=f"select * from project"
    cur.execute(qw)
    if cur.rowcount!=0:
        cur=con.cursor()
        qry=f"delete from project where projectID ={pid}"
        print("Record Deleted Successfully !!!!")
    else:
        print("Error in deleteing the record /Invalid projectID!!!!")
def manageproject():
    print("\n")
    print("Enter 1 to Add project")
    print("Enter 2 to view project")
    print("Enter 3 to delete project")
    print("Enter 4 to update project")
    print("Enter 5 to to terminate session")
    ch=int(input("Enter your choiche:"))
    if ch==1:
        addproject()
    elif ch==2:
        project()
    elif ch==3:
        deleteproject()
    else:
        sys.exit()
def addbug():
    print("\n")
    bugNo=int(input("Enter the bugNo:"))
    bugCode=int(input("Enter the Bug code:"))
    projectID=int(input("Enter projectID:"))
    TCode=int(input("Enter the Tester employee code:"))
    ECode=int(input("Enter your employee code:"))
    status=input("Enter the bug status:")
    bugdes=input("Enter bug description:")
    cur=con.cursor()
    qry=f"insert into bugreport values({bugNo},{bugCode},{projectID},{TCode},{ECode},'{status}','{bugdes}')"
    con.excute(qry)
    con.commit()
def deletebug():
    print("\n")
    bugNO= int(input("Enter the bug NO: "))
    qry=f"delete from bugreport where bugNo={bugNo}"
    cur = con.cursor()
    cur.execute(qry)
    con.commit()
    if cur.rowcount==1:
        print("Record Deleted Successfully !!!!")
    else:
        print("Error in deleteing the record !!!!")

def bugupdateok(bugNo):
    print("\n")
    print("Press 1 to update bugCode:")
    print("Press 2 to update projectID:")
    print("Press 3 to update Tester Code:")
    print("Press 4 to update bug status:")
    print("Press 5 to update bug Description:")
    print("Press 6 to terminate Session:")
    ch=int(input("Enter your Choiche:"))
    if ch==1:
        bugCode=int(input("Enter the Bugcode you want to upadte to:"))
        qry=f"update bugreport set bugCode={bugCode} where bugNo={bugNo}"
    elif ch==2:
        projectID=int(input("Enter the projectID you want to upadte to:"))
        qry=f"update bugreport set projectID={projectID} where bugNo={bugNo}"
    elif ch==3:
        TCode=int(input("Enter the Tester Code you want to upadte to:"))
        qry=f"update bugreport set TCode={TCode} where bugNo={bugNo}"
    elif ch==4:
        ECode=int(input("Enter the Employee Code you want to upadte to:"))
        qry=f"update bugreport set ECode={ECode} where bugNo={bugNo}"
    elif ch==5:
        status=input("Enter the bug status you want to upadte to:")
        qry=f"update bugreport set status='{status}' where bugNo={bugNo}"
    elif ch==6:
        bugDes=input("Enter the Employee Code you want to upadte to:")
        qry=f"update bugreport set bugDes='{bugDes}' where bugNo={bugNo}"
    elif ch==7:
        print("Session Terminated")
        sys.exit()
    else:
        pass
    if ch <7:
        cur=con.cursor()
        cur.execute(qry)
        con.commit()
        if cur.rowcount==1:
            print("Record Updated Successfully !!!!")
        else:
            print("Error in updating the record!!!!")
            
def updatebug():
    print("\n")
    bugNo= int(input("Enter the bug NO you want to update:"))
    cur=con.cursor()
    cur.execute(f"select * from bugreport where bugNo={bugNo}")
    if cur.rowcount==1:
        bugupdateok(bugNo)
    else:
        print("No such Bug no in our system")
        sys.exit()
        
def bugsection():
    print("\n")
    print("Enter 1 to add new bug:")
    print("Enter 2 to view all bug")
    print("Enter 3 to update bug")
    print("Enter 4 to delete bug")
    print("Enter 5 to terminate session")
    ch=int(input("Enter your choiche:"))
    if ch==1:
        addbug()
    elif ch==2:
        bugreport()
    elif ch==3:
        updatebug()
    elif ch==4:
        deletebug()
    elif ch==5:
        print("Done")
        sys.exit()
    else:
        pass
    
def managermodule():
    print("\n")
    print("Manager")
    print("Enter 1 to update your profile")
    print("Enter 2 to manage project")
    print("Enter 3 to view Bugreport")
    print("Enter 4 to to terminate session")
    ch=int(input("Enter your choiche:"))
    if ch==1:
        empcode=int(input("Enter Manger Employee code:"))
        emppassword=input("Enter Your Password:")
        qry=f"select * from employees where empcode={empcode} and role ='Manager' and emppassword='{emppassword}'"
        cur=con.cursor()
        cur.execute(qry)
        if cur.rowcount!=0:
            updatemanager1(empcode)
        else:
            print("Invalid Manager Id/Invalid Password")
            sys.exit()
    elif ch==2:
        manageproject()
    elif ch==3:
        bugsection()
    else:
        print("Invalid Manager Id")
        sys.exit()
def eprofile(empcode):
    print("\n")
    print("Press 1 to update name")
    print("Press 2 to update email")
    print("Press 3 to update password")
    print("Press 4 to update gender")
    print("Press 5 to update DOB")
    print("Press 6 to update mobile no")
    pwd=input("Enter Your Password to update your profile:")
    cur=con.cursor()
    cur.execute(f"select * from employees where empcode={empcode} and emppassword='{pwd}'")
    ch=int(input("Enter Your Choice"))
    if cur.rowcount!=0:
        if ch==1:
            empname=input("Enter the Name you want to update to:")
            qry = f"update employees set empname='{empname}' where empcode={empcode}"
        elif ch==2:
            empemail=input("Enter email you want to update to:")
            qry = f"update employees set empemail='{empemail}' where empcode={empcode}"
        elif ch==3:
            emppassword=input("Enter Password you want to update to:")
            qry = f"update employees set emppassword='{emppassword}' where empcode={empcode}"
        elif ch==4:
            gender=input("Enter gender you want to update to:")
            qry = f"update employees set gender='{gender}' where empcode={empcode}"
        elif ch==5:
            dob=input("Enter dob you want to update to:")
            qry = f"update employees set dob='{dob}' where empcode={empcode}"
        elif ch==6:
            mob=int(input("Enter your mobile no you want to update to:"))
            qry = f"update employees set mobileNO='{mob}' where empcode={empcode}"
        else:
            print("Invalid Choice!")
            sys.exit()
        if ch <7:
            cur.execute(qry)
            con.commit()
            if cur.rowcount==1:
                print("Record Updated Successfully !!!!")
            else:
                print("Error in updating the record!!!!")
    else:
        print("Invalid Employee ID")
def associateconsole(empcode):
    print("Enter 1 to update your profile")
    print("Enter 2 to update Bug status")
    print("Enter 3 to view BUG")
    print("Enter 4 to view BUG Detail")
    print("Enter 5 to exit")
    print("\n")
    ch=int(input("Enter your Choice:"))
    pwd=input("Enter Your Password:")
    cur=con.cursor()
    cur.execute(f"select * from employees where empcode={empcode} and emppassword='{pwd}'")
    if cur.rowcount!=0:
        if ch==1:
            eprofile(empcode)
        elif ch==2:
            bugCode=int(input("Enter the bugCode for which you want to upadte status:"))
            cur=con.cursor()
            cur.execute(f"select * from bugreport where bugCode={bugCode}")
            if cur.rowcount==1:
                cur=con.cursor()
                status=input("Enter the status you to update to:")
                qry=f"update bugreport set status ='{status}' where bugCode={bugCode}"
                con.commit()
                print("Record UPDATED successfully")
            else:
                print("Error while updating BUG status")
        elif ch==3:
            cur=con.cursor()
            qry=f"select * from bugreport"
            cur.execute(qry)
        elif ch==4:
            bugNo=int(input("Enter bugNo for you which you want to see details:"))
            cur=con.cursor()
            qry=f"select bugDes from bugreport where bugCode={bugNo}"
            cur.execute(qry)
        elif ch==5:
            sys.exit()
        else:
            sys.exit()
    else:
        print("Invalid Password")
        sys.exit()
        
def associateconsoletester(empcode):
    print("\n")
    print("Enter 1 to update your profile")
    print("Enter 2 to add Bug")
    print("Enter 3 to update Bug status")
    print("Enter 4 to view BUG")
    print("Enter 5 to view BUG Detail")
    pwd=input("Enter Your Password:")
    cur=con.cursor()
    cur.execute(f"select * from employees where empcode={empcode} and emppassword='{pwd}'")
    ch=int(input("Enter Your Choice"))
    if cur.rowcount!=0:
        if ch==1:
            eprofile()
        elif ch==2:
            addbug()
        elif ch==3:
            bugCode=int(input("Enter the bugCode for which you want to upadte status:"))
            cur=con.cursor()
            cur.execute(f"select * from bugreport where bugCode={bugCode}")
            if cur.rowcount==1:
                cur=con.cursor()
                status=input("Enter the status you to update to:")
                qry=f"update bugreport set status ='{status}' where bugCode={bugCode}"
                con.commit()
                print("Record UPDATED successfully")
            else:
                print("Error while updating BUG status")
        elif ch==4:
            cur=con.cursor()
            qry=f"select * from bugreport"
            cur.execute(qry)
        elif ch==5:
            bugNo=int(input("Enter bugNo for you which you want to see details:"))
            cur=con.cursor()
            qry=f"select bugDes from bugreport where bugCode={bugNo}"
            cur.execute(qry)
        else:
            pass
            sys.exit()
            
    else:
        print("Invalid Password")
        sys.exit()
    
# Program starts  here:-------------------------------------------------------------"
print("---------------------------------------------------")
print("\n")
print("Welcome to Bugs Tracking System")
print("Enter 1 to enter Admin Console")
print("Enter 2 to enter Manager Console")
print("Enter 3 to enter Associate Console")

choice=int(input("Enter your Choice:"))
if choice==1:
    user=int(input("Enter your user ID to login:"))
    cur=con.cursor()
    role='Admin'
    qry=f"select * from employees where empcode={user} and role='{role}'"
    m=cur.execute(qry)
    n=cur.execute(f"select * from employees where empcode={user}")
    if m==1:
        pwd=input("Enter Your Password:")
        qry=f"select * from employees where empcode={user} and emppassword='{pwd}'"
        cur.execute(qry)
        if cur.rowcount==1:
            AdminModule()
        else:
            print("Incorrect Password")
            sys.exit()
    elif n==1:
        print("You are not an Admin")
        sys.exit()
    else:
        print("Invalid User Id")
        sys.exit()
elif choice==2:
    managermodule()
elif choice==3:
    empcode=int(input("Please Enter your employee code:"))
    cur=con.cursor()
    qry=f"select * from employees where empcode={empcode} and role ='Tester'"
    qw=f"select * from employees where empcode={empcode}"
    t=cur.execute(qry)
    o=cur.execute(qw)
    if t!=0:
        associateconsoletester(empcode)
    elif o!=0:
        associateconsole(empcode)
    else:
        print("Invalid Employee ID")
        sys.exit()
else:
    print("Invalid Choice")
    sys.exit()
con.close()

