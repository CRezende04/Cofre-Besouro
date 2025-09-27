CREATE DATABASE TermoGuard;
USE TermoGuard;

CREATE TABLE empresa (
idEmpresa INT PRIMARY KEY,
nomeFantasia VARCHAR(45),
cnpj CHAR(18)
);

CREATE TABLE usuario (
idUsuario INT PRIMARY KEY AUTO_INCREMENT,
email VARCHAR(45),
senha VARCHAR(30),
fkEmpresa INT,
CONSTRAINT fkEmpresa FOREIGN KEY (fkEmpresa) REFERENCES empresa(idEmpresa)
)AUTO_INCREMENT = 100;

