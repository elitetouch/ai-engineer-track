create TABLE authors (
    authorId INT PRIMARY KEY,
    authorName VARCHAR(255),
    countryOfOrigin VARCHAR(255),
    numberOfBooksWritten INT
);


create TABLE books (
    bookId INT PRIMARY KEY,
    title VARCHAR(225),
    authorId INT,
    genre VARCHAR(100),
    dateOfPublication DATE,
    publisher VARCHAR(255),
    ISBN VARCHAR(20),
    language VARCHAR(50),
    availableCopies INT,
    ageRating VARCHAR(10),
    FOREIGN KEY (authorId) REFERENCES authors(authorId)
);


CREATE TYPE fulfillment_status AS ENUM ('Pending', 'Fulfilled', 'Processing');

CREATE TABLE bookOrders (
    orderId SERIAL PRIMARY KEY,
    orderDate DATE,
    bookId INT,
    cost DECIMAL(10, 2),
    quantity INT,
    supplyDate DATE,
    fulfillmentStatus fulfillment_status,
    supplierName VARCHAR(255),
    FOREIGN KEY (bookId) REFERENCES books(bookId)
);


CREATE TYPE memberStatus AS ENUM ('Active', 'Suspended');
CREATE TYPE gender AS ENUM ('Male', 'Female');
CREATE TYPE typeOfMembership AS ENUM ('Standard', 'Premium','Student');

CREATE TABLE members (
    memberId INT PRIMARY KEY,
    name VARCHAR(255),
    gender gender,
    emailAddress VARCHAR(100),
    phoneNumber VARCHAR(15),
    address VARCHAR(255),
    age INT,
    typeOfMembership typeOfMembership,
    dateOfMembership DATE,
    status memberStatus
);


CREATE TABLE borrowHistory (
    borrowedId INT PRIMARY KEY,
    bookId INT,
    memberId INT,
    borrowDate DATE,
    returnDate DATE,
    FOREIGN KEY (bookId) REFERENCES books(bookId),
    FOREIGN KEY (memberId) REFERENCES members(memberId)
);

CREATE TABLE departments (
    deptId INT PRIMARY KEY,
    departmentName VARCHAR(100),
    managerName VARCHAR(255)
);


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