# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T05:07:27.781542+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3642`

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

- `news_risk_high->unknown_1h` score `3335.1289` n `31` status `ready` deltaP `1.4825` edge `277.9351` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3188.3253` n `31` status `ready` deltaP `3.634` edge `265.6752` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `19.1441` n `31` status `ready` deltaP `30.156` edge `1.3943` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `13.2633` n `31` status `ready` deltaP `28.0763` edge `0.9181` maxDD `0.0`
- `news_risk_high->equity_24h` score `11.4053` n `31` status `ready` deltaP `23.9168` edge `0.791` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `7.3429` n `31` status `ready` deltaP `19.5957` edge `0.5683` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `5.005` n `31` status `ready` deltaP `27.621` edge `0.281` maxDD `-2.178`
- `news_risk_high->fx_24h` score `4.7402` n `31` status `ready` deltaP `38.6762` edge `0.15` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `4.5301` n `31` status `ready` deltaP `13.5769` edge `0.632` maxDD `-7.6714`
- `news_risk_high->metal_24h` score `3.356` n `31` status `ready` deltaP `12.1877` edge `0.2259` maxDD `-0.1986`
- `news_risk_high->index_1h` score `2.2193` n `31` status `ready` deltaP `27.3518` edge `0.0111` maxDD `-0.0136`
- `news_risk_high->index_24h` score `2.1836` n `31` status `ready` deltaP `24.6101` edge `0.0179` maxDD `0.0`
- `news_risk_high->index_4h` score `2.1727` n `31` status `ready` deltaP `27.0112` edge `0.027` maxDD `-0.4146`
- `news_risk_high->equity_1h` score `2.0428` n `31` status `ready` deltaP `13.9994` edge `0.0956` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `1.6519` n `31` status `ready` deltaP `5.0705` edge `0.2241` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.5456` n `31` status `ready` deltaP `8.3639` edge `0.1781` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.0772` n `31` status `ready` deltaP `23.7444` edge `0.0077` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.3262` n `31` status `ready` deltaP `8.3694` edge `0.0258` maxDD `-0.5151`
- `news_risk_high->metal_4h` score `0.2165` n `31` status `ready` deltaP `9.6135` edge `0.0194` maxDD `-0.7918`
- `news_risk_high->commodity_1h` score `-0.3495` n `31` status `ready` deltaP `-2.2117` edge `0.0118` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
