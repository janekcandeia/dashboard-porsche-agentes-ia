# Passo a passo: da planilha à dashboard

Este documento registra o processo realizado no projeto **Dashboard da Porsche com Agentes de IA**.

## 1. Análise da planilha

A planilha `Porsche_Base_Sanitizada.xlsx` contém 100 registros de vendas. A aba `Sanitized` possui tanto os dados originais quanto as versões tratadas.

Foram utilizadas principalmente as colunas:

| Informação | Coluna utilizada |
| --- | --- |
| Data da venda | `SaleDateSanitized` |
| Modelo | `PorscheModelSanitized` |
| Ano do modelo | `ModelYearSanitized` |
| Preço | `SalesPriceSanitized` |
| Quilometragem | `VehicleMileageSanitized` |
| Pagamento | `PayMethodSanitized` |
| Cidade | `CitySanitized` |
| Estado | `StateSanitized` |
| Status | `DeliveryStatusSanitized` |

## 2. Tratamento dos dados

O arquivo `scripts/tratar_dados.py` realiza as seguintes etapas:

1. Abre a aba `Sanitized` com a biblioteca `pandas`;
2. Seleciona as colunas necessárias para a dashboard;
3. Converte ano e quilometragem para números inteiros;
4. Converte o preço para número decimal;
5. Padroniza as datas no formato `AAAA-MM-DD`;
6. Converte datas inválidas e células vazias em `null`;
7. Gera o arquivo `dist/data/sales.json`.

Para executar o tratamento:

```bash
pip install -r requirements.txt
python scripts/tratar_dados.py
```

## 3. Estrutura da dashboard

O arquivo `dist/index.html` organiza a página em quatro áreas:

- filtros;
- indicadores principais;
- gráficos;
- tabela detalhada.

O arquivo `dist/assets/style.css` define a identidade visual, o layout responsivo e as cores inspiradas na Porsche.

## 4. Carregamento dos dados

No arquivo `dist/assets/app.js`, a função `init()` carrega o JSON:

```javascript
const res = await fetch('data/sales.json');
allSales = await res.json();
```

Os dados ficam armazenados no array `allSales`.

## 5. Preenchimento dos filtros

Os valores disponíveis são obtidos diretamente do conjunto de dados. Assim, os filtros de modelo, ano, estado, pagamento e status não precisam ser preenchidos manualmente.

```javascript
function unique(field) {
  return [...new Set(allSales.map(item => item[field]).filter(Boolean))];
}
```

## 6. Captura dos eventos

Cada campo acompanha o evento `change`. Quando a pessoa seleciona uma opção, a função `update()` é executada:

```javascript
filterIds.forEach(id => {
  document.getElementById(id).addEventListener('change', update);
});
```

## 7. Filtragem em memória

A função `filtered()` compara cada registro com os valores escolhidos. Um filtro vazio representa a opção “Todos”.

```javascript
return allSales.filter(row =>
  filterIds.every(id =>
    !document.getElementById(id).value ||
    String(row[campoDoFiltro]) === document.getElementById(id).value
  )
);
```

## 8. Atualização dos KPIs

A função `update()` recalcula:

- receita total: soma dos preços;
- veículos vendidos: quantidade de registros;
- ticket médio: receita dividida pela quantidade de vendas;
- taxa de entrega: pedidos entregues divididos pelo total filtrado.

## 9. Atualização dos gráficos

Após filtrar os dados, o JavaScript redesenha três gráficos utilizando a Canvas API:

- receita por mês;
- seis modelos com maior receita;
- quantidade de pedidos por status.

Os gráficos não dependem de bibliotecas externas.

## 10. Atualização da tabela

A função `renderTable()` limpa as linhas anteriores, ordena as vendas por data e inclui somente os registros que atendem aos filtros.

## 11. Execução local

O carregamento por `fetch` exige um servidor local. No Visual Studio Code, pode-se instalar a extensão **Live Server** e abrir `dist/index.html` com a opção **Open with Live Server**.

Outra opção é executar:

```bash
python -m http.server 8000 --directory dist
```

Depois, acessar `http://localhost:8000` no navegador.

## 12. Publicação no GitHub

1. Criar um repositório público chamado `dashboard-porsche-agentes-ia`;
2. Enviar todos os arquivos deste projeto;
3. Conferir se o `README.md` aparece na página inicial;
4. Copiar o endereço do repositório;
5. Entregar esse endereço no desafio da DIO.
