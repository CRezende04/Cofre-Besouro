-- EXERCICIO 01

CREATE DATABASE Lista6;
USE Lista6;

CREATE TABLE cliente (
idCliente INT PRIMARY KEY auto_increment, 
nome VARCHAR(45),
sobrenome VARCHAR(45),
telefone_fixo VARCHAR(20),
telefone_celular VARCHAR(20),
estado VARCHAR(45),
cidade VARCHAR(45),
bairro VARCHAR(45),
rua VARCHAR(100),
numero VARCHAR(10)
);

INSERT INTO cliente VALUES
	(null, 'Cauê', 'Rezende', '2930-1234', '11994863-9483', 'São Paulo', 'São Paulo', 'Vila Izolina Mazzei', 'Rua Cristovão Lins', '454'),
    (null, 'Marcelo', 'Rezende', '1238-9025', '11991827-2973', 'São Paulo', 'São Paulo', 'Vila Izolina Mazzei', 'Rua Cristovão Lins', '454'),
    (null, 'Alice', 'Carvalho', '2342-1231', '11992900-3498', 'São Paulo', 'São Paulo', 'Vila Maria', 'Rua ', '432'),
    (null, 'Nicolly', 'Juliane', '3480-0349', '11998394-7234', 'São Paulo', 'São Paulo', 'Grajau', 'Rua 1 De Abril ','222'),
    (null, 'Felipe', 'Dourado', '4378-3484', '11991287-3948', 'São Paulo', 'São Paulo', 'Grajau', 'Rua 1 De Abril', '333'),
    (null, 'Carlos', 'Gomes', '4830-9274', '119492135-5663', 'São Paulo', 'São Paulo', 'Itaquera', 'Rua tatuape brasil', '543');

CREATE TABLE pet (
idpet INT auto_increment,
tipo VARCHAR(45), 
nome VARCHAR(45),
raça VARCHAR(45),
dtNasc DATE,
fkCliente INT, 
PRIMARY KEY (idpet, fkCliente),
FOREIGN KEY (fkCliente) REFERENCES cliente(idCliente)
) AUTO_INCREMENT = 101;
    
insert into pet values
	(null, 'Cachorro', 'Odin', 'Bull-Terrier', '2012-08-01', 1),
    (null, 'Gato', 'Malhado', 'siames', '2015-12-25', 3),
    (null, 'Chachorro', 'Jade', 'Bull-Terrier', '2023-01-19', 2),
	(null, 'Cachorro', 'Frigga', 'Bull-Terrier', '2009-09-30', 1),
    (null, 'Gato','Bola de Pelo', 'himalaio', '2017-02-24', 4);
    
SELECT * FROM cliente;
SELECT * FROM pet;

ALTER TABLE cliente MODIFY COLUMN nome varchar(50);

SELECT * FROM pet WHERE tipo = 'Chachorro';
SELECT nome, dtNasc FROM pet;
SELECT * FROM pet ORDER BY nome;
SELECT * FROM cliente ORDER BY bairro DESC;
SELECT * FROM pet WHERE nome like 'F%';
SELECT * FROM cliente WHERE sobrenome = 'Rezende';

UPDATE cliente SET telefone_fixo = '8972-9874' 
	WHERE idCliente = 3;
    
SELECT * FROM cliente;
SELECT * FROM cliente JOIN pet
	ON idCliente = fkCliente;
SELECT * FROM cliente JOIN pet 
	ON idCliente = fkCliente WHERE idCliente = 1;
DELETE FROM pet where idPet = 104;

SELECT * FROM pet;

DROP TABLE pet, cliente;


-- EXERCICIO 02


CREATE TABLE pessoa (
idPessoa INT PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(45),
dtNasc DATE,
profissao VARCHAR(45)
);
    
INSERT INTO pessoa VALUES
	(null, 'Cauê', '2004-06-18', 'Estudante'),
    (null, 'Felipe', '2005-03-14', 'Estudante'),
    (null, 'Nicolly', '2004-05-03','Estudante'),
    (null, 'Marcelo', '1974-03-15', 'Policial'),
    (null, 'Erika', '1985-10-30', 'Policial');
    
