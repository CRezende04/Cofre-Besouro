-- Exerçício 01

CREATE DATABASE sprint1;

USE sprint1;

Create Table Atleta(
idAtleta INT PRIMARY KEY,
nome VARCHAR(40),
modalidade VARCHAR(40),
qtdMedalha INT
);

INSERT INTO Atleta
VALUES  ('1','GABRIEL','Futebol','2'),
		('2','Kauan','Futebol','1'),
		('3','Cauê','Handbol','2'),
		('4','Vick','Handbol','5'),
		('5','Kassio','Voleibol','4'),
		('6','Yan','Voleibol','3');
        
INSERT INTO Atleta
VALUES	('7','Breno','Basquete','6'),
		('8','Jhony','Basquete','10');
        
        
SELECT idAtleta, nome, modalidade, qtdMedalha FROM Atleta;
SELECT * FROM Atleta;


SELECT nome, qtdMedalha FROM Atleta;


SELECT * FROM Atleta WHERE modalidade = 'Futebol';

SELECT * FROM Atleta WHERE modalidade = 'Handbol';

SELECT * FROM Atleta WHERE modalidade = 'Voleibol';

SELECT * FROM Atleta WHERE modalidade = 'Basquete';
        

SELECT * FROM Atleta ORDER BY modalidade;

SELECT * FROM Atleta ORDER BY qtdMedalha DESC;


SELECT * FROM Atleta WHERE nome LIKE '%S%';

SELECT * FROM Atleta WHERE nome LIKE 'V%';

SELECT * FROM Atleta WHERE nome LIKE '%O';

SELECT * FROM Atleta WHERE nome LIKE '%U_';


DROP TABLE Atleta;



-- Exerçício 02

Create Table Musica(
idMusica INT PRIMARY KEY,
titulo VARCHAR(40),
artista VARCHAR(40),
genero VARCHAR(40)
);

INSERT INTO Musica
VALUES  ('1','Melodia Alucinógena','DJ AK BR & Dj Darge','Funk'),
		('2','Predominante','Mc Paiva ZS','Funk'),
		('3','Coração De Gelo','WIU','Trap'),
		('4','Hino Dos Mlks','BIN,Orochi & Mc Daniel','Trap'),
		('5','Goosebumps)','Travis Scott & HVME','Eletronica'),
		('6','Piece Of Your Heart','Medusa & Goodboys','Eletronica'),
		('7','Highway to Hell','AC/DC','Rock');
        
        
SELECT idMusica, titulo, artista, genero FROM Musica;
SELECT * FROM Musica;

SELECT titulo, artista FROM Musica;

SELECT * FROM musica WHERE genero = 'Funk';

SELECT * FROM musica WHERE genero = 'Trap';

SELECT * FROM musica WHERE genero = 'Eletronica';

SELECT * FROM musica WHERE genero = 'Rock';


SELECT * FROM musica WHERE artista = 'DJ AK BR & Dj Darge';

SELECT * FROM musica WHERE artista = 'Mc Paiva ZS';

SELECT * FROM musica WHERE artista = 'WIU';

SELECT * FROM musica WHERE artista = 'BIN,Orochi & Mc Daniel';

SELECT * FROM musica WHERE artista = 'Travis Scott & HVME';

SELECT * FROM musica WHERE artista = 'Medusa & Goodboys';

SELECT * FROM musica WHERE artista = 'AC/DC';


SELECT * FROM Musica ORDER BY titulo;

SELECT * FROM Musica ORDER BY artista DESC;


SELECT* FROM Musica WHERE titulo LIKE 'P%';

SELECT* FROM Musica WHERE titulo LIKE '%S';

SELECT* FROM Musica WHERE titulo LIKE '_I%';

SELECT* FROM Musica WHERE titulo LIKE '%L_';

DROP TABLE Musica;



-- Exercício 03


CREATE TABLE Filme(
idFilme INT PRIMARY KEY,
titulo VARCHAR(50),
genero VARCHAR(40),
diretor VARCHAR(40)
);

INSERT INTO Filme
VALUES  ('1','Tropa De ELite','Ação','José Padilha'),
		('2','John Wick','Ação','Chad Stahelski'),
		('3','Arremessando Alto','Comedia','Jeremiah Zagar'),
		('4','Gente Grande','Comedia','Dennis Dugan'),
		('5','Coach Carter - Treino para a Vida','Drama','Thomas Carter'),
		('6','Quebrando as Regras','Drama','Jeff Wadlow'),
		('7','Truque De Mestre','Suspense','Louis Leterrier');


