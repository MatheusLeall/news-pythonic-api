## News API

#### Projeto simples usando a API do [newsapi.org](https://newsapi.org/)

#### Este projeto usa [docker](https://www.docker.com/) e [docker-compose](https://docs.docker.com/compose/) para executá-lo em sua máquina você percisará instalar. Se já possuí-los em sua máquina você precisará agora colocar os valores das váriáveis `DJANGO_SECRET_KEY` e `NEWS_API_KEY` no arquivo `.env` do projeto, lembre-se esses valores são secretos e não podem ser colocados de forma exposta no repositório por questões de segurança.

#### Talvez você precise dar permissão de execução para os arquivos que estão dentro da pasta script, para isso basta rodar o seguinte comando:

``` bash
chmod +x ./scripts/nome_do_arquivo.sh
```

#### Após ter realizado os passos acima basta executar o seguinte comando dentro da pasta onde se encontra o arquivo docker-compose.yaml:

``` bash
docker-compose up app
```

#### Se for a primeira executando o projeto ele será construído e executado, após o build ser concluído basta acessar o locahost:8000/api/v1/articles e será exibido uma lista de artigos com nome do autor, titulo e descrição do mesmo.

#### Caso queira rodar os testes do projeto basta usar também o docker-compose, lá tem um service para isso:

``` bash
docker-compose up integration-tests
```