CREATE TABLE gasto (
idGasto INT AUTO_INCREMENT,
valor VARCHAR(45),
descricao VARCHAR(200),
dtGasto DATE,
fkPessoa INT,
PRIMARY KEY (idGasto, fkPessoa),
FOREIGN KEY (fkPessoa) REFERENCES pessoa(idPessoa)
);

INSERT INTO gasto VALUES
	(null, '2022-11-18', 'R$550,50', 'Rodizio de Sushi', 1),
    (null, '2023-01-01', 'R$50,00', 'Ifood', 3),
    (null, '2023-02-25', 'R$68,89', 'Comida', 4),
    (null, '2023-01-12', 'R$499,99', 'Video Game', 1),
    (null, '2023-03-31', 'R$44,55', 'Cinema', 2);
    
SELECT * FROM pessoa;
SELECT * FROM gasto;
SELECT * FROM pessoa WHERE profissao = 'Policial';
SELECT * FROM gasto WHERE descricao = 'Cinema';
SELECT * FROM pessoa JOIN gasto
	ON fkPessoa = idPessoa;
SELECT * FROM pessoa JOIN gasto 
	ON fkPessoa = idPessoa WHERE nome = 'Cauê';

UPDATE gasto SET valor = 'R$250,00' where idGasto = 1 ;
UPDATE pessoa SET profissao = 'Estagiário' WHERE idPessoa = 2;

DELETE FROM pessoa WHERE profissao = 'VideoGame';
DELETE FROM gasto WHERE descricao = 'Cinema';
DROP TABLE pessoa, gasto;


-- EXERCICIO 03


CREATE TABLE setor (
idSetor INT PRIMARY KEY AUTO_INCREMENT,
NSetor VARCHAR(45),
andar INT);
    
CREATE TABLE funcionario (
idFunc INT PRIMARY KEY AUTO_INCREMENT,
NFunc VARCHAR(45),
telefone_celular VARCHAR(20),
telefone_fixo VARCHAR(20),
salario DECIMAL(10,2) CHECK (salario > 0),
fkSetor INT,
FOREIGN KEY (fkSetor) REFERENCES setor(idSetor)
);

CREATE TABLE acompanhante (
idAcompanhante INT,
fkFunc INT,
nome VARCHAR(45),
relacao VARCHAR(45),
dtNasc DATE,
PRIMARY KEY (fkFunc, idAcompanhante),
FOREIGN KEY (fkFunc) REFERENCES funcionario(idFunc)
);
  
INSERT INTO setor VALUES 
	(null, 'Tecnologia', 3),
    (null, 'Investimentos', 4),
    (null, 'Vendas', 2),
    (null, 'Design', 1);

INSERT INTO funcionario VALUES
	(null, 'Cauê', '119984734-6904', '1827-5314', '8724.00', 1),
	(null, 'Felipe', '11992348-6342', '2972-9342', '9724.44', 3),
    (null, 'Nicolly', '11994522-2355', '1027-3410', '9824.12', 2),
    (null, 'Nicolas', '11993409-3344', '9873-3249', '1235.24', 1),
    (null, 'Gabriel', '11997253-3423', '2384-2358', '8123.34', 3),
    (null, 'Maria', '11998123-1263', '1209-9823', '8127.12', 4),
    (null, 'Joao', '11991274-4533', '8912-1208', '0912.23', 2),
    (null, 'Pedro', '11992738-1293', '0812-9182', '9823.12', 4);
    
INSERT INTO acompanhante VALUES
	(1,1, 'Duda', 'Prima', '2004-12-12'),
    (2,1, 'Augusto', 'Irmão', '2005-03-11'),
    (3,1, 'Maria', 'Tia', '1990-06-25'),
    (4,6, 'Antonio', 'Tio', '1985-01-03'),
    (5,2, 'Francisco', 'Avô', '1975-04-30'),
    (6,5, 'Maria Helena', 'Avó', '1975-05-01'),
    (7,4, 'Marcelo', 'Pai', '1989-05-01'),
    (8,2, 'Paulo', 'Pai', '1994-11-25');
    
