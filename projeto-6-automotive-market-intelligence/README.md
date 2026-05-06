# Automotive Market Intelligence Platform

## Visão Geral

Plataforma de inteligência de mercado automotivo baseada em tendências de busca no mercado brasileiro.

O projeto simula uma arquitetura moderna de dados para análise de comportamento do consumidor automotivo, utilizando dados históricos de interesse digital para geração de insights estratégicos.

---

## Objetivo

Monitorar o interesse de mercado por:

- SUVs
- Sedans
- Hatchs
- Elétricos
- Caminhões

Permitindo análises como:

- Share de interesse
- Crescimento de marcas
- Tendências de mercado
- Comparação entre segmentos

---

## Arquitetura

```mermaid
flowchart LR

    A[SerpAPI Google Trends] --> B[Python Ingestion]

    B --> C[RAW_MARKET_TRENDS]

    C --> D[Tratamento / Normalização]
    D --> E[TRUSTED_MARKET_TRENDS]

    E --> F[Market Share]
    E --> G[Growth Analysis]
    E --> H[Brand Ranking]
    E --> I[Category Analysis]

    F --> J[REFINED_MARKET_INTELLIGENCE]

    J --> K[Dashboard]
