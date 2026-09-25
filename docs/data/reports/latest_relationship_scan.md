# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T05:22:27.978330+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11226`

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

- `market_context_high->unknown_1h` score `85.8453` n `47` status `ready` deltaP `8.7687` edge `7.1024` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `49.0632` n `47` status `ready` deltaP `30.5962` edge `3.9239` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `31.996` n `47` status `ready` deltaP `24.782` edge `2.5391` maxDD `-2.7051`
- `market_context_high->equity_24h` score `26.107` n `47` status `ready` deltaP `34.7628` edge `1.9794` maxDD `-2.1786`
- `market_context_high->index_24h` score `8.2652` n `47` status `ready` deltaP `38.9295` edge `0.4422` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.7466` n `47` status `ready` deltaP `40.0931` edge `0.1521` maxDD `-0.2401`
- `news_risk_high->commodity_24h` score `3.6639` n `54` status `ready` deltaP `30.3819` edge `0.1376` maxDD `-1.7857`
- `market_context_high->index_4h` score `2.9631` n `47` status `ready` deltaP `33.8739` edge `0.0365` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.5751` n `47` status `ready` deltaP `17.1445` edge `0.1421` maxDD `-1.3444`
- `news_risk_high->unknown_1h` score `1.3292` n `116` status `ready` deltaP `2.6792` edge `0.1068` maxDD `-0.4452`
- `news_risk_high->crypto_alt_1h` score `1.3108` n `116` status `ready` deltaP `11.5941` edge `0.123` maxDD `-4.2849`
- `market_context_high->crypto_alt_4h` score `1.01` n `47` status `ready` deltaP `9.2306` edge `0.0894` maxDD `-3.3417`
- `market_context_high->equity_1h` score `0.9762` n `47` status `ready` deltaP `11.7658` edge `0.0432` maxDD `-1.5564`
- `market_context_high->index_1h` score `0.9595` n `47` status `ready` deltaP `14.6101` edge `0.0104` maxDD `-0.2275`
- `news_risk_high->crypto_major_1h` score `0.474` n `116` status `ready` deltaP `7.9909` edge `0.0608` maxDD `-3.2991`
- `market_context_high->fx_1h` score `0.3524` n `47` status `ready` deltaP `8.7622` edge `0.0066` maxDD `-0.1854`
- `market_context_high->metal_1h` score `0.0585` n `47` status `ready` deltaP `4.026` edge `0.0123` maxDD `-0.1976`
- `news_risk_high->metal_1h` score `0.0538` n `116` status `ready` deltaP `8.5381` edge `0.0105` maxDD `-0.7016`
- `market_context_high->crypto_major_1h` score `-0.1205` n `47` status `ready` deltaP `2.5067` edge `0.055` maxDD `-4.5405`
- `news_risk_high->equity_1h` score `-0.2103` n `116` status `ready` deltaP `0.9808` edge `0.0245` maxDD `-2.6402`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
