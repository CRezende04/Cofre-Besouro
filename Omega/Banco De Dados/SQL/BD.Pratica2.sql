-- Criar Tabela
CREATE DATABASE sprint1;
USE sprint1;

-- Exercício 1

-- Criar Table Atleta
CREATE TABLE Atleta(
idAtleta INT PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(40),
modalidade VARCHAR(40),
qtdMedalha INT 
);

-- Inserir Dados da Tabela
INSERT INTO Atleta (nome, modalidade, qtdMedalha)
VALUES  ('GABRIEL','Futebol','2'),
		('Kauan','Futebol','3'),
		('Cauê','Handbol','2'),
		('Vick','Handbol','5'),
		('Kassio','Voleibol','4');

-- Exibir dados da Tabela
SELECT * FROM Atleta;

-- Atualizar a quantidade de medalhas do atleta com id=1;
UPDATE Atleta SET qtdMedalha = 3
	WHERE idAtleta IN (1);
    

-- Atualizar a quantidade de medalhas do atleta com id=2 e com o id=3;
UPDATE Atleta SET qtdMedalha = 5
	WHERE idAtleta IN (2,3);
    

-- Atualizar o nome do atleta com o id=4;
UPDATE Atleta SET nome = 'Victoria'
	WHERE idAtleta IN (4);
    

-- Adicionar o campo dtNasc na tabela, com a data de nascimento dos atletas, tipo date;
ALTER TABLE Atleta ADD COLUMN dtNasc DATE;

-- Atualizar a data de nascimento de todos os atletas;
UPDATE Atleta SET dtNasc = '2005-11-05'
	WHERE idAtleta IN(1);
    
UPDATE Atleta SET dtNasc = '2005-02-23'
	WHERE idAtleta IN(2);
    
UPDATE Atleta SET dtNasc = '2004-06-18'
	WHERE idAtleta IN(3);
    
UPDATE Atleta SET dtNasc = '2005-05-10'
	WHERE idAtleta IN(4);
    
UPDATE Atleta SET dtNasc = '2005-01-15'
	WHERE idAtleta IN(5);
    
-- Excluir o Atleta com o id=5;
DELETE FROM Atleta WHERE idAtleta = 5;


-- Exibir os atletas onde a modalidade é diferente de natação;
SELECT * FROM Atleta WHERE modalidade != 'Futebol';


-- Exibir os dados dos atletas que tem a quantidade de medalhas maior ou igual a 3;
SELECT * FROM Atleta WHERE qtdMedalha >= 3;


-- Modificar o campo modalidade do tamanho 40 para o tamanho 60;
ALTER TABLE Atleta MODIFY COLUMN modalidade VARCHAR(60);


-- Descrever os campos da tabela mostrando a atualização do campo modalidade;
DESC Atleta;

-- Limpar Dados da Tabela
TRUNCATE TABLE Atleta;




-- Exercicio 2

-- Criar Table
CREATE TABLE Musica(
idMusica INT PRIMARY KEY AUTO_INCREMENT,
titulo VARCHAR(40),
artista VARCHAR(40),
genero VARCHAR(40)
);


-- Inserir Dados na Tabela
INSERT INTO Musica(titulo,artista,genero)
VALUES  ('Melodia Alucinógena','DJ AK BR & Dj Darge','Funk'),
		('Predominante','Mc Paiva ZS','Funk'),
		('Coração De Gelo','WIU','Trap'),
		('Hino Dos Mlks','BIN,Orochi & Mc Daniel','Trap'),
		('Goosebumps)','Travis Scott & HVME','Eletronica'),
		('Piece Of Your Heart','Medusa & Goodboys','Eletronica'),
		('Highway to Hell','AC/DC','Rock');

-- Exibir todos os Dados da Tabela
SELECT * FROM Musica;

-- Adicionar o campo curtidas do tipo int na tabela;
ALTER TABLE Musica ADD COLUMN curtidas INT;