SELECT idFilme, titulo, genero, diretor FROM Filme;
SELECT * FROM Filme;


SELECT titulo, diretor FROM Filme;

SELECT * FROM Filme WHERE genero = 'Ação';

SELECT * FROM Filme WHERE genero = 'Comedia';

SELECT * FROM Filme WHERE genero = 'Drama';

SELECT * FROM Filme WHERE genero = 'Suspense';


SELECT * FROM Filme WHERE diretor = 'José Padilha';

SELECT * FROM Filme WHERE diretor = 'Chad Stahelski';

SELECT * FROM Filme WHERE diretor = 'Jeremiah Zagar';

SELECT * FROM Filme WHERE diretor = 'Dennis Dugan';

SELECT * FROM Filme WHERE diretor = 'Thomas Carter';

SELECT * FROM Filme WHERE diretor = 'Jeff Wadlow';

SELECT * FROM Filme WHERE diretor = 'Louis Leterrier';


SELECT * FROM Filme ORDER BY titulo;

SELECT * FROM Filme ORDER BY diretor DESC;


SELECT* FROM Filme WHERE titulo LIKE 'T%';

SELECT* FROM Filme WHERE titulo LIKE '%E';

SELECT* FROM Filme WHERE titulo LIKE '_R%';

SELECT* FROM Filme WHERE titulo LIKE '%T_';

DROP TABLE Filme;



-- Exercício 04


CREATE TABLE Professor(
idProfessor INT PRIMARY KEY,
nome VARCHAR(50),
especialidade VARCHAR(40),
dtNasc date
);


INSERT INTO Professor
VALUES  ('1','Rafael','Matematica','1980-05-20'),
		('2','Paulo','Historia','1985-07-10'),
		('3','Vivian','Banco De Dados','1980-10-15'),
		('4','Marcelo','Educação Fisica','1971-05-14'),
		('5','Francisco','Direito','1950-08-18'),
		('6','Maria Christina','Biologia','1955-03-20'),
		('7','Sandro','Matematica','1980-11-10');


SELECT idProfessor, nome, especialidade, dtNasc FROM Professor;
SELECT * FROM Professor;


SELECT especialidade FROM Professor;

SELECT * FROM Professor WHERE especialidade = 'Matematica';

SELECT * FROM Professor WHERE especialidade = 'Historia';

SELECT * FROM Professor WHERE especialidade = 'Banco De Dados';

SELECT * FROM Professor WHERE especialidade = 'Educação Fisica';

SELECT * FROM Professor WHERE especialidade = 'Direito';

SELECT * FROM Professor WHERE especialidade = 'Biologia';


SELECT * FROM Professor ORDER BY nome;

SELECT * FROM Professor ORDER BY dtNasc DESC;


SELECT* FROM Professor WHERE nome LIKE 'M%';

SELECT* FROM Professor WHERE nome LIKE '%O';

SELECT* FROM Professor WHERE nome LIKE '_A%';

SELECT* FROM Professor WHERE nome LIKE '%L_';

DROP TABLE Professor;



-- Exercício 05


CREATE TABLE Curso(
idCurso INT PRIMARY KEY,
nome VARCHAR(50),
sigla VARCHAR (3),
coordenador VARCHAR(40)
);


INSERT INTO Curso
VALUES  ('1','Banco De Dados','BD','Vivian'),
		('2','Algoritmo','AG','Caio'),
		('3','Projeto Inovação','PI','Fernando');


SELECT idCurso, nome, sigla, coordenador FROM Curso;
SELECT * FROM Curso;


SELECT coordenador FROM Curso;

SELECT * FROM Curso WHERE sigla = 'BD';

SELECT * FROM Curso WHERE sigla = 'AG';

SELECT * FROM Curso WHERE sigla = 'PI';


SELECT * FROM Curso ORDER BY nome;

SELECT * FROM Curso ORDER BY coordenador DESC;


SELECT* FROM Curso WHERE nome LIKE 'B%';

SELECT* FROM Curso WHERE nome LIKE '%O';

SELECT* FROM Curso WHERE nome LIKE '_L%';

SELECT* FROM Curso WHERE nome LIKE '%M_';

DROP TABLE Curso;


DROP DATABASE sprint1;