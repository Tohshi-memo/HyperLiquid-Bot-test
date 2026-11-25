# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T14:37:34.952178+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3744`

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

- `market_context_high->unknown_1h` score `32207.6053` n `45` status `ready` deltaP `2.465` edge `2683.9601` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21923.6449` n `45` status `ready` deltaP `3.1776` edge `1826.9631` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `972.6503` n `31` status `ready` deltaP `2.6801` edge `81.0539` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `670.6974` n `31` status `ready` deltaP `4.3962` edge `55.8678` maxDD `-0.1191`
- `news_risk_high->unknown_24h` score `507.0911` n `31` status `ready` deltaP `5.7292` edge `42.2194` maxDD `0.0`
- `news_risk_high->equity_24h` score `44.7817` n `31` status `ready` deltaP `50.5208` edge `3.395` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `41.6787` n `31` status `ready` deltaP `52.0833` edge `3.126` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `38.3122` n `31` status `ready` deltaP `54.6875` edge `2.8281` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.8985` n `31` status `ready` deltaP `27.3701` edge `0.8961` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.8634` n `31` status `ready` deltaP `41.2355` edge `0.7412` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `11.2293` n `31` status `ready` deltaP `37.8344` edge `0.7316` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.4854` n `31` status `ready` deltaP `19.0647` edge `0.9743` maxDD `-7.6714`
- `news_risk_high->index_24h` score `7.1308` n `31` status `ready` deltaP `51.2153` edge `0.2528` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.3179` n `31` status `ready` deltaP `45.3573` edge `0.1536` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `4.0253` n `31` status `ready` deltaP `20.8856` edge `0.2149` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.4086` n `31` status `ready` deltaP `36.31` edge `0.068` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.7682` n `31` status `ready` deltaP `11.807` edge `0.3223` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.7214` n `31` status `ready` deltaP `31.9925` edge `0.022` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.513` n `31` status `ready` deltaP `13.6034` edge `0.2672` maxDD `-1.5232`
- `market_context_high->fx_4h` score `2.4834` n `45` status `ready` deltaP `30.3929` edge `0.0328` maxDD `-0.2774`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
