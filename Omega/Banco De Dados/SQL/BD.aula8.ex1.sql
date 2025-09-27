CREATE DATABASE sprint1;
USE sprint1;

CREATE TABLE professor(
idProf INT PRIMARY KEY auto_increment,
nome VARCHAR(45),
sobrenome VARCHAR(45),
especialidade1 VARCHAR(45),
especialidade2 VARCHAR(45)
);

INSERT INTO professor VALUES

	(null,'Xororó','Lima','Biologia','Matematica'),
	(null,'Chitãozinho','Lima','Matematica','Fisica'),
	(null,'Brandao','Lima','PI','SocioEmocional'),
	(null,'Vivian','Lima','BD','Algoritmo'),
    (null,'Junior','Lima','Historia','Fisica'),
    (null,'JP','Lima','Algoritmo','SocioEmocinal');
    
CREATE TABLE disciplina (
idDisc INT auto_increment,
nomeDisc VARCHAR(45),
fkProf INT,
CONSTRAINT fkProfDisc FOREIGN KEY (fkProf) REFERENCES professor(idProf),
CONSTRAINT pkCompostaDisc PRIMARY KEY (idDisc,fkProf)
) auto_increment = 100;

INSERT INTO disciplina VALUES
	(null,'Matematica',1),
	(null,'Fisica',2),
	(null,'SocioEmocional',3);
    
SELECT * FROM professor LEFT JOIN disciplina 
	ON idProf = fkProf;
    
SELECT concat(nome,'  ',especialidade1) as disciplina FROM professor;

SELECT nome FROM professor INNER JOIN disciplina;








-- Exercicio 02
CREATE DATABASE sprint2;
USE sprint2;

CREATE TABLE curso(
idCurso INT PRIMARY KEY auto_increment,
nome VARCHAR(50),
sigla CHAR(3),
coordenador VARCHAR(50)
);

INSERT INTO curso VALUES
	(null,'Banco De Dados','BD','Vivian'),
	(null,'Algoritmo','AGT','Caio'),
	(null,'SocioEmocional','SC','Vera');
    
CREATE TABLE auxiliar (
idAux INT auto_increment,
nomeAux VARCHAR(45),
fkCurso INT,
CONSTRAINT fkCursoAux FOREIGN KEY (fkCurso) REFERENCES curso(idCurso),
CONSTRAINT pkCompostaAux PRIMARY KEY (idAux,fkCurso)
) auto_increment = 100;

INSERT INTO auxiliar VALUES
	(null,'Nenhum',1),
	(null,'JP',2),
	(null,'Marcela',3);
    
SELECT * FROM curso LEFT JOIN auxiliar 
	ON idCurso = fkCurso;
    
SELECT * FROM auxiliar RIGHT JOIN curso 
	ON idCurso = fkCurso
    WHERE fkCurso is null;