-- Atualizar o campo curtidas de todas as músicas inseridas;
UPDATE Musica SET curtidas = 399
	WHERE idMusica = 1;
    
UPDATE Musica SET curtidas = 499
	WHERE idMusica = 2;
    
UPDATE Musica SET curtidas = 599
	WHERE idMusica = 3;
    
UPDATE Musica SET curtidas = 699
	WHERE idMusica = 4;
    
UPDATE Musica SET curtidas = 799
	WHERE idMusica = 5;

UPDATE Musica SET curtidas = 899
	WHERE idMusica = 6;
    
UPDATE Musica SET curtidas = 999
	WHERE idMusica = 7;
    
-- Modificar o campo artista do tamanho 40 para o tamanho 80;
ALTER TABLE Musica MODIFY COLUMN artista VARCHAR (80);

-- Atualizar a quantidade de curtidas da música com id=1;
UPDATE Musica SET curtidas = 199
	WHERE idMusica = 1;
    
-- Atualizar a quantidade de curtidas das músicas com id=2 e com o id=3;
UPDATE Musica SET curtidas = 350
	WHERE idMusica IN (2,3);
    
-- Atualizar o nome da música com o id=5;
UPDATE Musica SET titulo = 'Yosemite'
	WHERE idMusica = 5;
    
-- Excluir a música com o id=4;
DELETE FROM Musica WHERE idMusica = 4;

-- Exibir as músicas onde o gênero é diferente de funk;
SELECT * FROM Musica WHERE genero != 'Funk';

-- Exibir os dados das músicas que tem curtidas maior ou igual a 20;
SELECT * FROM Musica WHERE curtidas >= 500;

-- Descrever os campos da tabela mostrando a atualização do campo artista;
DESC Musica;

-- Limpar os Dados da Tabela 
TRUNCATE TABLE Musica;


-- Exercicio 3


