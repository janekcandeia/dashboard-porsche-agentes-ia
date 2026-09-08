# Dashboard da Porsche com Agentes de IA

Projeto desenvolvido para o desafio **“Criando uma Dashboard da Porsche com Agentes de IA”**, da plataforma DIO.

## Sobre o projeto

O objetivo foi transformar uma base de vendas da Porsche, inicialmente disponibilizada em Excel, em uma dashboard web interativa. Os dados sanitizados foram convertidos para JSON e consumidos pelo JavaScript da página.

A dashboard permite analisar os resultados e aplicar filtros que atualizam, em tempo real, os indicadores, os gráficos e a tabela detalhada.

## Funcionalidades

- Filtros por modelo, ano, estado, forma de pagamento e status da entrega;
- KPIs de receita total, quantidade de veículos, ticket médio e taxa de entrega;
- Evolução da receita por mês;
- Ranking dos modelos com maior receita;
- Distribuição dos status de entrega;
- Tabela detalhada das vendas filtradas;
- Botão para limpar todos os filtros;
- Layout responsivo para computadores e celulares.

## Tecnologias utilizadas

- Microsoft Excel para a base de dados;
- Agentes de Inteligência Artificial para apoio no tratamento e na organização dos dados;
- HTML5;
- CSS3;
- JavaScript;
- Canvas API para os gráficos, sem dependências externas.

## Estrutura do projeto

```text
dashboard-porsche-agentes-ia/
├── dist/
│   ├── assets/
│   │   ├── app.js
│   │   └── style.css
│   ├── data/
│   │   └── sales.json
│   └── index.html
├── scripts/
│   └── tratar_dados.py
├── Porsche_Base_Sanitizada.xlsx
├── PASSO_A_PASSO.md
├── requirements.txt
└── README.md
```

## Processo completo

O roteiro desde o tratamento da planilha até a dashboard está documentado em [`PASSO_A_PASSO.md`](PASSO_A_PASSO.md). O tratamento pode ser reproduzido executando o arquivo [`scripts/tratar_dados.py`](scripts/tratar_dados.py).

## Como executar

Como os dados são carregados por `fetch`, execute o projeto por meio de um servidor local. Uma opção simples é usar a extensão **Live Server** no Visual Studio Code e abrir o arquivo `dist/index.html`.

## Tratamento e uso dos dados

Foram priorizadas as colunas sanitizadas fornecidas na planilha, incluindo data, modelo, ano, preço, quilometragem, pagamento, cidade, estado e status. Datas marcadas como inválidas permanecem identificadas na tabela e não são consideradas no gráfico mensal.

## Aprendizados

O projeto demonstra como integrar dados tratados com apoio de IA a uma aplicação web, capturar eventos de filtros, filtrar um conjunto de dados em memória e atualizar indicadores e visualizações dinamicamente.

## Autora

**Jane Katy Santana dos Santos Candeia**

Projeto criado para fins educacionais no bootcamp da DIO.
