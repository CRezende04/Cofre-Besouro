CREATE TABLE Produtos (
	ProdutoID INT PRIMARY KEY AUTO_INCREMENT,
    NomeProduto VARCHAR(100),
    Quantidade INT,
    Preco DECIMAL(10, 2)
);

INSERT INTO Produtos (ProdutoID, NomeProduto, Quantidade, Preco) VALUES
(1, 'Notebook', 10, 3500.00),
(2, 'Smartphone', 25, 1500.50),
(3, 'Mouse', 50, 80.99);