CREATE TABLE Filme(
idFilme INT PRIMARY KEY AUTO_INCREMENT,
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


-- Exibir todos os dados da tabela.
SELECT * FROM Filme;

-- Adicionar o campo protagonista do tipo varchar(50) na tabela;
ALTER TABLE Filme ADD COLUMN protagonista VARCHAR (50);

-- Adicionar o campo protagonista de todos os filme inseridos;
UPDATE Filme SET protagonista = 'Wagner Moura'
	WHERE idFilme = 1;
    
UPDATE Filme SET protagonista = 'Keanu Reeves'
	WHERE idFilme = 2;

UPDATE Filme SET protagonista = 'Juancho Hernangómez'
	WHERE idFilme = 3;

UPDATE Filme SET protagonista = 'Adam Sandler'
	WHERE idFilme = 4;
    
UPDATE Filme SET protagonista = 'Adam Sandler'
	WHERE idFilme = 5;

UPDATE Filme SET protagonista = 'Sean Faris'
	WHERE idFilme = 6;
    
UPDATE Filme SET protagonista = 'Jesse Eisenberg'
	WHERE idFilme = 7;
    
    
-- Modificar o campo diretor do tamanho 40 para o tamanho 150;
ALTER TABLE Filme MODIFY COLUMN diretor VARCHAR (150);

-- Atualizar o diretor do filme com id=5
UPDATE Filme SET diretor = 'Vivian'
	WHERE idFilme = 5;
    
-- Atualizar o diretor dos filmes com id=2 e com o id=7;
UPDATE Filme SET diretor = 'Caio'
	WHERE idFilme IN (2,7);
    
-- Atualizar o título do filme com o id=6;
UPDATE Filme SET titulo = 'Quebrando as Regras 2'
	WHERE idFilme = 6;
    
-- Excluir o filme com o id=3;
DELETE FROM Filme WHERE idFilme = 3;

-- Exibir os filmes em que o gênero é diferente de drama;
SELECT * FROM Filme WHERE genero != 'Drama';

-- Exibir os dados dos filmes que o gênero é igual ‘suspense’;
SELECT * FROM Filme WHERE genero = 'Suspense';

-- Descrever os campos da tabela mostrando a atualização do campo protagonista e diretor;
DESC Filme;

-- Limpas Dados da Tabela
TRUNCATE TABLE Filme;



-- Exercicio 4


CREATE TABLE Professor(
idProfessor INT PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(50),
especialidade VARCHAR(40),
dtNasc date
);


INSERT INTO Professor(nome, especialidade, dtNasc)
VALUES  ('Rafael','Matematica','1980-05-20'),
		('Paulo','Historia','1985-07-10'),
		('Vivian','Banco De Dados','1980-10-15'),
		('Marcelo','Educação Fisica','1971-05-14'),
		('Francisco','Direito','1950-08-18'),
		('Maria Christina','Biologia','1955-03-20'),
		('Sandro','Matematica','1980-11-10');
        
	
-- Exibir todos os dados da tabela.
SELECT * FROM Professor;

-- Adicionar o campo funcao do tipo varchar(50), onde a função só pode ser ‘monitor’,‘assistente’ ou ‘titular’;
ALTER TABLE Professor ADD COLUMN funcao VARCHAR (50),
ADD CONSTRAINT chkFuncao CHECK (funcao IN ('monitor','assistente','titular'));

--  Atualizar os professores inseridos e suas respectivas funções;DROP TABLE Professor;
UPDATE Professor SET funcao = 'Titular'
	WHERE idProfessor = 1;
    
UPDATE Professor SET funcao = 'Assistente'
	WHERE idProfessor = 2;
    
UPDATE Professor SET funcao = 'Titular'
	WHERE idProfessor = 3;

UPDATE Professor SET funcao = 'Titular'
	WHERE idProfessor = 4;
    
UPDATE Professor SET funcao = 'Titular'
	WHERE idProfessor = 5;
    
UPDATE Professor SET funcao = 'Monitor'
	WHERE idProfessor = 6;
    
UPDATE Professor SET funcao = 'Monitor'
	WHERE idProfessor = 7;
    
-- Inserir um novo professor;
INSERT INTO Professor VALUES
	(null,'Fernanda','Projeto Inovação','1990-05-20','Assistente');
    
-- Excluir o professor onde o idProfessor é igual a 5;
DELETE FROM Professor WHERE idProfessor = 5;

-- Exibir apenas os nomes dos professores titulares;
SELECT * FROM Professor WHERE funcao = 'Titular';

-- Exibir apenas as especialidades e as datas de nascimento dos professores monitores;
SELECT especialidade, dtNasc FROM Professor WHERE funcao = 'Monitor';

-- Atualizar a data de nascimento do idProfessor igual a 3;
UPDATE Professor SET dtNasc = '1985-09-10'
	WHERE idProfessor = 3;
    
-- Limpar a Tabela Professor
TRUNCATE TABLE Professor;



-- Exercicio 5


CREATE TABLE Curso(
idCurso INT PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(50),
sigla CHAR (3),
coordenador VARCHAR(40)
);


INSERT INTO Curso(nome, sigla, coordenador)
VALUES  ('Banco De Dados','BD','Vivian'),
		('Algoritmo','AG','Caio'),
		('Projeto Inovação','PI','Fernando');


-- Exibir todos os dados da tabela.
SELECT * FROM Curso;

-- Exibir apenas os coordenadores dos cursos
SELECT coordenador FROM Curso;

--  Exibir apenas os dados dos cursos de uma determinada sigla.
SELECT * FROM Curso WHERE sigla = 'BD';

--  Exibir os dados da tabela ordenados pelo nome do curso
SELECT * FROM Curso ORDER BY nome;

-- Exibir os dados da tabela ordenados pelo nome do coordenador em ordem decrescente
SELECT * FROM Curso ORDER BY coordenador DESC;

-- Exibir os dados da tabela, dos cursos cujo nome comece com uma determinada letra
SELECT * FROM Curso WHERE nome LIKE 'B%';

-- Exibir os dados da tabela, dos cursos cujo nome termine com uma determinada letra.
SELECT * FROM Curso WHERE nome LIKE '%O';

-- Exibir os dados da tabela, dos cursos cujo nome tenha como segunda letra uma determinada letra
SELECT * FROM Curso WHERE nome LIKE '_R%';

-- Exibir os dados da tabela, dos cursos cujo nome tenha como penúltima letra uma determinada letra.
SELECT * FROM Curso WHERE nome LIKE '%O_';

-- Elimine a Tabela 
DROP TABLE Curso;




-- Exercicio 6



CREATE TABLE Revista(
idRevista INT PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(40),
categoria VARCHAR(30)
);

INSERT Revista(nome)
VALUES  ('Vougue'),
		('Placar'),
		('Maxima Receitas');
        
-- Exibir todos os dados da tabela.
SELECT * FROM Revista;

-- Atualize os dados das categorias das 3 revistas inseridas. Exibir os dados da tabela novamente para verificar se atualizou corretamente.
UPDATE Revista SET categoria = 'Moda'
	WHERE idRevista = 1;
    
UPDATE Revista SET categoria = 'Esporte'
	WHERE idRevista = 2;
    
UPDATE Revista SET categoria = 'Comida'
	WHERE idRevista = 3;

-- Insira mais 3 registros completos
INSERT Revista(nome, categoria)
VALUES  ('Bazaar','Moda'),
		('ESPN','Esporte'),
		('Menu','Comida');

-- Exibir novamente todos os dados da tabela.
SELECT * FROM Revista;

-- Exibir a descrição da estrutura da tabela
DESC Revista; 

-- Alterar a tabela para que a coluna categoria possa ter no máximo 40 caracteres
ALTER TABLE Revista MODIFY COLUMN categoria VARCHAR (40);

-- Exibir novamente a descrição da estrutura da tabela, para verificar se alterou o tamanho da coluna categoria
DESC Revista;

-- Acrescentar a coluna periodicidade à tabela, que é varchar(15).
ALTER TABLE Revista ADD COLUMN periodicidade VARCHAR(15);

 --  Exibir os dados da tabela.
 SELECT * FROM Revista;
 
 -- Excluir a coluna periodicidade da tabela.
ALTER TABLE Revista DROP COLUMN periodicidade;


USE sptechc;

-- datetime '2023-03-03 13:50:01'
-- tinyint 0-255
-- default - configuração padrão do campo
-- constraint

CREATE TABLE professor (
id INT PRIMARY KEY auto_increment,
nome VARCHAR(50),
especialidade VARCHAR(40) default 'Sem Especialidade',
genero char(1), constraint chkGenero CHECK
	(genero IN ('f','m','n')),
dtAtual DATETIME default current_timestamp,
sttAtual tinyint
);

INSERT INTO professor (genero) VALUES ('m');

SELECT * FROM professor;

INSERT INTO professor (nome, sttAtual) VALUES
		('Dell Vale',0),
        ('Tang', 1),
        ('Sukita', 2);
        
UPDATE professor SET sttAtual = 1
	WHERE id=4;
    
ALTER TABLE professor ADD CONSTRAINT chksttAtual CHECK (sttAtual IN (0,1));
    
DELETE FROM professor WHERE id = 4;

INSERT INTO professor (nome, sttAtual) VALUES ('Ki Suco', 1);
    
SELECT * FROM professor;

ALTER TABLE professor auto_increment = 1000;

INSERT INTO professor (nome, especialidade) VALUES ('Coca','cola');
SELECT * FROM professor;

-- o professor com o nome xpto tem a especialidade x
SELECT concat('O Professor com o nome  ', nome, ' tem a especialidade ', especialidade) FROM professor;

-- Apelidar (alias)
SELECT concat('O Professor com o nome  ', nome, ' tem a especialidade ', especialidade) AS Frase FROM professor;
SELECT nome AS 'Nome do Professor' FROM professor;
SELECT especialidade AS especial, sttAtual AS 'Status Atual' FROM professor;

