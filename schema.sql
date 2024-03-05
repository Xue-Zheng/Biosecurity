DROP TABLE IF EXISTS PestController;
DROP TABLE IF EXISTS StaffAdmin;
DROP TABLE IF EXISTS AnimalPest;
DROP TABLE IF EXISTS User;

-- Pest Controller
CREATE TABLE PestController (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    pest_controller_id_number VARCHAR(50) UNIQUE,
    address VARCHAR(255),
    email VARCHAR(100) UNIQUE,
    phone_number VARCHAR(20),
    date_joined DATE,
    status VARCHAR(50) -- active inactive
);

-- Staff/Admin
CREATE TABLE StaffAdmin (
    id INT AUTO_INCREMENT PRIMARY KEY,
    staff_number VARCHAR(50) NOT NULL UNIQUE,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    work_phone_number VARCHAR(20),
    hire_date DATE,
    position VARCHAR(100),
    department VARCHAR(100),
    status VARCHAR(20) -- active inactive
);

-- Animal Pest Guide
CREATE TABLE AnimalPest (
    animal_id VARCHAR(100) PRIMARY KEY,
    description TEXT,
    size VARCHAR(255),
    distribution TEXT,
    droppings TEXT,
    footprints TEXT,
    impacts TEXT,
    control_methods TEXT,
    images VARCHAR(255)
);

-- 用户（User），集成了PestController、Staffs和Admins
CREATE TABLE User (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL,
    role VARCHAR(50) NOT NULL, -- 'PestController', 'Staff', 'Admin'
    profile_id INT,
    -- FOREIGN KEY (profile_id) REFERENCES StaffAdmin(id),
    UNIQUE(role, profile_id)
);
