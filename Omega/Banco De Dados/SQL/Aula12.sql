-- Aula 12 - 05/05
-- Relacionamento N:N e funções matemáticas

-- Escola de Idiomas
CREATE DATABASE EscolaIdiomas;
USE EscolaIdiomas;

CREATE TABLE aluno (
idAluno INT PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(45),
bairro VARCHAR(45)
);

INSERT INTO aluno VALUES
	(NULL,'Bob Esponja','Cerqueira Cesar'),
	(NULL,'Patrick Estrela','Cerqueira Cesar'),
	(NULL,'Gary','Paraiso');
    

CREATE TABLE curso (
idCurso INT PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(45)
) AUTO_INCREMENT = 1000;

INSERT INTO curso VALUES
	(NULL,'Inglês'),
	(NULL,'Espanhol'),
	(NULL,'Mandarim');
    

CREATE TABLE alunoCurso (
idAlunoCurso INT,
fkAluno INT,
fkCurso INT,
dtInicio DATE,
nivel CHAR(2),
nota FLOAT,
CONSTRAINT fkAluno FOREIGN KEY (fkAluno)
	REFERENCES aluno(idAluno),
CONSTRAINT fkCurso FOREIGN KEY (fkCurso)
	REFERENCES curso(idCurso),
CONSTRAINT pkSuperComposta PRIMARY KEY (idAlunoCurso, fkAluno, fkCurso)
);

-- ALTER TABLE alunoCurso DROP CONSTRAINT pkSuperComposta;

INSERT INTO alunoCurso VALUES
	(1, 1, 1000, '2023-01-01', 'B1', NULL),
	(2, 1, 1001, '2023-01-01', 'A1', NULL),
	(3, 2, 1001, '2023-01-01', 'A1', 6.75),
	(4, 2, 1001, '2023-01-01', 'A2', 8),
	(5, 2, 1001, '2023-01-01', 'A3', NULL);
    

SELECT * FROM aluno JOIN alunoCurso
	ON idAluno = fkAluno
    JOIN curso ON idCurso = fkCurso;

SELECT * FROM aluno LEFT JOIN alunoCurso
	ON idAluno = fkAluno
    LEFT JOIN curso ON idCurso = fkCurso;
    
SELECT * FROM aluno RIGHT JOIN alunoCurso
	ON idAluno = fkAluno
    RIGHT JOIN curso ON idCurso = fkCurso;
    
SELECT * FROM aluno LEFT JOIN alunoCurso
	ON idAluno = fkAluno
    LEFT JOIN curso ON idCurso = fkCurso
    WHERE fkCurso IS NULL;
    
SELECT * FROM aluno RIGHT JOIN alunoCurso
	ON idAluno = fkAluno
    RIGHT JOIN curso ON idCurso = fkCurso
    WHERE fkAluno IS NULL;

    
-- FULL OUTER JOIN 
-- UNION

SELECT * FROM aluno LEFT JOIN alunoCurso
	ON idAluno = fkAluno
    LEFT JOIN curso ON idCurso = fkCurso
    WHERE fkCurso IS NULL
UNION
SELECT * FROM aluno RIGHT JOIN alunoCurso
	ON idAluno = fkAluno
    RIGHT JOIN curso ON idCurso = fkCurso
    WHERE fkAluno IS NULL;
    

/* SELECT * FROM aluno FULL OUTER JOIN alunoCurso
	ON idAluno = fkAluno
    FULL OUTER JOIN curso ON idCurso = fkCurso;*/
    

-- Funções Matemáticas
-- COUNT()
SELECT COUNT(*) FROM alunoCurso;
SELECT COUNT(nota) FROM alunoCurso;
SELECT * FROM alunoCurso;

-- Soma SUM()
SELECT SUM(nota) FROM alunoCurso;
SELECT SUM(nota)/COUNT(nota) FROM alunoCurso;

-- Average média AVG()
SELECT AVG(nota) FROM alunoCurso;

-- ROUND()
SELECT ROUND(AVG(nota),2) FROM alunoCurso;


-- TRUNCATE()
SELECT TRUNCATE(AVG(nota),2) FROM alunoCurso;


-- Menor MIN() ou Maior MAX()
SELECT MIN(nota), MAX(nota) FROM alunoCurso;

SELECT MAX(nota), MIN(nota) FROM alunoCurso;

SELECT MAX(nota) as Maior,
	MIN(nota) as Menor
    FROM alunoCurso;
    
SELECT DISTINCT nivel FROM alunoCurso;

SELECT nome,nota FROM aluno JOIN alunoCurso
	ON idAluno = fkAluno
    WHERE nota = (SELECT MAX(nota) FROM alunoCurso);
    
SELECT nome,nota FROM aluno JOIN alunoCurso
	ON idAluno = fkAluno
    WHERE nota = (SELECT MIN(nota) FROM alunoCurso);
    
SELECT nivel, AVG(nota) FROM alunoCurso GROUP BY nivel;






