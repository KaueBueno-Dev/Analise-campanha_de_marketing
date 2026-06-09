-- Qual canal gerou mais lucro para a empresa?
SELECT
    channel,
    ROUND(SUM(revenue_usd), 2) AS receita_total,
    ROUND(SUM(cost_usd), 2) AS custo_total,
    ROUND(SUM(lucro), 2) AS lucro_total
FROM marketing_campaigns
GROUP BY channel
ORDER BY lucro_total DESC;


-- Qual canal possui o melhor ROI médio?
SELECT
    channel,
    ROUND(AVG(roi), 4) AS roi_medio
FROM marketing_campaigns
GROUP BY channel
ORDER BY roi_medio DESC;


-- Qual canal possui a maior taxa média de conversão?
SELECT
    channel,
    ROUND(AVG(conversion_rate), 2) AS taxa_conversao_media
FROM marketing_campaigns
GROUP BY channel
ORDER BY taxa_conversao_media DESC;


-- Qual canal possui o menor custo médio por aquisição de clientes (CPA)?
SELECT
    channel,
    ROUND(AVG(cpa), 2) AS cpa_medio
FROM marketing_campaigns
GROUP BY channel
ORDER BY cpa_medio ASC;


-- Qual canal gerou o maior número de conversões?
SELECT
    channel,
    SUM(conversions) AS total_conversoes
FROM marketing_campaigns
GROUP BY channel
ORDER BY total_conversoes DESC;


-- Qual canal gerou a maior receita total?
SELECT
    channel,
    ROUND(SUM(revenue_usd), 2) AS receita_total
FROM marketing_campaigns
GROUP BY channel
ORDER BY receita_total DESC;


-- Quais são as 10 campanhas com menor retorno financeiro?
SELECT
    campaignid,
    channel,
    cost_usd,
    revenue_usd,
    lucro
FROM marketing_campaigns
ORDER BY lucro ASC
LIMIT 10;


-- Quais são as 10 campanhas mais lucrativas?
SELECT
    campaignid,
    channel,
    cost_usd,
    revenue_usd,
    lucro
FROM marketing_campaigns
ORDER BY lucro DESC
LIMIT 10;


-- Qual foi o lucro total obtido pela empresa em todas as campanhas?
SELECT
    ROUND(SUM(lucro), 2) AS lucro_total_empresa
FROM marketing_campaigns;


-- Qual canal apresenta a maior taxa média de cliques (CTR)?
SELECT
    channel,
    ROUND(AVG(ctr), 2) AS ctr_medio
FROM marketing_campaigns
GROUP BY channel
ORDER BY ctr_medio DESC;