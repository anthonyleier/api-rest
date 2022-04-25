CREATE DATABASE delivery;

CREATE TABLE IF NOT EXISTS usuario (
    id SERIAL,
    nome VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    senha VARCHAR(100) NOT NULL
);

INSERT INTO
    usuario (nome, email, senha)
VALUES
    (
        'Anthony Cruz',
        'anthonyleierlw@gmail.com',
        'developer'
    );

CREATE TABLE IF NOT EXISTS produto (
    id SERIAL,
    nome VARCHAR(50) NOT NULL,
    descricao TEXT,
    valor FLOAT NOT NULL,
    imagem VARCHAR(200)
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