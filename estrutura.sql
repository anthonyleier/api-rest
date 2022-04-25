CREATE DATABASE delivery;

CREATE TABLE IF NOT EXISTS usuario (
    id serial,
    nome varchar(50) NOT NULL,
    email varchar(100) NOT NULL UNIQUE,
    senha varchar(100) NOT NULL
);

INSERT INTO usuario (nome, email, senha) VALUES ('Anthony Cruz', 'anthonyleierlw@gmail.com', 'developer');