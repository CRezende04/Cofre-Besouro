-- Aula 11 - 28/04
-- Introdução a Relacionamento N:N

CREATE DATABASE Sprint3;
USE Sprint3;

CREATE TABLE paciente (
idPaciente INT PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(45),
genero CHAR(1),
CONSTRAINT chkGenero
	CHECK(genero IN ('F','M','N')));
    
    
INSERT INTO paciente VALUES
	(NULL,'Coração','N'),
	(NULL,'Intestino','M'),
	(NULL,'Ovário','F');
    

CREATE TABLE medico (
idMedico INT PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(45),
especialidade VARCHAR(45)) AUTO_INCREMENT = 1000;


INSERT INTO medico VALUES
	(NULL,'Aorta','cardiologista'),
	(NULL,'Delgado','endocrinologista'),
	(NULL,'Útero','ginecologista');
    
    
-- Vamos criar a tabela associativa

CREATE TABLE consulta (
idConsulta INT,
fkPaciente INT,
CONSTRAINT fkPacienteConsulta FOREIGN KEY (fkPaciente)
	REFERENCES paciente(idPaciente),
fkMedico INT,
CONSTRAINT fkMedicoConsulta FOREIGN KEY (fkMedico)
	REFERENCES medico(idMedico),
dtConsulta DATETIME DEFAULT CURRENT_TIMESTAMP,
CONSTRAINT pkAssociativa PRIMARY KEY (idConsulta, fkPaciente, fkMedico));


SELECT * FROM paciente;
SELECT * FROM medico;


INSERT INTO consulta VALUES
	(1,1,1000,DEFAULT),
	(1,2,1001,DEFAULT),
	(1,3,1002,DEFAULT);
    

SELECT * FROM paciente JOIN consulta 
ON idPaciente = fkPaciente JOIN medico 
ON idMedico = fkMedico;

INSERT INTO consulta VALUES
	(2,1,1000,DEFAULT);
    

/* 1 Paciente Tem 1 OU MUITOS endereços 1 ENDEREÇO é de 1  ou muitos PACIENTE*/

CREATE TABLE endereço (
idEndereço INT PRIMARY KEY AUTO_INCREMENT,
rua VARCHAR(45),
bairro VARCHAR(45)) AUTO_INCREMENT = 100;


INSERT INTO endereço VALUES
	(NULL,'Rua Haddock Lobo','Paulista Pernambucana'),
	(NULL,'Rua Augusta','Consolação'),
	(NULL,'Rua Oscar Feire','Higeanopolis Mackenzie');
  

CREATE TABLE local_de_encontro (
idLocal INT,
fkPaciente INT,
CONSTRAINT fkPacienteLocal FOREIGN KEY (fkPaciente)
	REFERENCES paciente(idPaciente),
fkEndereço INT,
CONSTRAINT fkEndereçolocal FOREIGN KEY (fkEndereço)
	REFERENCES endereço(idEndereço),
numero CHAR (5),
complemento CHAR(10),
CONSTRAINT pkAssociativa PRIMARY KEY (idLocal, fkPaciente, fkEndereço));


SELECT * FROM paciente;
SELECT * FROM endereço;


INSERT INTO local_de_encontro VALUES
	(1,1,100,151,DEFAULT),
	(1,2,101,171,DEFAULT),
	(1,3,102,191,DEFAULT);
    
SELECT * FROM paciente JOIN local_de_encontro 
	ON idPaciente = fkPaciente JOIN endereço 
	ON idEndereço = fkEndereço;
    