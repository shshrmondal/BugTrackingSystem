# BugTrackingSystem  
# Overview  

This is a console-based project management system with distinct roles and functionalities for Admin, Manager, and Employee. The application supports role-specific access and operations, making it suitable for managing projects, employees, and bug reports effectively.  

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

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/repository.git
   ```
2. Navigate to the project directory:
   ```bash
   cd repository
   ```
3. Compile and run the application as per the instructions in the `README.md` file.

## Contributing

Feel free to contribute by submitting issues or pull requests. Please ensure that your contributions adhere to the project's coding standards and guidelines.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to adjust any details according to your preferences or any additional project specifics.
