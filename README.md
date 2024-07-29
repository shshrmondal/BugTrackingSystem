# BugTrackingSystem  
# Overview  

This console-based project management system provides role-specific access for Admin, Manager, and Employee, ensuring secure and organized management of projects, employees, and bug reports. The system enforces strict role-based access control, preventing unauthorized access to various parts of the system.    

Authentication  
Login Process  
ID and Password: Users authenticate using their empCode (ID) and password.  
Role Verification: Post-login, the system verifies the user’s role to determine access to the appropriate console.  
Role-Based Access  
Console Access Control:  
Admin Console: Accessible only to users with the Admin role. Admins cannot access Manager or Employee consoles.  
Manager Console: Accessible only to users with the Manager role. Managers cannot access Admin or Employee consoles.  
Employee Console: Accessible only to users with the Employee role. Employees cannot access Admin or Manager consoles.  

### Admin Console  

- **Manager Management**  
  - Add Manager Account  
  - View Manager Account  
  - Delete Manager  
  - Update Manager Details  

- **Employee Management**  
  - Add Employee Account  
  - View Employee Account  
  - Delete Employee Account  
  - Update Employee Details  

- **Project Management**  
  - View All Projects

- **Bug Reports**  
  - View Bug Reports  

### Manager Console  

- **Profile Management**  
  - Update Profile  

- **Project Management**  
  - Add Project  
  - View All Projects  
  - Delete Project  
  - Update Project  

- **Bug Management**  
  - Add New Bug  
  - View All Bugs  
  - Update Bug  
  - Delete Bug  

- **Exit**   

### Employee Console  

- **Profile Management**
  - Update Profile

- **Bug Reporting (Tester Only)**
  - Add Bug Report

- **Bug Status Management**
  - Update Bug Status
  - View Bugs
  - Bug Details

- **Exit**

## Database Schema

The system uses a relational database with the following tables:

- **Employee**
  - `empCode` (INT, PK) - Username for login
  - `empName` (VARCHAR(30))
  - `empEmail` (VARCHAR(40))
  - `empPassword` (VARCHAR(20))
  - `gender` (VARCHAR(10))
  - `DOB` (VARCHAR(20))
  - `mobileNo` (BIGINT)
  - `Role` (VARCHAR(20)) - Roles include Manager, Developer, Tester, Admin

- **AssignProject**
  - `projectID` (INT, FK)
  - `empCode` (INT, FK)

- **Project**
  - `projectID` (INT, PK)
  - `projectName` (VARCHAR(30))
  - `SDate` (VARCHAR(30))
  - `EDate` (VARCHAR(30))
  - `projectDec` (VARCHAR(200))

- **BugReport**
  - `bugNo` (INT, PK)
  - `bugCode` (INT, FK)
  - `projectID` (INT, FK)
  - `TCode` (INT, FK)
  - `ECode` (INT, FK)
  - `status` (VARCHAR(20)) - Statuses include Pending, Resolved
  - `bugDes` (VARCHAR(100))

- **BugType**
  - `bugCode` (INT, PK)
  - `bugCategory` (VARCHAR(30))
  - `bugSeverity` (VARCHAR(20)) - Severities include Critical, Major, Medium, Low  

  Snip of Console  
  ![Bug1](https://github.com/user-attachments/assets/22020688-2cb2-4e8c-bd9c-ca6367f69756) 

Navigation  

