![Banner Pipoca.AI](banner_pipoca_ai.png)

# Pipoca.AI — Plataforma Integrada de Streaming, Live PPV & Digital Store

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analytics-150458?style=flat-square&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Architecture](https://img.shields.io/badge/Architecture-Modular%20(18%20Modules)-2EA44F?style=flat-square)]()
[![License](https://img.shields.io/badge/License-Educacional%20%2F%20SENAC%20RJ-004A8D?style=flat-square)]()

**Pipoca.AI** é uma aplicação modular em Python projetada para simular o ecossistema de autoatendimento, faturamento e telemetria de dados de uma plataforma digital de entretenimento. O sistema unifica assinaturas recorrentes (SaaS), transmissões ao vivo (*Pay-Per-View* com controle de capacidade de servidor), loja de ativos digitais e um pipeline analítico automatizado com exportação estruturada em CSV.

---

## Visão Geral e Capacidades

O software opera sobre uma arquitetura desacoplada em 18 módulos independentes orquestrados por um núcleo central (`main.py`), garantindo resiliência na execução e facilidade de manutenção:

* **Gestão de Assinaturas (SaaS):** Catálogo de planos de streaming com cálculo dinâmico de fidelidade (desconto progressivo para contratos anuais) e controle de telas simultâneas.
* **Live Events & Infraestrutura Cloud:** Reserva de acessos *Pay-Per-View* com validação em tempo real de *slots* disponíveis em servidor e rotina administrativa para liberação de conexões encerradas.
* **Loja de Ativos Digitais & Supply Chain:** Comercialização de moedas virtuais, passes de temporada e aluguéis 8K, acompanhada de auditoria preventiva de estoque mínimo de chaves de licença.
* **Checkout, Benefícios e Anti-Churn:** Motor de descontos cumulativos (fidelidade anual + cupons de criadores de conteúdo), processamento de pagamentos (`PIX`, `CARTAO_VIRTUAL`, `CRIPTO_REAL`) e fluxo de reembolso com conciliação automática de receita.
* **Data Analytics & Telemetria:** Consolidação do histórico transacional em `DataFrame` via **Pandas**, exibição tabular em console e exportação de base estruturada (`.csv`) para consumo em ferramentas de BI.

---

## Arquitetura do Projeto

```text
PipocaAI-Platform/
├── banner_pipoca_ai.png                 # Identidade visual do repositório
├── README.md                            # Documentação oficial do software
├── DISTRIBUICAO_MODULOS.md              # Matriz de responsabilidade e engenharia
├── main.py                              # Orquestrador principal com fallback resiliente
└── modulos/                             # Pacote de regras de negócio desacopladas
    ├── __init__.py
    ├── f01_login_usuario.py             # Autenticação e validação de credenciais
    ├── f02_menu_chatbot.py              # Interface CLI e tratamento de entradas
    ├── f03_abrir_pedido.py              # Inicialização de sessão transacional
    ├── f04_validar_influencer.py        # Validação de cupons promocionais
    ├── f05_catalogo_planos.py           # Exibição de planos de streaming
    ├── f06_assinar_plano.py             # Contratação e cálculo de fidelidade SaaS
    ├── f07_catalogo_lives.py            # Exibição de eventos Pay-Per-View
    ├── f08_comprar_ppv.py               # Reserva de slots em servidor cloud
    ├── f09_liberar_servidor.py          # Desalocação de conexões de servidor
    ├── f10_catalogo_loja.py             # Exibição de ativos e licenças digitais
    ├── f11_comprar_item_digital.py      # Baixa de estoque e venda de ativos
    ├── f12_auditoria_licencas.py        # Monitoramento de estoque crítico
    ├── f13_resumo_carrinho.py           # Extrato detalhado da transação
    ├── f14_remover_item.py              # Remoção de itens e recálculo de saldo
    ├── f15_calculo_cashback_desconto.py # Motor de descontos cumulativos
    ├── f16_gateway_pagamento.py         # Processamento de checkout e receita
    ├── f17_reembolso_churn.py           # Estorno financeiro e gestão de churn
    └── f18_analytics_pandas.py          # Pipeline analítico Pandas e exportação CSV