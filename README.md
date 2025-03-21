# API de Doação de Livros

Esta é uma API Flask simples para cadastrar e listar livros para doação.

## Como usar

Para cadastrar um livro, envie uma requisição POST para `/doar` com os dados do livro no formato JSON.

Para listar os livros, acesse `/livros` no seu navegador ou use uma ferramenta como o curl.

## Exemplo de requisição POST para /doar

```json
{
    "titulo": "Dom Quixote",
    "categoria": "Romance",
    "autor": "Miguel de Cervantes",
    "imagem_url": "[https://example.com/dom_quixote.jpg](https://example.com/dom_quixote.jpg)"
}
