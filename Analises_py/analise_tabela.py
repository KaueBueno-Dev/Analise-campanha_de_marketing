import pandas as pd

df = pd.read_csv("marketing_campaign_performance_10000.csv")

df["Lucro"] = df["Revenue_USD"] - df["Cost_USD"]

df["CTR"] = (df["Clicks"] / df["Impressions"]) * 100

df["Conversion_Rate"] = (df["Conversions"] / df["Clicks"]) * 100

df["CPA"] = df["Cost_USD"] / df["Conversions"]

df.to_csv("Tabelas_tratadas/marketing_campaign_performance_tratado.csv", index=False)

print("\n===== LUCRO POR CANAL =====\n")
print(
    df.groupby("Channel")[["Revenue_USD", "Cost_USD", "Lucro"]]
      .sum()
      .sort_values("Lucro", ascending=False)
)


print("\n===== ROI MÉDIO POR CANAL =====\n")
print(
    df.groupby("Channel")["ROI"]
      .mean()
      .sort_values(ascending=False)
)


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