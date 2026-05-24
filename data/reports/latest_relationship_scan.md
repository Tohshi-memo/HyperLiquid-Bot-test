# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T21:07:20.248596+00:00`
- Price records: `672`
- Market context records: `1776`
- Flow alert records: `7011`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8872`

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

- `market_context_high->metal_24h` score `7.262` n `179` status `ready` deltaP `28.8398` edge `0.6555` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `6.012` n `194` status `ready` deltaP `21.7076` edge `0.5329` maxDD `-9.1295`
- `news_risk_high->commodity_4h` score `5.8554` n `30` status `ready` deltaP `27.124` edge `0.3726` maxDD `-3.5713`
- `market_context_high->crypto_major_4h` score `4.6252` n `194` status `ready` deltaP `22.935` edge `0.4731` maxDD `-10.9117`
- `market_context_high->index_24h` score `3.6664` n `179` status `ready` deltaP `18.3853` edge `0.3058` maxDD `-4.1604`
- `market_context_high->unknown_4h` score `3.3732` n `194` status `ready` deltaP `14.6875` edge `0.4103` maxDD `-11.1695`
- `market_context_high->equity_4h` score `3.1369` n `194` status `ready` deltaP `16.7793` edge `0.259` maxDD `-5.0894`
- `news_risk_high->commodity_1h` score `3.0384` n `30` status `ready` deltaP `23.6727` edge `0.1271` maxDD `-1.2043`
- `market_context_high->equity_24h` score `2.4425` n `179` status `ready` deltaP `16.4979` edge `0.5834` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `2.2439` n `179` status `ready` deltaP `14.0004` edge `0.6257` maxDD `-35.8966`
- `market_context_high->index_4h` score `0.9775` n `194` status `ready` deltaP `12.4591` edge `0.1073` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `0.9184` n `194` status `ready` deltaP `8.4295` edge `0.1227` maxDD `-4.1892`
- `news_risk_high->fx_4h` score `0.8071` n `30` status `ready` deltaP `20.2643` edge `-0.0044` maxDD `-0.1774`
- `market_context_high->crypto_major_1h` score `0.3658` n `194` status `ready` deltaP `5.5698` edge `0.1007` maxDD `-3.9211`
- `news_risk_high->unknown_4h` score `0.3019` n `30` status `ready` deltaP `9.9796` edge `0.0445` maxDD `-2.7857`
- `market_context_high->equity_1h` score `0.1339` n `194` status `ready` deltaP `5.5513` edge `0.055` maxDD `-2.8014`
- `market_context_high->crypto_major_24h` score `0.1201` n `179` status `ready` deltaP `18.8082` edge `0.7432` maxDD `-62.3533`
- `market_context_high->index_1h` score `-0.0981` n `194` status `ready` deltaP `4.9201` edge `0.0222` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.1268` n `194` status `ready` deltaP `13.4743` edge `0.1631` maxDD `-12.5349`
- `news_risk_high->unknown_1h` score `-0.4473` n `30` status `ready` deltaP `16.8563` edge `-0.1225` maxDD `-2.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
