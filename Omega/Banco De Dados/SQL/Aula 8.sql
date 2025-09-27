-- AULA 08 - 31/03
-- Tipos de Relacionamentos, entidades e atributos

-- Exercicio Funcionario X Dependete (Plano de Saude)

CREATE DATABASE saude;
USE saude;

CREATE TABLE funcionario(
idFunc INT PRIMARY KEY auto_increment, -- Atributo Identificador
nome VARCHAR(45), -- + Sobrenome == Atributo Composto
sobrenome VARCHAR(45),
cep CHAR(9), -- + Complemento = Atributo Multivalorado
complemento VARCHAR(45)
);

INSERT INTO funcionario VALUES
	(null,'Xororó','Lima','01414905',' num 9 , apto 110'),
	(null,'Chitãozinho','Lima','01414905',' num 9, apto 120'),
	(null,'Sandy','Lima','01414905',' num 9 , apto 130'),
	(null,'Junior
    ','Lima','01414905',' num 9 , apto 140');
    
SELECT * FROM funcionario;

CREATE TABLE dependente (
idDep INT auto_increment,
nome VARCHAR(45),
parentesco VARCHAR(45),
dtNasc DATE,
fkFunc INT,
CONSTRAINT fkFuncDep FOREIGN KEY (fkFunc) REFERENCES funcionario(idFunc),
CONSTRAINT pkCompostaDep PRIMARY KEY (idDep,fkFunc) -- Chave primaria comp
) auto_increment = 100;

INSERT INTO dependente VALUES
	(null,'Lucas','Marido','1984-01-1', 3),
	(null,'Theo','Filho','2006-01-1', 3),
	(null,'Noeli','Esposa','2006-01-1', 1);
    
SELECT * FROM dependente;

UPDATE dependente SET dtNasc = '1954-01-01' WHERE idDep = 102;

SELECT * FROM funcionario JOIN dependente
	ON idFunc = fkFunc;
    
SELECT nome ,
timestampdiff(YEAR, dtNasc, now()) as idade FROM dependente;

SELECT nome ,
timestampdiff(DAY, dtNasc, now()) as idade FROM dependente;

SELECT concat(cep,'',complemento) as endereço FROM funcionario;

SELECT * FROM funcionario LEFT JOIN dependente 
	ON idFunc = fkFunc;

SELECT * FROM dependente INNER JOIN funcionario 
	ON idFunc = fkFunc;

SELECT * FROM dependente RIGHT JOIN funcionario 
	ON idFunc = fkFunc
    WHERE fkFunc is null;
    
/* 
join em mais de 2 tabelas 
SELECT * FROM TB1 JOIN 	tb2 on id = fk
	JOIN tb3 on id = fk;
*/
