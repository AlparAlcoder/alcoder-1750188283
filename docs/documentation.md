# Documentação da API FastAPI

Essa API foi desenvolvida utilizando o framework Python FastAPI. Ela consiste em duas rotas principais que permitem a criação e leitura de itens.

## Dependências

- FastAPI
- Pydantic

Instalar com pip:
```
pip install fastapi pydantic
```

## Modelos

- Item: Este modelo representa um item com as seguintes propriedades:
  - name (str): Nome do item.
  - description (str, optional): Descrição do item. Default: None.
  - price (float): Preço do item.
  - quantity (int): Quantidade do item em estoque.

## Endpoints

### POST `/items/`

Cria um novo item.

#### Parâmetros

- item (Item): O item a ser criado.

#### Exemplo de uso

```
curl -X POST "http://localhost:8000/items/" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"name\":\"foo\",\"description\":\"A very nice item\",\"price\":10.5,\"quantity\":100}"
```

### GET `/items/{item_name}`

Obtém um item específico pelo nome.

#### Parâmetros

- item_name (str): O nome do item a ser obtido.

#### Exemplo de uso

```
curl -X GET "http://localhost:8000/items/foo" -H  "accept: application/json"
```

## Notas importantes

- A rota POST `/items/` irá retornar um erro 400 se um item com o mesmo nome já existir.
- A rota GET `/items/{item_name}` irá retornar um erro 404 se o item não for encontrado.