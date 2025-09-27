-- Aula 5 - 17/03
-- Configuração de chave estrageira

CREATE DATABASE sprint2;
USE sprint2;

CREATE TABLE aluno(
ra CHAR(8) PRIMARY KEY,
nome VARCHAR(45),
email VARCHAR(45)-- ,
-- fkEmpresa int,
-- CONSTRAINT FKEmp foreign key (fkEmpresa)
	-- REFERENCES empresa(idEmpresa
);

CREATE TABLE empresa(
idEmpresa INT PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(45),
responsavel VARCHAR(45)
) AUTO_INCREMENT = 100;

DESC aluno;

ALTER TABLE aluno ADD COLUMN fkEmpresa INT,
	ADD CONSTRAINT fkEmp FOREIGN KEY (fkEmpresa)
			REFERENCES empresa(idEmpresa);
            
INSERT INTO empresa VALUES
	(null,'C6Bank','Andresa'),
    (null,'Safra','Joana'),
    (null,'Tivit','Tatiana');
    
INSERT INTO aluno VALUES
	('01231999','Isabel','isabel@sptech',100),
    ('01231888','Ex da Isabel','exisabel@sptech',101),
	('01231777','Futuro da Sarah','futuro@sptech',101),
    ('01231666','Sarah','sarah@sptech',100),
    ('01231555','Karma do Pedro','pedro@sptech',100),
    ('01231444','Pedro','pedrosemkarma@sptech',102);
    
SELECT * FROM aluno;

-- JOIN = JUNÇÃO
SELECT
aluno.*,
empresa.nome
FROM aluno JOIN empresa
-- Todo JOIN tem ON
ON idEmpresa = fkEmpresa;

SELECT
aluno.nome,
empresa.nome
FROM aluno JOIN empresa
	ON aluno.fkEmpresa = empresa.idEmpresa;
    
SELECT 
aluno.nome AS NomeAluno,
empresa.nome AS NomeEmpresa
FROM aluno JOIN empresa
	ON aluno.fkEmpresa = empresa.idEmpresa;
    
SELECT * FROM aluno;
UPDATE aluno SET fkEmpresa = 101 
	WHERE ra = '01231444';
    
DELETE FROM empresa WHERE idEmpresa = 102;