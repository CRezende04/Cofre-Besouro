CREATE DATABASE GameSelect;
USE GameSelect;
-- drop database GameSelect;

CREATE TABLE marca (
idMarca INT PRIMARY KEY AUTO_INCREMENT,
NomeModelo VARCHAR(45),
Modelo VARCHAR(45),
Ano CHAR(4)
)AUTO_INCREMENT = 100;

INSERT INTO marca VALUES 
	(NULL,'Chevrolet','Chevette','1976'),
	(NULL,'Chevrolet','Chevelle','1970'),
	(NULL,'Chevrolet','Opala','1979'),
	(NULL,'Chevrolet','Impala','1969'),
	(NULL,'Nissan','Skyline KGC10','1980'),
	(NULL,'Nissan','Fairlady Z 432','1969'),
	(NULL,'Nissan','Skyline R32','1989'),
	(NULL,'Volkswagen','Fusca-Azul','1989'),
	(NULL,'Volkswagen','Brasilia-Amarela','1989');

CREATE TABLE funcionario (
idFuncionario INT PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(45),
salario DECIMAL(10,2)
)AUTO_INCREMENT = 1000;

INSERT INTO funcionario VALUES 
	(null, 'Kowalski','10000'),
    (null, 'Rian','30000'),
    (null, 'Gustavo','30000'),
    (null, 'Jubiscleiton','1000'),
    (null, 'Cauê','30000'),
    (null, 'Zoi de Gato','5000'),
    (null, 'Felipe Boladão','1000'),
    (null, 'DaLeste','30000'),
    (null, 'McKevin','50000'),
    (null, 'Cabeça Branca','90000');

CREATE TABLE concessionaria (
idConcessionaria INT PRIMARY KEY AUTO_INCREMENT,
NomeConcessionaria VARCHAR(45),
CEP CHAR(9),
CNPJ CHAR(14),
fkFuncionario INT,
CONSTRAINT fkFuncionario FOREIGN KEY (fkFuncionario) REFERENCES funcionario(idFuncionario)
);


INSERT INTO concessionaria VALUES
(null, 'Simas-Turbo', '123456789', '2143658709', 1004),
(null, 'SoLoveCars', '987654321', '2143658709', 1005),
(null, 'Car-Tucho', '123987456', '2143658709', 1002),
(null, 'DinheiroCar-Teira', '789321654', '2143658709', 1008),
(null, 'NFS-Wanted', '642318957', '2143658709', 1001),
(null, 'Velhice-Turbo', '213546879', '2143658709', 1000),
(null,'Torretos-Retro', '798465231', '2143658709', 1009),
(null,'You-FordCar', '312465879', '2143658709', 1007),
(null,'Dadinh`sCar', '769835421', '2143658709', 1006),
(null,'DSM MultiMarcas', '591728364', '2143658709', 1003);


CREATE TABLE TipoDeModelo (
idTipoDeModelo INT PRIMARY KEY AUTO_INCREMENT,
Tipo VARCHAR(45)
);

INSERT INTO TipoDeModelo VALUES 
	(1,'Retro');

CREATE TABLE concessionariaMarca (
idConcessionariaMarca INT AUTO_INCREMENT,
fkConcessionaria INT,
fkMarca INT,
CONSTRAINT fkConsessionaria FOREIGN KEY (fkConcessionaria) REFERENCES concessionaria(idConcessionaria),
CONSTRAINT fkMarca FOREIGN KEY (fkMarca) REFERENCES marca(idMarca),
CONSTRAINT pkConcessionariaMarca PRIMARY KEY (idConcessionariaMarca,fkConcessionaria,fkMarca)
)AUTO_INCREMENT = 10000;


SELECT * FROM marca;

SELECT * FROM funcionario;

SELECT * FROM concessionaria;
