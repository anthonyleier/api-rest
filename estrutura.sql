-- Estrutura do banco de dados (PostgreSQL)
-- Usuário
DROP TABLE IF EXISTS usuario CASCADE;

CREATE TABLE usuario (
    id INT GENERATED ALWAYS AS IDENTITY,
    nome VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    senha VARCHAR(100) NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO
    usuario (nome, email, senha)
VALUES
    (
        'Anthony Cruz',
        'anthonyleierlw@gmail.com',
        'developer'
    );

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

INSERT INTO
    produto (nome, descricao, valor, imagem)
VALUES
    (
        'Big Mac',
        'Não existe nada igual! Dois hambúrgueres, alface, queijo e molho especial, cebola e picles num pão com gergelim. O sabor de McDonalds duplamente delicioso. Com dois hambúrgueres de carne 100% bovina, queijo cheddar derretido, cebola, picles e o incrível molho Big Mac.',
        24.90,
        'https://cache-backend-mcd.mcdonaldscupones.com/media/image/product$kzXCTbnv/200/200/original?country=br'
    );

-- Pedido
DROP TABLE IF EXISTS pedido CASCADE;

CREATE TABLE pedido (
    id INT GENERATED ALWAYS AS IDENTITY,
    usuario INT,
    PRIMARY KEY (id),
    FOREIGN KEY (usuario) REFERENCES usuario (id)
);

INSERT INTO
    pedido (usuario)
VALUES
    (1) RETURNING id;

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

INSERT INTO
    pedido_produto (pedido, produto, quantidade)
VALUES
    (1, 1, 5),
    (1, 1, 10),
    (1, 1, 15),
    (1, 1, 20);