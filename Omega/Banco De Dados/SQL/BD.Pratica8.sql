CREATE DATABASE Vendas;
USE Vendas;

CREATE TABLE Cliente (
idCliente INT PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(45),
email VARCHAR(45),
endereco VARCHAR(45),
fkIndicador INT,
CONSTRAINT fkIndicado FOREIGN KEY (fkIndicador) REFERENCES Cliente(idCliente)
);

INSERT INTO Cliente VALUES 
	(NULL,'Vivian','vivian@sptech.school','Rua Haddock Lobo',NULL),
	(NULL,'Caue','caue.rezende@sptech.school','Rua Haddock Lobo',1),
	(NULL,'Carlos','carlos.goes@sptech.school','Rua Haddock Lobo',NULL);

CREATE TABLE Venda (
idVendas INT PRIMARY KEY AUTO_INCREMENT,
VendaTotal VARCHAR(45),
dtVenda DATE,
fkCliente INT,
CONSTRAINT fkCliente FOREIGN KEY (fkCliente) REFERENCES Cliente(idCliente)
)AUTO_INCREMENT = 100;

INSERT INTO Venda VALUES
	(NULL,1000,'2023-01-01',1),
	(NULL,100,'2023-01-01',2),
	(NULL,2000,'2023-01-01',3);

CREATE TABLE Produto (
idProduto INT PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(45),
descricao VARCHAR(45),
preco VARCHAR(45)
)AUTO_INCREMENT = 1000;

INSERT INTO Produto VALUES
	(NULL,'Cafe','Bebida',50),
	(NULL,'Bis','Doce',75),
	(NULL,'Lanche','Salgado',100);

CREATE TABLE Sacola (
idSacola INT,
quantidade VARCHAR(45),
desconto VARCHAR(45),
fkVendas INT,
fkProduto INT,
CONSTRAINT fkVenda FOREIGN KEY (fkVendas) REFERENCES Venda(idVendas),
CONSTRAINT fkProduto FOREIGN KEY (fkProduto) REFERENCES Produto(idProduto),
CONSTRAINT pkSacolaComposta PRIMARY KEY (idSacola,fkVendas,fkProduto)
);

INSERT INTO Sacola VALUES
	(1,3,0,100,1000),
	(2,2,0,101,1001),
	(3,2,0,101,1001),
	(4,1,0,102,1002);
    
    
SELECT * FROM Cliente;
SELECT * FROM Venda;
SELECT * FROM Produto;
SELECT * FROM Sacola;

SELECT * FROM Cliente JOIN Venda
	ON idCliente = fkCliente;
    
SELECT * FROM Cliente JOIN Venda
	ON idCliente = fkCliente
    WHERE nome = 'Vivian';
    
SELECT * FROM Cliente JOIN Cliente as fkIndicador 
    ON Cliente.fkIndicador = fkIndicador.idCliente;

SELECT * FROM Cliente JOIN Cliente AS fkIndicador 
	ON Cliente.fkIndicador = fkIndicador.idCliente
    WHERE fkIndicador.nome = "Vivian";
    
SELECT * FROM Cliente JOIN Cliente AS fkIndicador 
	ON Cliente.fkIndicador = fkIndicador.idCliente JOIN Venda 
    ON fkIndicador.idCliente = Venda.fkCliente JOIN Sacola 
    ON Venda.idVendas = Sacola.fkVendas JOIN Produto 
    ON Sacola.fkProduto = Produto.idProduto;
    
SELECT  Venda.dtVenda, 
		Produto.nome, 
        Sacola.quantidade FROM Venda JOIN Sacola 
		ON Venda.idVendas = Sacola.fkVendas JOIN Produto 
		ON Sacola.fkProduto = Produto.idProduto;
            
SELECT  Produto.nome,
		Produto.preco, SUM(Sacola.quantidade) AS quantidade_VendaTotal FROM Produto JOIN Sacola
		ON Produto.idProduto = Sacola.fkProduto
        GROUP BY Produto.nome;
        
INSERT INTO Cliente VALUES 
	(null, 'Kat', 'kat@sptech.school', 'Itaim Paulista', 3);
    
SELECT * FROM Cliente LEFT JOIN Venda
	ON idCliente = fkCliente;
    
SELECT  MAX(preco) AS PreçoMaximo, MIN(preco) AS PreçoMinimo FROM Produto;

SELECT SUM(preco) AS Produto_Soma, AVG(preco) AS Produto_Media FROM Produto;

SELECT preco FROM Produto
	WHERE preco > 75;
    
SELECT SUM(DISTINCT preco) FROM Produto;

SELECT *, SUM(Produto.preco) FROM Produto
	JOIN Sacola ON Sacola.fkProduto = Produto.idProduto
    JOIN Venda ON Venda.idVendas = Sacola.fkVendas;
    
	
