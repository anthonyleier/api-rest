CREATE DATABASE delivery;

\c delivery

-- Usuário
DROP TABLE IF EXISTS usuario CASCADE;

CREATE TABLE usuario (
    id INT GENERATED ALWAYS AS IDENTITY,
    nome VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    senha VARCHAR(100) NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO usuario (nome, email, senha) VALUES
('Eduarda Azevedo', 'eduarda.azevedo@gmail.com', 'eduarda123'),
('Bianca Araújo', 'bianca.araujo@gmail.com', 'bianca123'),
('Lucas Carvalho', 'lucas.carvalho@gmail.com', 'lucas123'),
('Rafaela Barros', 'rafaela.barros@gmail.com', 'rafaela123'),
('João Martins', 'joao.martins@gmail.com', 'joao123'),
('Gabriel Costa', 'gabriel.costa@gmail.com', 'gabriel123'),
('Isabelle Fernandes', 'isabelle.fernandes@gmail.com', 'isabelle123'),
('José Rocha', 'jose.rocha@gmail.com', 'jose123'),
('Vinicius Gomes', 'vinicius.gomes@gmail.com', 'vinicius123'),
('Victor Oliveira', 'victor.oliveira@gmail.com', 'victor123'),
('Mariana Melo', 'mariana.melo@hotmail.com', 'mariana123'),
('Lara Costa', 'lara.costa@hotmail.com', 'lara123'),
('Gustavo Dias', 'gustavo.dias@hotmail.com', 'gustavo123'),
('Gabrielly Fernandes', 'gabrielly.fernandes@hotmail.com', 'gabrielly123'),
('Matilde Oliveira', 'matilde.oliveira@hotmail.com', 'matilde123'),
('Lívia Carvalho', 'livia.carvalho@hotmail.com', 'livia123'),
('Tânia Castro', 'tania.castro@hotmail.com', 'tania123'),
('Victoria Alves', 'victoria.alves@hotmail.com', 'victoria123'),
('Bruno Gonçalves', 'bruno.goncalves@hotmail.com', 'bruno123'),
('Erick Gonçalves', 'erick.goncalves@hotmail.com', 'erick123');

-- Produto
DROP TABLE IF EXISTS produto CASCADE;

CREATE TABLE produto (
    id INT GENERATED ALWAYS AS IDENTITY,
    nome VARCHAR(50) NOT NULL,
    descricao TEXT,
    valor FLOAT NOT NULL,
    imagem VARCHAR(200),
    PRIMARY KEY (id)
);

INSERT INTO produto (nome, descricao, valor, imagem) VALUES
('X-Salada', 'Pão, maionese, alface, tomate, queijo e hambúrguer artesanal.', 11, 'https://static.deliverymuch.com.br/images/products/602ff217d5554.png'),
('X-Calabresa', 'Pão, maionese, alface, tomate, queijo, hambúrguer artesanal, ovo e calabresa.', 16, 'https://static.deliverymuch.com.br/images/products/60217fc2316e8.png'),
('X-Bacon', 'Pão, maionese, alface, tomate, queijo, hambúrguer artesanal, ovo e bacon.', 17, 'https://static.deliverymuch.com.br/images/products/602ff18425507.png'),
('X-Frango', 'Pão, maionese, alface, tomate, queijo, hambúrguer artesanal, ovo e frango.', 16, 'https://static.deliverymuch.com.br/images/products/6021877c98cee.png'),
('X-Coração', 'Pão, maionese, alface, tomate, queijo, hambúrguer artesanal, ovo e coração.', 18, 'https://static.deliverymuch.com.br/images/products/602180428eaf5.png');

-- Pedido
DROP TABLE IF EXISTS pedido CASCADE;

CREATE TABLE pedido (
    id INT GENERATED ALWAYS AS IDENTITY,
    usuario INT,
    PRIMARY KEY (id),
    FOREIGN KEY (usuario) REFERENCES usuario (id)
);

INSERT INTO pedido (usuario) VALUES
(1),(2),(3),(4),(5),(6),(7),(8),(9),(10),(11),(12),(13),(14),(15),(16),(17),(18),(19),(20);

DROP TABLE IF EXISTS pedido_produto CASCADE;

CREATE TABLE pedido_produto (
    id INT GENERATED ALWAYS AS IDENTITY,
    pedido INT,
    produto INT,
    quantidade INT,
    PRIMARY KEY (id),
    FOREIGN KEY (pedido) REFERENCES pedido (id),
    FOREIGN KEY (produto) REFERENCES produto (id)
);

INSERT INTO pedido_produto (pedido, produto, quantidade) VALUES
(1, 1, 1), (1, 2, 1),
(2, 2, 1), (2, 3, 1),
(3, 3, 1), (3, 4, 1),
(4, 4, 1), (4, 5, 1),
(5, 5, 1), (5, 1, 1),
(6, 1, 1), (6, 2, 1),
(7, 2, 1), (7, 3, 1),
(8, 3, 1), (8, 4, 1),
(9, 4, 1), (9, 5, 1),
(10, 5, 1), (10, 1, 1),
(11, 1, 1), (11, 2, 1),
(12, 2, 1), (12, 3, 1),
(13, 3, 1), (13, 4, 1),
(14, 4, 1), (14, 5, 1),
(15, 5, 1), (15, 1, 1),
(16, 1, 1), (16, 2, 1),
(17, 2, 1), (17, 3, 1),
(18, 3, 1), (18, 4, 1),
(19, 4, 1), (19, 5, 1),
(20, 5, 1), (20, 1, 1);