# delivery-api

Este é um projeto de API REST desenvolvida em Flask, um framework Python que serve para criar aplicações web e APIs. Com esta API, é possível criar e gerenciar produtos, pedidos e usuários em um sistema de delivery. A API é baseada no padrão REST e implementa os verbos HTTP para manipulação de dados, tais como GET, POST, PUT e DELETE. Ela também é compatível com JSON, permitindo a troca de informações de forma fácil e eficiente. Além disso, o projeto conta com testes automatizados utilizando a biblioteca unittest e pode ser implementado via docker para garantir a facilidade de instalação e execução em diferentes ambientes. Este projeto foi desenvolvido com base nas melhores práticas de desenvolvimento e utiliza tecnologias modernas e de alta performance para garantir a melhor experiência possível aos usuários finais. Fique à vontade para utilizar, contribuir e melhorar este projeto!

# Exemplos
- ``` https://deliveryapi.anthonycruz.com.br/usuarios ```
- ``` https://deliveryapi.anthonycruz.com.br/produtos ```
- ``` https://deliveryapi.anthonycruz.com.br/pedidos ```

# Instalação Docker

Para iniciar o projeto através do Docker, é necessário certificar de que o Docker e o Docker Compose estejam instalados em seu sistema. Após isso, é necessário executar o comando "docker-compose up" com privilégios de administrador na pasta do repositório para iniciar os containers do projeto.

``` docker-compose up ```

O comando "docker-compose up" é usado para iniciar e executar todos os contêineres definidos em um arquivo de composição do Docker Compose. O comando cria e inicia todos os serviços especificados no arquivo docker-compose.yml no diretório atual. Ele também conecta todos os contêineres a redes definidas no arquivo de composição, permitindo que eles se comuniquem entre si. Além disso, o comando exibe logs combinados de todos os contêineres. É uma forma simples de criar e gerenciar um ambiente multi-contêiner para aplicativos que precisam de vários serviços.

# Instalação Manual

O comando "pip install" é utilizado para instalar pacotes Python em um ambiente virtual ou sistema operacional. Nesse exemplo, estamos instalando três pacotes Python especificos: psycopg2, flask e flask_restful.

``` pip install psycopg2==2.9.3 flask==2.1.2 flask_restful==0.3.9 ```

O pacote psycopg2 é uma biblioteca para conexão com bancos de dados PostgreSQL, permitindo que o Python se comunique com o banco de dados, execute queries e manipule dados. Os pacotes flask e flask_restful são ambos frameworks Python para construir APIs web. O Flask é um framework leve e flexível, enquanto o Flask-RESTful é uma extensão do Flask que adiciona funcionalidades para construção de APIs RESTful.

``` python main.py ```

Por fim, o comando "python main.py" pode ser executado para iniciar os serviços da API. Assim que carregar os pacotes correspondentes, o serviço já poderá ser utilizado acessando, por padrão, no endereço http://localhost:5000.
