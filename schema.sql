DROP TABLE IF EXISTS PestController;
DROP TABLE IF EXISTS StaffAdmin;
DROP TABLE IF EXISTS AnimalPest;
DROP TABLE IF EXISTS User;

-- Pest Controller
CREATE TABLE PestController (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    pest_controller_id_number VARCHAR(50) NOT NULL UNIQUE,
    address VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone_number VARCHAR(20) NOT NULL,
    date_joined DATE NOT NULL,
    status VARCHAR(50) NOT NULL -- active inactive
);

-- Staff/Admin
CREATE TABLE StaffAdmin (
    id INT AUTO_INCREMENT PRIMARY KEY,
    staff_number VARCHAR(50) NOT NULL UNIQUE,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    work_phone_number VARCHAR(20) NOT NULL,
    hire_date DATE NOT NULL,
    position VARCHAR(100) NOT NULL,
    department VARCHAR(100) NOT NULL,
    status VARCHAR(20) NOT NULL -- active inactive
);

-- Animal Pest Guide
CREATE TABLE AnimalPest (
    animal_id INT AUTO_INCREMENT PRIMARY KEY,
    description TEXT NOT NULL,
    distribution TEXT NOT NULL,
    size VARCHAR(100) NOT NULL,
    droppings TEXT NOT NULL,
    footprints TEXT NOT NULL,
    impacts TEXT NOT NULL,
    control_methods TEXT NOT NULL,
    images VARCHAR(255) NOT NULL
);

-- 用户（User），集成了PestController、Staffs和Admins
CREATE TABLE User (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(50) NOT NULL, -- 'PestController', 'Staff', 'Admin'
    profile_id INT NOT NULL,
    -- FOREIGN KEY (profile_id) REFERENCES StaffAdmin(id),
    UNIQUE(role, profile_id)
);

-- 示例数据填充，假设密码已经通过散列处理
INSERT INTO User (username, password, role, profile_id) 
VALUES ('pestController', '123', 'PestController', 1), 
       ('staff', '123', 'Staff', 2), 
       ('admin', '123', 'Admin', 3);
