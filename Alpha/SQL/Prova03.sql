CREATE TABLE Estoque (
    EstoqueID INT PRIMARY KEY AUTO_INCREMENT,
    ProdutoID INT,
    FornecedorID INT,
    Quantidade INT,
    DataEntrada DATE,
    CONSTRAINT fk_produto FOREIGN KEY (ProdutoID) REFERENCES Produtos(ProdutoID),
    CONSTRAINT fk_fornecedor FOREIGN KEY (FornecedorID) REFERENCES Fornecedores(FornecedorID)
);

SELECT 
    Produtos.ProdutoID, Produtos.NomeProduto, 
    Estoque.EstoqueID, Estoque.Quantidade, Estoque.DataEntrada
FROM 
    Produtos
FULL OUTER JOIN 
    Estoque ON Produtos.ProdutoID = Estoque.ProdutoID;
    
SELECT 
    ProdutoID, 
    SUM(Quantidade) AS TotalEstoque
FROM 
    Estoque
GROUP BY 
    ProdutoID;
    
ALTER TABLE Produtos ADD COLUMN Categoria VARCHAR(50);
ALTER TABLE Produtos MODIFY COLUMN Preco DECIMAL(12, 2); 