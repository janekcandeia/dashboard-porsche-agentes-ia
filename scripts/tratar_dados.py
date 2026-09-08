"""Converte a planilha sanitizada da Porsche em JSON para a dashboard.

Uso:
    pip install pandas openpyxl
    python scripts/tratar_dados.py
"""

from pathlib import Path
import json
import pandas as pd


RAIZ = Path(__file__).resolve().parents[1]
ARQUIVO_EXCEL = RAIZ / "Porsche_Base_Sanitizada.xlsx"
ARQUIVO_JSON = RAIZ / "dist" / "data" / "sales.json"


def texto_ou_nulo(valor):
    """Retorna texto limpo ou None quando a célula estiver vazia."""
    if pd.isna(valor):
        return None
    texto = str(valor).strip()
    return texto or None


def numero_ou_nulo(valor, inteiro=False):
    """Converte valores numéricos e evita NaN no arquivo JSON."""
    numero = pd.to_numeric(valor, errors="coerce")
    if pd.isna(numero):
        return None
    return int(numero) if inteiro else float(numero)


def tratar_data(valor):
    """Mantém datas ISO válidas e transforma INVALID em valor nulo."""
    if pd.isna(valor) or str(valor).strip().upper() == "INVALID":
        return None
    data = pd.to_datetime(valor, errors="coerce")
    return None if pd.isna(data) else data.strftime("%Y-%m-%d")


def tratar_planilha():
    dados = pd.read_excel(ARQUIVO_EXCEL, sheet_name="Sanitized")

    # A base já contém colunas originais e colunas sanitizadas pela IA.
    # Para a dashboard, priorizamos as versões Sanitized.
    vendas = []
    for _, linha in dados.iterrows():
        vendas.append(
            {
                "id": numero_ou_nulo(linha["sale_id"], inteiro=True),
                "date": tratar_data(linha["SaleDateSanitized"]),
                "customer": texto_ou_nulo(linha["customer_name"]),
                "model": texto_ou_nulo(linha["PorscheModelSanitized"]),
                "year": numero_ou_nulo(linha["ModelYearSanitized"], inteiro=True),
                "price": numero_ou_nulo(linha["SalesPriceSanitized"]),
                "mileage": numero_ou_nulo(
                    linha["VehicleMileageSanitized"], inteiro=True
                ),
                "payment": texto_ou_nulo(linha["PayMethodSanitized"]),
                "city": texto_ou_nulo(linha["CitySanitized"]),
                "state": texto_ou_nulo(linha["StateSanitized"]),
                "salesperson": texto_ou_nulo(linha["salesperson"]),
                "status": texto_ou_nulo(linha["DeliveryStatusSanitized"]),
            }
        )

    ARQUIVO_JSON.parent.mkdir(parents=True, exist_ok=True)
    with ARQUIVO_JSON.open("w", encoding="utf-8") as arquivo:
        json.dump(vendas, arquivo, ensure_ascii=False, indent=2)

    print(f"Tratamento concluído: {len(vendas)} registros.")
    print(f"JSON gerado em: {ARQUIVO_JSON}")


if __name__ == "__main__":
    tratar_planilha()
