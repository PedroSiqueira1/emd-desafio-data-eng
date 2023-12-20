# Desafio de Data Engineer - EMD

Este é o desafio técnico que fiz para vaga de Pessoa Engenheira de Dados no Escritório de Dados do Rio de Janeiro.

## Configuração de ambiente
### Requisitos

- `Python 3.8.x`
- `pip`
- `Banco de dados PostgreSQL`
- `Ambiente virtual (recomendado)`


### Procedimentos

- Clonar esse repositório

```
git clone https://github.com/PedroSiqueira1/emd-desafio-data-eng
```

- Abrí-lo no seu editor de texto

- Instalar as dependências do projeto

```
pip install -r requirements.txt
```

- Criar um arquivo `.env` na raiz do projeto e adicionar as configurações necessárias da seguinte forma:

 ```
    HOST=seu_host
    USER=seu_usario
    PASSWORD=sua_senha
    DATABASE=seu_database
    PORT=sua_porta
    DIALECT=postgresql+psycopg2 (Não modifique esta variável)
```

- Pronto! Seu ambiente está configurado para desenvolvimento.

---


## Como rodar as aplicações

### Como rodar a pipeline usando o Prefect

- Navegue até o diretório da pipeline
```
cd emd-desafio-data-eng/pipelines/brt
```

- Execute o script `run.py`
```
python run.py
```

- Com isso, um schema `transporte_rodoviario_gps` e uma tabela `dados_brt` serão gerados em seu banco, inicialmente vazios.

- Quando o script acabar de rodar, a tabela estará populada com os dados da API!

- (Opcional) Se você possuir o Prefect Cloud configurado, é possível utilizá-lo para monitorar as runs do pipeline, para isso rode o comando `prefect agent local start` em um terminal dentro do diretório do projeto e acompanhe pelo site `cloud.prefect.io`


### Como gerar a tabela derivada usando o DBT

- Navegue até o diretório do DBT
```
cd emd-desafio-data-eng/tables/dados_brt
```

- Execute o comando `dbt run`

- Feito! A tabela derivada estará em seu banco no formato de uma view
ndado) Quando acabar de desenvolver sua pipeline, delete todas as versões da mesma pela UI do Prefect.

- (Opcional) Após a execução bem-sucedida, você pode gerar e visualizar a documentação usando os seguintes comandos:

```
dbt docs generate
dbt docs serve
```


