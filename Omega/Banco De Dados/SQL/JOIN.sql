USE sprint2;

CREATE TABLE atleta (
idAtleta INT PRIMARY KEY  AUTO_INCREMENT,
Nome  VARCHAR(45),
Modalidade VARCHAR(40),
qtdMedalha INT
);

INSERT INTO atleta  VALUE
	(NULL,'Arthur','Natação','11',1),
    (NULL,'Guedes','Futebol','4',4),
    (NULL,'Cauê','Muay Thai','6',3),
    (NULL,'Dourado','Basquete','15',2),
	(NULL,'Kauan','Futebol','10',2);
    
CREATE TABLE pais (
idPais INT PRIMARY KEY AUTO_INCREMENT,
Nome VARCHAR(30),
Capital VARCHAR(40)
);

INSERT INTO pais (nome, capital) VALUES
	('Egito','Cairo'),
    ('Brasil','Brasilia'),
    ('Emirados Arabes Unidos','Abu Dhabi'),
    ('Canada','Ottawa');

ALTER TABLE atleta ADD COLUMN fkPais INT,
	ADD CONSTRAINT fkP FOREIGN KEY (fkPais)
			REFERENCES pais(idPais);
            
SELECT
atleta.*,
pais.nome
FROM atleta JOIN pais
ON idPais = fkPais;

SELECT
atleta.nome,
pais.nome
FROM atleta JOIN pais
	ON atleta.fkPais = pais.idPais;
    
SELECT
atleta.nome,
pais.nome
FROM atleta JOIN pais
	ON atleta.fkPais = pais.idPais WHERE capital = 'Brasilia';
    


-- Exercicio 02 

CREATE TABLE Album(
idAlbum INT PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(40),
tipo VARCHAR(20),
dtLancamento DATE
) AUTO_INCREMENT = 100;

INSERT INTO Album VALUES 
	(NULL,'Dos Predios','digital','2022-05-13'),
	(NULL,'Tempo De Paz','digital','2015-12-01'),
	(NULL,'Ninguem ta Puro','digital','2022-03-07');
    
ALTER TABLE Album ADD CONSTRAINT chkTipo CHECK (tipo IN('digital', 'fisico'));

CREATE TABLE Musica(
idMusica INT PRIMARY KEY AUTO_INCREMENT,
titulo VARCHAR(40),
genero VARCHAR(40),
artista VARCHAR(40)
);

ALTER TABLE Musica ADD COLUMN fkAlbum INT,
	ADD CONSTRAINT fkAlb FOREIGN KEY (fkAlbum)
			REFERENCES Album(idAlbum);

INSERT INTO Musica VALUES
	(NULL,'Saudades do Tempo','POP','Maneva',101),
    (NULL,'Me perdoa vida','Trap','Veigh',100),
    (NULL,'Migo ou Vida','Funk','MC IG',102),
    (NULL,'So quando ela me quer','Funk','Yunk Vino',102),
    (NULL,'Vida Chique','Trap','Veigh',100);
    
SELECT
Musica.*,
Album.nome
FROM Musica JOIN Album
ON idAlbum = fkAlbum;

SELECT
Musica.titulo,
Album.nome
FROM Musica JOIN Album
	ON Musica.fkAlbum WHERE Titulo = 'So quando ela me quer';
    
SELECT
Musica.titulo,
Album.nome
FROM Musica JOIN Album
	ON Musica.fkAlbum = Album.idAlbum WHERE genero = 'Trap';
    
