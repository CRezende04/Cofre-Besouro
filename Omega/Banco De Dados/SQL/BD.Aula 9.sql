-- Aula 9 e 10 - Revisao e Reforço

CREATE DATABASE revisao;
USE revisao;

CREATE TABLE treinador (
idTreinador INT PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(45),
sobrenome VARCHAR(45), -- + nome = atributo composto
telFixo CHAR(11),
telMovel CHAR(12), -- + nome = atributo composto
fkExperiente INT,
CONSTRAINT fkNovatoExperiente FOREIGN KEY (fkExperiente)
REFERENCES treinador(idTreinador)
);

-- Inserir os Treinadore experientes, fkExperiente = null
INSERT INTO treinador VALUES
	(NULL,'Azul','Marinho','11-98767898',NULL,NULL),
	(NULL,'Rosa','Pink',NULL,'11-98767898',NULL);
    
-- Inserir os treinadores novatos, fkExperiente tem algum valor
INSERT INTO treinador VALUES
	(NULL,'Verde','Musgo',NULL,NULL,1),
	(NULL,'Amarelo',NULL,NULL,NULL, 1),
	(NULL,'Laranja',NULL,NULL,NULL, 2);
    
UPDATE treinador SET fkExperiente = 2 WHERE idTreinador = 1;

SELECT novato.nome AS NomeNovato,
experiente.nome AS NomeExperiente
	FROM treinador AS novato JOIN treinador AS experiente
		ON novato.fkExperiente = experiente.idTreinador; 


CREATE TABLE nadador (
idNadador INT PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(45),
dtNasc DATE,
fkTreinador INT,
constraint fkNadadorTreinador FOREIGN KEY (fkTreinador)
REFERENCES treinador(idTreinador)
)AUTO_INCREMENT = 100;

INSERT INTO nadador VALUES 
	(NULL,'Vermelho','2013-10-10',1),
	(NULL,'Preto','2005-10-10',3),
	(NULL,'Branco','2003-10-10',2),
	(NULL,'Cinza','2000-10-10',2);
    
SELECT * FROM nadador;

SELECT * FROM nadador JOIN treinador
	ON fkTreinador = idTreinador;
    
SELECT nadador.nome AS NadadorNome,
treinador.nome AS TreinadorNome
	FROM nadador JOIN treinador
    ON fkTreinador = idTreinador;
    
SELECT * FROM nadador INNER JOIN treinador
	ON fkTreinador = idTreinador;
    
SELECT concat(treinador.nome,' ',treinador.sobrenome) AS NomeCompleto 
	FROM treinador;
    
SELECT concat(treinador.nome,' ',
ifnull(treinador.sobrenome,'Silva'	)) AS NomeCompleto 
	FROM treinador;
    
CREATE TABLE convidado (
idConvidado INT ,
nome VARCHAR(45),
fkQConvidou INT,
CONSTRAINT fkQConvidou FOREIGN KEY (fkQConvidou)
REFERENCES nadador(idNadador),
CONSTRAINT pkComposta PRIMARY KEY (idConvidado,fkQConvidou)
);

-- FK nao pode ser nula pois ela tbm é PK da tabela composta
INSERT INTO convidado VALUES
	(1,'Shitzu',100),
	(2,'Poodle',100),
	(1,'Vira Lata',101),
	(1,'Pinscher',102);
    
UPDATE convidado SET nome = 'Vira Lata'
	WHERE idConvidado = 1 AND fkQConvidou = 101;
    
SELECT * FROM convidado;
SELECT * FROM convidado ORDER BY fkQConvidou;

SELECT novato.nome AS NomeNovato,
	experiente.nome AS NomeExperiente,
	nadador.nome AS NomeNadador,
    convidado.nome AS NomeConvidado
    FROM treinador AS novato JOIN treinador AS experiente
	ON novato.fkExperiente = experiente.idTreinador
    JOIN nadador ON nadador.fkTreinador = novato.idTreinador
    JOIN convidado ON convidado.fkQConvidou = nadador.idNadador;
    
