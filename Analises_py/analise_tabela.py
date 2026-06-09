import pandas as pd

# Carrega o conjunto de dados das campanhas de marketing
df = pd.read_csv("marketing_campaign_performance_10000.csv")

# Métricas de negócio

# Calcula o lucro obtido por cada campanha
df["Lucro"] = df["Revenue_USD"] - df["Cost_USD"]

# Calcula a taxa de cliques (CTR) de cada campanha
df["CTR"] = (df["Clicks"] / df["Impressions"]) * 100

# Calcula a taxa de conversão de cada campanha
df["Conversion_Rate"] = (df["Conversions"] / df["Clicks"]) * 100

# Calcula o custo por aquisição (CPA) de cada campanha
df["CPA"] = df["Cost_USD"] / df["Conversions"]

# Salva as novas colunas em um novo arquivo CSV
df.to_csv("Tabelas_tratadas/marketing_campaign_performance_tratado.csv", index=False)

# ANÁLISES DE NEGÓCIO

# Calcula qual canal gerou mais lucro para a empresa
print("\n===== LUCRO POR CANAL =====\n")
print(
    df.groupby("Channel")[["Revenue_USD", "Cost_USD", "Lucro"]]
      .sum()
      .sort_values("Lucro", ascending=False)
)

# Calcula qual canal possui o melhor retorno médio sobre o investimento (ROI)
print("\n===== ROI MÉDIO POR CANAL =====\n")
print(
    df.groupby("Channel")["ROI"]
      .mean()
      .sort_values(ascending=False)
)

# Calcula qual canal possui a maior taxa média de conversão
print("\n===== TAXA DE CONVERSÃO POR CANAL =====\n")
print(
    df.groupby("Channel")["Conversion_Rate"]
      .mean()
      .sort_values(ascending=False)
)

# Calcula qual canal adquire clientes pelo menor custo (CPA)
print("\n===== CPA MÉDIO POR CANAL =====\n")
print(
    df.groupby("Channel")["CPA"]
      .mean()
      .sort_values()
)

# Calcula qual canal gera mais conversões
print("\n===== CONVERSÕES POR CANAL =====\n")
print(
    df.groupby("Channel")["Conversions"]
      .sum()
      .sort_values(ascending=False)
)

# Calcula qual canal gera mais receita
print("\n===== RECEITA POR CANAL =====\n")
print(
    df.groupby("Channel")["Revenue_USD"]
      .sum()
      .sort_values(ascending=False)
)

# Calcula quantas campanhas operaram com prejuízo
print("\n===== QUANTIDADE DE CAMPANHAS COM PREJUÍZO =====\n")
print((df["Lucro"] < 0).sum())

# Calcula o valor total perdido em campanhas deficitárias
print("\n===== PREJUÍZO TOTAL DAS CAMPANHAS DEFICITÁRIAS =====\n")
print(df[df["Lucro"] < 0]["Lucro"].sum())

# Identifica as 10 campanhas com maior prejuízo
print("\n===== TOP 10 CAMPANHAS COM MAIOR PREJUÍZO =====\n")
print(
    df.sort_values("Lucro")
      [["CampaignID", "Channel", "Cost_USD", "Revenue_USD", "Lucro"]]
      .head(10)
)

# Identifica as 10 campanhas mais lucrativas
print("\n===== TOP 10 CAMPANHAS MAIS LUCRATIVAS =====\n")
print(
    df.sort_values("Lucro", ascending=False)
      [["CampaignID", "Channel", "Cost_USD", "Revenue_USD", "Lucro"]]
      .head(10)
)