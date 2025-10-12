CREATE TABLE libraryStaff (
    staffId INT PRIMARY KEY,
    name VARCHAR(255),
    jobTitle VARCHAR(255),
    departmentId INT,
    gender gender,
    address VARCHAR(255),
    phoneNumber VARCHAR(15),
    emailAddress VARCHAR(100) NULL,
    hireDate DATE,
    managerId INT,
    FOREIGN KEY (departmentId) REFERENCES departments(deptId)
);


