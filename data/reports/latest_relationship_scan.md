# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T21:07:25.417644+00:00`
- Price records: `672`
- Market context records: `3112`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6925`

## Conditions

- `news_risk_high`: News Risk is elevated.
- `macro_risk_high`: Macro Risk is elevated.
- `risk_on_high`: Risk-On score is elevated.
- `market_context_high`: Market Context is supportive.
- `polymarket_volume_spike`: Polymarket 24h volume z-score is elevated.
- `flow_alert_high`: Flow Alert score is elevated.
- `news_and_polymarket`: News Risk and Polymarket volume spike happen together.
- `risk_on_and_context`: Risk-On and Market Context are both supportive.
- `macro_and_flow`: Macro Risk and Flow Alert are elevated together.

## Top Patterns

- `market_context_high->crypto_alt_24h` score `14.7499` n `91` status `ready` deltaP `12.4809` edge `2.4605` maxDD `-43.5484`
- `market_context_high->commodity_24h` score `14.7334` n `91` status `ready` deltaP `46.1863` edge `0.9627` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `13.4378` n `91` status `ready` deltaP `22.2928` edge `1.02` maxDD `-1.9039`
- `market_context_high->index_24h` score `10.3989` n `91` status `ready` deltaP `32.4787` edge `0.9055` maxDD `-16.1026`
- `market_context_high->equity_24h` score `6.2594` n `91` status `ready` deltaP `15.0755` edge `1.3466` maxDD `-42.903`
- `market_context_high->commodity_4h` score `2.9882` n `120` status `ready` deltaP `17.9878` edge `0.1749` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `-0.0418` n `129` status `ready` deltaP `1.8417` edge `0.0265` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.4447` n `129` status `ready` deltaP `4.6593` edge `0.0182` maxDD `-4.5023`
- `market_context_high->fx_24h` score `-0.519` n `91` status `ready` deltaP `4.4719` edge `-0.0003` maxDD `-0.4876`
- `market_context_high->crypto_alt_1h` score `-0.8199` n `129` status `ready` deltaP `2.9325` edge `0.0883` maxDD `-14.7034`
- `market_context_high->fx_1h` score `-0.8987` n `129` status `ready` deltaP `-9.7166` edge `-0.0051` maxDD `-0.6277`
- `market_context_high->equity_1h` score `-1.0616` n `129` status `ready` deltaP `0.5373` edge `0.0089` maxDD `-8.8863`
- `market_context_high->fx_4h` score `-1.3375` n `120` status `ready` deltaP `-12.5711` edge `-0.0033` maxDD `-1.0829`
- `market_context_high->index_4h` score `-1.4218` n `120` status `ready` deltaP `9.6341` edge `0.0444` maxDD `-17.6057`
- `market_context_high->unknown_4h` score `-1.9274` n `120` status `ready` deltaP `4.4411` edge `0.0115` maxDD `-13.8046`
- `market_context_high->crypto_major_1h` score `-2.1978` n `129` status `ready` deltaP `-0.9539` edge `0.0495` maxDD `-15.1032`
- `market_context_high->metal_1h` score `-2.3491` n `129` status `ready` deltaP `-7.0487` edge `-0.0094` maxDD `-7.4828`
- `market_context_high->unknown_1h` score `-2.8707` n `129` status `ready` deltaP `1.9218` edge `-0.0494` maxDD `-14.2111`
- `market_context_high->crypto_alt_4h` score `-3.9383` n `120` status `ready` deltaP `12.2053` edge `0.2182` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-4.0641` n `120` status `ready` deltaP `5.9146` edge `-0.0299` maxDD `-36.7784`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