SELECT * FROM setor;
SELECT * FROM funcionario;
SELECT * FROM acompanhante;
SELECT * FROM setor JOIN funcionario
	ON fkSetor = idSetor;
SELECT * FROM setor JOIN funcionario 
	ON fkSetor = idSetor WHERE nomeSetor = 'Investimentos';        
SELECT * FROM funcionario JOIN acompanhante
	ON fkFunc = idFunc;
SELECT * FROM funcionario JOIN acompanhante
	ON fkFunc = idFunc WHERE nomeFunc = 'Lucas';
SELECT * FROM funcionario JOIN acompanhante
	ON fkFunc = idFunc JOIN setor ON fkSetor = idSetor;
    
DROP TABLE setor, funcionario, acompanhante;


-- 	EXERCICIO 04


CREATE TABLE treinadorexp (
idTexp INT PRIMARY KEY AUTO_INCREMENT,
NTexp VARCHAR(45),
telefone VARCHAR(20),
email VARCHAR(100)
)AUTO_INCREMENT = 10;
     
CREATE TABLE treinador (
idTreinador INT PRIMARY KEY AUTO_INCREMENT,
NT VARCHAR(45),
telefone VARCHAR(20),
email VARCHAR(100),
fkTexp INT,
FOREIGN KEY(fkTexp) REFERENCES treinadorexp(idTexp)
) AUTO_INCREMENT = 10;

CREATE TABLE nadador (
idNadador INT PRIMARY KEY AUTO_INCREMENT,
NNadador VARCHAR(45),
estado VARCHAR(45),
dtNasc DATE,
fkTreinador INT,
FOREIGN KEY (fkTreinador)REFERENCES treinador(idTreinador)
) AUTO_INCREMENT = 100;
    
INSERT INTO treinadorexp VALUES
	(null, 'Zed','2341-5765','zed@gmail.com'),
    (null, 'KaiSa','4634-4733','kaisa@hotmail.com');
    
INSERT INTO treinador VALUES
	(null, 'Galio','9275-2457','galio@gmail.com', 10),
    (null, 'MasterYI','2348-8235','masteryi@hotmail.com', 10),
    (null, 'Yasuo','1245-1082','yasuo@gmail.com', 11),
    (null, 'LeeSin','9834-1274','leesin@outlook', 12);
    
INSERT INTO nadador VALUES
	(null, 'Nami', 'São Paulo', '2001-05-11', 10),
    (null, 'Kayn', 'Rio de Janeiro', '2003-01-10', 11),
    (null,'Vayne', 'Espirito Santo', '1999-10-01', 12),
    (null, 'Lucian', 'Bahia', '1988-09-14', 13),
    (null, 'Nasus', 'Florianopolis', '1999-12-01', 10),
    (null, 'Darius', 'Acre', '2001-11-10', 11),
    (null, 'Yone', 'São Paulo', '2005-02-15', 12),
    (null, 'Lux', 'Rio de Janeiro', '1995-10-02', 13);

SELECT * FROM treinadorexp;
SELECT * FROM treinador;
SELECT * FROM nadador;
SELECT * FROM treinador JOIN nadador
	ON fkTreinador = idTreinador;    
SELECT * FROM treinador JOIN nadador 
	ON fkTreinador = idTreinador WHERE nomeTreinador = 'Yasuo';
SELECT * FROM treinador JOIN treinadorexp
	ON fkTreinadorexp = idTreinadorexp;    
SELECT * FROM treinador JOIN treinadorexp
	ON fkTreinadorexp = idTreinadorexp WHERE nomeTreinadorexp = 'Zed';
SELECT * FROM nadador JOIN treinador
	ON fkTreinador = idTreinador JOIN treinadorexp ON fkTreinadorexp = idTreinadorexp;
SELECT * FROM treinador JOIN nadador
	ON fkTreinador = idTreinador JOIN treinadorexp ON fkTreinadorexp = idTreinadorexp WHERE nomeTreinador = 'Galio';
		
DROP TABLE treinadorexp, treinador, nadador;
DROP DATABASE lista6;