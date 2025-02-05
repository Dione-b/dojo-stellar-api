# Como Rodar a Aplicação com Docker Compose

Este guia explica como configurar e executar a aplicação utilizando **Docker Compose**.

## Pré-requisitos

Certifique-se de ter os seguintes requisitos instalados em sua máquina:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Passos para Rodar a Aplicação

1. Clone este repositório:

   ```sh
   git clone https://github.com/Dione-b/dojo-stellar-api
   cd dojo-stellar-api/setup-node
   ```

2. Execute o Docker Compose:

   ```sh
   docker-compose up -d
   ```

   Isso iniciará os containers em segundo plano.

3. Verifique se os containers estão rodando:

   ```sh
   docker ps
   ```

4. Para parar a aplicação, utilize:

   ```sh
   docker-compose down
   ```

## Configuração

Se necessário, edite o arquivo `docker-compose.yml` para ajustar configurações, como portas, variáveis de ambiente e volumes.

## Logs

Para visualizar os logs da aplicação, utilize:

```sh
   docker-compose logs -f
```

Agora sua aplicação está rodando com Docker Compose! 🚀
