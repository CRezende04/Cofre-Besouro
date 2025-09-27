-- Toda tabela tem uma chave prímaria
-- Todo comando é em ingles
-- Todo Comando termina com ;
 
-- Criar o Banco de Dados (SCHEMA OU DATABASE)
CREATE DATABASE sptechc;

-- Utilizar o Banco de Dados
USE sptechc;

-- Criar Nossa Primeira Tabela
Create Table aluno(
-- nomeCampo tipagem restrição/constraint
ra char(8) primary key,
nome varchar(100),
bairro varchar (50)

-- Char comando utilizado para campos com a quantidade caracteres especificos
-- Varchar comando utilizado para campos com a quantidade de caracteres não especificado
);

-- Descrever a estrutura da nossa tabela
Describe aluno;
Desc aluno;

-- Inserir Dados na Tabela
Insert Into aluno 
Values ('01231198','Amanda','Tucuruvi');

Insert Into aluno
Values ('01231042','Theo','Guilhermina'),
       ('01231022','Felipe','Vila Andrade'),
       ('01231092','Kat','Itam Paulista'),
       ('01231079','João','Vilas Assis'),
       ('01231170','Cauê','Tucuruvi');
-- Exibir os Dados da tabela
Select ra, nome, bairro From aluno;
Select * From aluno;

-- Excluiar a tabela aluno
DROP TABLE aluno;

-- Adicionar um Campo na Tabela aluno
ALTER TABLE aluno ADD COLUMN email VARCHAR(100) NOT NULL;
DESCRIBE aluno;

ALTER TABLE aluno ADD COLUMN dtNasc VARCHAR(100) NOT NULL;
DESCRIBE aluno;

-- Atualizar os Emails dos Alunos
UPDATE aluno SET email = 'cauê@sptech.school'
	WHERE ra = '01231170';

-- Inserir um Novo Aluno,porém apenas os campos RA,EMAIL,DTNASC
-- Data formato americano 'AAAA-MM-DD'
INSERT INTO aluno (ra,email,dataNasc) VALUES
	('01231170', 'cauê@sptech.school', '2004-06-18');

-- Modificar a Tipagem de um curso
ALTER TABLE aluno MODIFY COLUMN nome VARCHAR(120);
DESC aluno;

-- Renomar um Campo Da Tabela
ALTER TABLE aluno RENAME COLUMN dtnasc TO dataNasc;

-- Excluir uma tupla/linha inteira
DELETE FROM aluno WHERE ra='01231170';
SELECT * FROM aluno ;

-- Excluir a Coluna datanasc
ALTER TABLE aluno DROP COLUMN dataNasc;
DESC aluno;

-- SELECTS Marotos
-- Exibir o Aluno cujo o Nome é Kat
SELECT * FROM aluno WHERE nome = 'Kat';

-- Exibir apenas o Bairro da Kat
SELECT bairro FROM aluno WHERE nome = 'Kat';
SELECT ra,email FROM aluno WHERE nome = 'Kat';

SELECT * FROM aluno;

-- Exibir os dados dos alunos ordenados pelo nome em ordem descrescente e crescente
SELECT * FROM aluno ORDER BY nome;
SELECT * FROM aluno ORDER BY nome DESC;

-- Exibir os Dados dos alunos cujo o nome começa com a letra A
SELECT * FROM aluno WHERE nome LIKE 'A%';
SELECT * FROM aluno WHERE nome LIKE '%O';
SELECT * FROM aluno WHERE bairro LIKE '%SS%';

-- Exibir os Dados dos alunos cujo a terceira letra do nome é E
SELECT * FROM aluno WHERE nome LIKE '__E%';

-- Criar a Tabela Empresa
CREATE TABLE empresa(
id INT PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(100),
responsavel VARCHAR(100)
);

INSERT INTO empresa(nome,responsavel)VALUES
	('C6 BANK','ANDRESA'),
    ('BOX DELIVERY','ERICA');
    
SELECT * FROM empresa;

-- LIMPAR A TABLE
TRUNCATE TABLE empresa;


-- Campos Do Tipo Numérico
-- Números Inteiros (INT)
-- Numeros Decimais
-- Float: 7 Digitos 1234567
-- Double: 15 Digitos 123456789012345
-- Decimal (Total,QTDNUMPOSVIRGULA)
-- Decimal(5,2) 123,45
-- Decimal (7,4) 123,4567

CREATE TABLE Pessoa(
id INT PRIMARY KEY auto_increment,
nome VARCHAR(50) NOT NULL,
peso FLOAT,
altura FLOAT,
salario DECIMAL(5,2),
CONSTRAINT chkSalario CHECK (salario >= 0)
)auto_increment = 100;

-- CONSTRAINT (RESTRIÇÃO OU CONFIGURAÇÃO)
-- CHECK
-- NOT NULL
-- PRIMARY KEY

DESC Pessoa;

-- Check peso e na altura
ALTER TABLE Pessoa 
	ADD constraint chkPeso CHECK (peso>=0),
	ADD constraint chkAltura CHECK (altura>=0);
    
-- Este comando tem que dar erro
INSERT INTO Pessoa VALUES
	(null,'Marcos',90.4,210,-9.99);
-- Error Code: 3819. Check constraint 'chkSalario' is violated.


INSERT INTO Pessoa VALUES    
	(null,'Durant',90.4,210,399.99),
	(null,'Hortencia',78.6,174,99.99),
	(null,'Oscar',110.2,205,99.99);
    
-- Selecionando os dados da Tabela
SELECT * FROM Pessoa;

-- Exibir as Pessoas cujo o nome a terceira letre é R
SELECT * FROM Pessoa WHERE nome LIKE '__r%';

-- Exibir as Pessoas cujo a altura é diferente de 210
SELECT * FROM Pessoa WHERE altura <> 210;
SELECT * FROM Pessoa WHERE altura != 210;

-- Exibir as Pessoas cujo a altura é igual a 210 e 205
SELECT * FROM Pessoa WHERE altura = 210 or altura = 205;
SELECT * FROM Pessoa WHERE altura IN (210,205);

UPDATE Pessoa SET salario = 199.99
	WHERE id IN (101,102);
    
DELETE FROM Pessoa WHERE id = 102;

SELECT * FROM Pessoa;


-- id 103
INSERT INTO Pessoa VALUES
	(null,'James',115,212,999.99);
    
TRUNCATE TABLE Pessoa;

INSERT INTO Pessoa VALUES
	(null,'Jordan',99.7,199,976.90);
    
SELECT * FROM Pessoa;

DROP DATABASE sptechc;