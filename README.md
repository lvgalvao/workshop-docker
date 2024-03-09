# Workshop Docker

Primeiro vamos fazer um "hello world" 

1) Fazer o projeto app.py

2) Escrever o readme ensinando como instalar

3) Criar um arquivo Dockerfile

```Dockerfile
FROM python:3.12
RUN pip install poetry
COPY . /src
WORKDIR /src
RUN poetry install
EXPOSE 8501
ENTRYPOINT ["poetry","run", "streamlit", "run", "app/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

6) Rodar local

```bash
docker build minha-primeira-imagem
```

```bash
docker run -d -p 8501:8501 --name meu-primeiro-container dashboard_hello_world
```

1) Para gerar os valores mockados utilizar o comando

```bash
poetry run python data/sales_data_generator.py
```

2) Para subir um postgres

```bash
docker pull postgres
docker run --name my_postgres -e POSTGRES_USER=myuser -e POSTGRES_PASSWORD=mypassword -e POSTGRES_DB=mydatabase -p 5432:5432 -d postgres
```

Neste comando:

* `--name my_postgres`: Define o nome do container como `my_postgres`.
* `-e POSTGRES_USER=myuser`: Define o usuário do banco de dados como `myuser`.
* `-e POSTGRES_PASSWORD=mypassword`: **Importante!** Aqui você define a senha para o superusuário, substitua `mypassword` pela senha desejada.
* `-e POSTGRES_DB=mydatabase`: Cria um banco de dados inicial chamado `mydatabase`.
* `-p 5432:5432`: Mapeia a porta 5432 do container para a porta 5432 do host, permitindo acessar o banco de dados a partir do host.
* `-d postgres`: Especifica que o container será baseado na imagem `postgres` mais recente e rodará em modo detached.

3) E como acessar esse Postgres?

```bash
docker pull dpage/pgadmin4
docker run --name my_pgadmin -p 80:80 -e 'PGADMIN_DEFAULT_EMAIL=user@example.com' -e 'PGADMIN_DEFAULT_PASSWORD=SuperSecret' -d dpage/pgadmin4
```

### Acessando o pgAdmin 4

Após iniciar o container, você pode acessar o pgAdmin 4 abrindo um navegador web e visitando `http://localhost`. Você será solicitado a entrar usando o e-mail e a senha que você especificou nas variáveis de ambiente `PGADMIN_DEFAULT_EMAIL` e `PGADMIN_DEFAULT_PASSWORD`.

### Conectando ao PostgreSQL a partir do pgAdmin 4

Para conectar ao seu servidor PostgreSQL a partir do pgAdmin 4:

1. Clique com o botão direito em "Servers" na barra lateral esquerda e selecione "Create" > "Server".
2. Na aba "General", forneça um nome para a conexão.
3. Na aba "Connection", insira:
    * "Host name/address": Se o PostgreSQL estiver rodando como um container Docker no mesmo host, use `host.docker.internal` (para Docker no Windows ou Mac) ou o endereço IP do container PostgreSQL (você pode obtê-lo com `docker inspect my_postgres | grep IPAddress` no Linux).
    * "Port": `5432` (a menos que você tenha configurado de outra forma).
    * "Maintenance database": o nome do banco de dados que você criou, por exemplo, `mydatabase`.
    * "Username": o nome do usuário, por exemplo, `myuser`.
    * "Password": a senha do usuário PostgreSQL.

    
[Excalidraw](https://link.excalidraw.com/l/8pvW6zbNUnD/6MNAkqnvTPt)

Tabelas geradas



