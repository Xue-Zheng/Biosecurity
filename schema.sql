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

insert into AnimalPest (animal_id, description, size)
values (
        'Asian Brown Mussel',
        'Brown or brown-yellow color, possibly tinged with green around the edges.',
        'Length of about 90mm, can reach up to 120mm.'
    ),
    (
        'Crab with Mitten Claws',
        ' Front claws with hairy mitten with white tips, distinctive notches between the eyes, 4 spines on each side of the carapace, light brown to olive green carapace.',
        'Carapace width generally 5cm to 7cm, up to 10cm.'
    ),
    (
        'South American Fruit Fly',
        'Distinctive patterned wings with yellow to orange-brown bands, yellow to orange-brown body.',
        '12mm to 14mm long.'
    ),
    (
        'Aphid',
        'Pale green, slightly elongated, oval-shaped.',
        'About 2mm long.'
    ),
    (
        'Asian Ambrosia Beetle',
        'The adult beetles are small and slender, with a brown-black color, and are hard to spot as they spend most of their lives inside their tunnels.',
        '2mm to 3mm long.'
    );
insert into AnimalPest (animal_id)
values ('citrus longhorn beetle'),
    ('Pea Weevil'),
    ('Mountain pine Beetle'),
    ('Black Rot'),
    ('Brown Marmorated Stink Bug'),
    ('Flies'),
    ('Pine Shoot Beetle'),
    ('European Pine Shoot Moth'),
    ('Red Imported Fire Ant (RIFA)'),
    ('Painted Apple Moth Caterpillar'),
    ('Pine Processionary Moth'),
    ('European Crane Fly'),
    ('Wallaby'),
    ('Northern Pacific Seastar'),
    ('Nun Moth');