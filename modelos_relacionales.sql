# Base de datos: clinica
CREATE DATABASE IF NOT EXISTS clinica;

USE clinica;

CREATE TABLE IF NOT EXISTS paciente
(
    ID_Paciente      INT AUTO_INCREMENT PRIMARY KEY,
    Nombre           VARCHAR(100) NOT NULL,
    Direccion        VARCHAR(255) NOT NULL,
    Telefono         VARCHAR(15)  NOT NULL,
    Fecha_Nacimiento DATE         NOT NULL,
    Historial_Medico TEXT         NOT NULL
);

CREATE TABLE IF NOT EXISTS medico
(
    ID_Medico            INT AUTO_INCREMENT PRIMARY KEY,
    Nombre               VARCHAR(100) NOT NULL,
    Especialidad         VARCHAR(100) NOT NULL,
    Licencia_Medica      VARCHAR(50)  NOT NULL,
    Informacion_Contacto TEXT         NOT NULL
);

CREATE TABLE IF NOT EXISTS cita
(
    ID_Cita       INT AUTO_INCREMENT PRIMARY KEY,
    ID_Paciente   INT      NOT NULL,
    ID_Medico     INT      NOT NULL,
    Fecha_Hora    DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    Motivo_Visita TEXT     NOT NULL,
    FOREIGN KEY (ID_Paciente) REFERENCES paciente (ID_Paciente)
        ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (ID_Medico) REFERENCES medico (ID_Medico)
        ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS tratamiento
(
    ID_Tratamiento INT AUTO_INCREMENT PRIMARY KEY,
    Nombre         VARCHAR(100)   NOT NULL,
    Descripcion    TEXT           NOT NULL,
    Costo          DECIMAL(10, 2) NOT NULL
);

# Base de datos: Restaurante
CREATE DATABASE IF NOT EXISTS restaurante;

USE restaurante;

CREATE TABLE IF NOT EXISTS cliente
(
    ID_Cliente         INT AUTO_INCREMENT PRIMARY KEY,
    Nombre             VARCHAR(100) NOT NULL,
    Correo_Electronico VARCHAR(100) NOT NULL UNIQUE,
    Telefono           VARCHAR(15)  NOT NULL
);

CREATE TABLE IF NOT EXISTS empleado
(
    ID_Empleado        INT AUTO_INCREMENT PRIMARY KEY,
    Nombre             VARCHAR(100) NOT NULL,
    Posicion           VARCHAR(50)  NOT NULL,
    Fecha_Contratacion DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS plato
(
    ID_Platillo         INT AUTO_INCREMENT PRIMARY KEY,
    Nombre              VARCHAR(100) NOT NULL,
    Cantidad_Disponible INT(10)      NOT NULL,
    Unidad_Medida       VARCHAR(20)  NOT NULL
);

CREATE TABLE IF NOT EXISTS ingrediente
(
    ID_Ingrediente      INT AUTO_INCREMENT PRIMARY KEY,
    Nombre              VARCHAR(100) NOT NULL,
    Cantidad_Disponible INT(10)      NOT NULL,
    Unidad_Medida       VARCHAR(20)  NOT NULL
);

CREATE TABLE IF NOT EXISTS pedido
(
    ID_Pedido   INT AUTO_INCREMENT PRIMARY KEY,
    ID_Cliente  INT      NOT NULL,
    ID_Empleado INT      NOT NULL,
    Fecha_Hora  DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ID_Cliente) REFERENCES cliente (ID_Cliente)
        ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (ID_Empleado) REFERENCES empleado (ID_Empleado)
        ON DELETE RESTRICT ON UPDATE CASCADE
);

# Base de datos: Venta_Automoviles
CREATE DATABASE IF NOT EXISTS venta_automoviles;

USE venta_automoviles;

CREATE TABLE IF NOT EXISTS cliente
(
    ID_Cliente         INT AUTO_INCREMENT PRIMARY KEY,
    Nombre             VARCHAR(100) NOT NULL,
    Direccion          VARCHAR(255) NOT NULL,
    Correo_Electronico VARCHAR(100) NOT NULL UNIQUE,
    Telefono           VARCHAR(15)  NOT NULL
);

CREATE TABLE IF NOT EXISTS vendedor
(
    ID_Vendedor        INT AUTO_INCREMENT PRIMARY KEY,
    Nombre             VARCHAR(100) NOT NULL,
    Direccion          VARCHAR(255) NOT NULL,
    Telefono           VARCHAR(15)  NOT NULL,
    Fecha_Contratacion DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS vehiculo
(
    VIN             VARCHAR(17) PRIMARY KEY,
    Marca           VARCHAR(50)    NOT NULL,
    Modelo          VARCHAR(50)    NOT NULL,
    Anio            INT(4)         NOT NULL,
    Color           VARCHAR(20)    NOT NULL,
    Tipo            VARCHAR(50)    NOT NULL,
    Precio          DECIMAL(10, 2) NOT NULL,
    Fecha_Recepcion DATETIME       NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS venta
(
    ID_Venta    INT AUTO_INCREMENT PRIMARY KEY,
    ID_Cliente  INT            NOT NULL,
    ID_Vendedor INT            NOT NULL,
    VIN         VARCHAR(17)    NOT NULL,
    Fecha       DATETIME       NOT NULL DEFAULT CURRENT_TIMESTAMP,
    Precio      DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (ID_Cliente) REFERENCES cliente (ID_Cliente)
        ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (ID_Vendedor) REFERENCES Vendedor (ID_Vendedor)
        ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (VIN) REFERENCES vehiculo (VIN)
        ON DELETE RESTRICT ON UPDATE CASCADE
);

### Volcado de datos mediante procedimientos almacenados para la base de datos clinica ###
USE clinica;
# Crear 1000 registros en la tabla paciente
DELIMITER //

CREATE PROCEDURE InsertarPacientes()
BEGIN
    DECLARE i INT DEFAULT 1;
    DECLARE nombre VARCHAR(100);
    DECLARE direccion VARCHAR(255);
    DECLARE telefono VARCHAR(15);
    DECLARE fecha_nacimiento DATE;
    DECLARE historial_medico TEXT;

    WHILE i <= 1000 DO
            SET nombre = CONCAT('Paciente ', i);
            SET direccion = CONCAT('Direccion ', i);
            SET telefono = CONCAT('3', FLOOR(1 + (RAND() * 999999999)));
            SET fecha_nacimiento = DATE_ADD('1990-01-01', INTERVAL FLOOR(1 + (RAND() * 30)) YEAR);
            SET historial_medico = CONCAT('Historial medico ', i);

            INSERT INTO paciente (Nombre, Direccion, Telefono, Fecha_Nacimiento, Historial_Medico)
            VALUES (nombre, direccion, telefono, fecha_nacimiento, historial_medico);

            SET i = i + 1;
        END WHILE;
END //

CALL InsertarPacientes();

# Crear 1000 registros en la tabla medico
DELIMITER //

CREATE PROCEDURE InsertarMedicos()
BEGIN
    DECLARE i INT DEFAULT 1;
    DECLARE nombre VARCHAR(100);
    DECLARE especialidad VARCHAR(100);
    DECLARE licencia_medica VARCHAR(50);
    DECLARE informacion_contacto TEXT;

    WHILE i <= 1000 DO
            SET nombre = CONCAT('Medico ', i);
            SET especialidad = CONCAT('Especialidad ', i);
            SET licencia_medica = CONCAT('Licencia medica ', i);
            SET informacion_contacto = CONCAT('Informacion de contacto ', i);

            INSERT INTO medico (Nombre, Especialidad, Licencia_Medica, Informacion_Contacto)
            VALUES (nombre, especialidad, licencia_medica, informacion_contacto);

            SET i = i + 1;
        END WHILE;
END //

CALL InsertarMedicos();

# Crear 1000 registros en la tabla cita
DELIMITER //

CREATE PROCEDURE InsertarCitas()
BEGIN
    DECLARE i INT DEFAULT 1;
    DECLARE paciente_id INT;
    DECLARE medico_id INT;
    DECLARE fecha DATETIME;
    DECLARE motivo TEXT;

    WHILE i <= 1000 DO
            SET paciente_id = FLOOR(1 + (RAND() * 1000));
            SET medico_id = FLOOR(1 + (RAND() * 1000));
            SET fecha = DATE_ADD('1960-01-01', INTERVAL FLOOR(1 + (RAND() * 62 * 365)) DAY);
            SET motivo = CONCAT('Motivo de visita ', i);

            INSERT INTO cita (ID_Paciente, ID_Medico, Fecha_Hora, Motivo_Visita)
            VALUES (paciente_id, medico_id, fecha, motivo);

            SET i = i + 1;
        END WHILE;
END //

CALL InsertarCitas();

# Crear 1000 registros en la tabla tratamiento
DELIMITER //

CREATE PROCEDURE InsertarTratamientos()
BEGIN
    DECLARE i INT DEFAULT 1;
    DECLARE nombre VARCHAR(100);
    DECLARE descripcion TEXT;
    DECLARE costo DECIMAL(10, 2);

    WHILE i <= 1000 DO
            SET nombre = CONCAT('Tratamiento ', i);
            SET descripcion = CONCAT('Descripcion del tratamiento ', i);
            SET costo = FLOOR(1 + (RAND() * 1000));

            INSERT INTO tratamiento (Nombre, Descripcion, Costo)
            VALUES (nombre, descripcion, costo);

            SET i = i + 1;
        END WHILE;
END //

CALL InsertarTratamientos();

### Volcado de datos mediante procedimientos almacenados para la base de datos restaurante ###
USE restaurante;
# Crear 1000 registros en la tabla cliente
DELIMITER //

CREATE PROCEDURE InsertarClientes()
BEGIN
    DECLARE i INT DEFAULT 1;
    DECLARE nombre VARCHAR(100);
    DECLARE correo VARCHAR(100);
    DECLARE telefono VARCHAR(15);

    WHILE i <= 1000 DO
            SET nombre = CONCAT('Cliente ', i);
            SET correo = CONCAT('cliente', i, '@gmail.com');
            SET telefono = CONCAT('3', FLOOR(1 + (RAND() * 999999999)));

            INSERT INTO cliente (Nombre, Correo_Electronico, Telefono)
            VALUES (nombre, correo, telefono);

            SET i = i + 1;
        END WHILE;
END //

CALL InsertarClientes();

# Crear 1000 registros en la tabla empleado
DELIMITER //

CREATE PROCEDURE InsertarEmpleados()
BEGIN
    DECLARE i INT DEFAULT 1;
    DECLARE nombre VARCHAR(100);
    DECLARE posicion VARCHAR(50);

    WHILE i <= 1000 DO
            SET nombre = CONCAT('Empleado ', i);
            SET posicion = CONCAT('Posicion ', i);

            INSERT INTO empleado (Nombre, Posicion)
            VALUES (nombre, posicion);

            SET i = i + 1;
        END WHILE;
END //

CALL InsertarEmpleados();

# Crear 1000 registros en la tabla plato
DELIMITER //

CREATE PROCEDURE InsertarPlatos()
BEGIN
    DECLARE i INT DEFAULT 1;
    DECLARE nombre VARCHAR(100);
    DECLARE cantidad INT;
    DECLARE unidad VARCHAR(20);

    WHILE i <= 1000 DO
            SET nombre = CONCAT('Plato ', i);
            SET cantidad = FLOOR(1 + (RAND() * 100));
            SET unidad = 'g';

            INSERT INTO plato (Nombre, Cantidad_Disponible, Unidad_Medida)
            VALUES (nombre, cantidad, unidad);

            SET i = i + 1;
        END WHILE;
END //

CALL InsertarPlatos();

# Crear 1000 registros en la tabla ingrediente
DELIMITER //

CREATE PROCEDURE InsertarIngredientes()
BEGIN
    DECLARE i INT DEFAULT 1;
    DECLARE nombre VARCHAR(100);
    DECLARE cantidad INT;
    DECLARE unidad VARCHAR(20);

    WHILE i <= 1000 DO
            SET nombre = CONCAT('Ingrediente ', i);
            SET cantidad = FLOOR(1 + (RAND() * 100));
            SET unidad = 'g';

            INSERT INTO ingrediente (Nombre, Cantidad_Disponible, Unidad_Medida)
            VALUES (nombre, cantidad, unidad);

            SET i = i + 1;
        END WHILE;
END //

CALL InsertarIngredientes();

# Crear 1000 registros en la tabla pedido
DELIMITER //

CREATE PROCEDURE InsertarPedidos()
BEGIN
    DECLARE i INT DEFAULT 1;
    DECLARE cliente_id INT;
    DECLARE empleado_id INT;

    WHILE i <= 1000 DO
            SET cliente_id = FLOOR(1 + (RAND() * 1000));
            SET empleado_id = FLOOR(1 + (RAND() * 1000));

            INSERT INTO pedido (ID_Cliente, ID_Empleado)
            VALUES (cliente_id, empleado_id);

            SET i = i + 1;
        END WHILE;
END //

CALL InsertarPedidos();

### Volcado de datos mediante procedimientos almacenados para la base de datos venta_automoviles ###
USE venta_automoviles;
# Crear 1000 registros en la tabla cliente
DELIMITER //

CREATE PROCEDURE InsertarClientes()
BEGIN
    DECLARE i INT DEFAULT 1;
    DECLARE nombre VARCHAR(100);
    DECLARE direccion VARCHAR(255);
    DECLARE correo VARCHAR(100);
    DECLARE telefono VARCHAR(15);

    WHILE i <= 1000 DO
            SET nombre = CONCAT('Cliente ', i);
            SET direccion = CONCAT('Direccion ', i);
            SET correo = CONCAT('cliente', i, '@gmail.com');
            SET telefono = CONCAT('3', FLOOR(1 + (RAND() * 999999999)));

            INSERT INTO cliente (Nombre, Direccion, Correo_Electronico, Telefono)
            VALUES (nombre, direccion, correo, telefono);

            SET i = i + 1;
        END WHILE;
END //

CALL InsertarClientes();

# Crear 1000 registros en la tabla vendedor
DELIMITER //

CREATE PROCEDURE InsertarVendedores()
BEGIN
    DECLARE i INT DEFAULT 1;
    DECLARE nombre VARCHAR(100);
    DECLARE direccion VARCHAR(255);
    DECLARE telefono VARCHAR(15);

    WHILE i <= 1000 DO
            SET nombre = CONCAT('Vendedor ', i);
            SET direccion = CONCAT('Direccion ', i);
            SET telefono = CONCAT('3', FLOOR(1 + (RAND() * 999999999)));

            INSERT INTO vendedor (Nombre, Direccion, Telefono)
            VALUES (nombre, direccion, telefono);

            SET i = i + 1;
        END WHILE;
END //

CALL InsertarVendedores();

# Crear 1000 registros en la tabla vehiculo
DELIMITER //

CREATE PROCEDURE InsertarVehiculos()
BEGIN
    DECLARE i INT DEFAULT 1;
    DECLARE vin VARCHAR(17);
    DECLARE marca VARCHAR(50);
    DECLARE modelo VARCHAR(50);
    DECLARE anio INT;
    DECLARE color VARCHAR(20);
    DECLARE tipo VARCHAR(50);
    DECLARE precio DECIMAL(10, 2);
    DECLARE fecha_recepcion DATETIME;

    WHILE i <= 1000 DO
            SET vin = CONCAT('VIN-', i);
            SET marca = CONCAT('Marca ', i);
            SET modelo = CONCAT('Modelo ', i);
            SET anio = FLOOR(1990 + (RAND() * 30));
            SET color = CONCAT('Color ', i);
            SET tipo = CONCAT('Tipo ', i);
            SET precio = FLOOR(1 + (RAND() * 100000));
            SET fecha_recepcion = DATE_ADD('2020-01-01', INTERVAL FLOOR(1 + (RAND() * 365)) DAY);

            INSERT INTO vehiculo (VIN, Marca, Modelo, Anio, Color, Tipo, Precio, Fecha_Recepcion)
            VALUES (vin, marca, modelo, anio, color, tipo, precio, fecha_recepcion);

            SET i = i + 1;
        END WHILE;
END //

CALL InsertarVehiculos();

# Crear 1000 registros en la tabla venta
DELIMITER //

CREATE PROCEDURE InsertarVentas()
BEGIN
    DECLARE i INT DEFAULT 1;
    DECLARE cliente_id INT;
    DECLARE vendedor_id INT;
    DECLARE vin VARCHAR(17);
    DECLARE precio DECIMAL(10, 2);

    WHILE i <= 1000 DO
            SET cliente_id = FLOOR(1 + (RAND() * 1000));
            SET vendedor_id = FLOOR(1 + (RAND() * 1000));
            SET vin = CONCAT('VIN-', FLOOR(1 + (RAND() * 1000)));
            SET precio = FLOOR(1 + (RAND() * 100000));

            INSERT INTO venta (ID_Cliente, ID_Vendedor, VIN, Precio)
            VALUES (cliente_id, vendedor_id, vin, precio);

            SET i = i + 1;
        END WHILE;
END //

CALL InsertarVentas();

# Y eso es, eso es, eso es todo amigos!