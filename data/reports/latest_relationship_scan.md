# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T06:37:26.895667+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3995`

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

- `news_risk_high->unknown_4h` score `3223.7347` n `31` status `ready` deltaP `3.4815` edge `268.627` maxDD `-0.1191`
- `news_risk_high->unknown_1h` score `3223.2937` n `31` status `ready` deltaP `1.4825` edge `268.6155` maxDD `-0.7395`
- `market_context_high->unknown_1h` score `93.0019` n `31` status `ready` deltaP `1.4825` edge `7.7497` maxDD `-0.4209`
- `news_risk_high->equity_24h` score `40.949` n `31` status `ready` deltaP `47.2222` edge `3.0976` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `39.0192` n `31` status `ready` deltaP `48.0903` edge `2.931` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `33.4581` n `31` status `ready` deltaP `47.3958` edge `2.4722` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `10.8609` n `31` status `ready` deltaP `26.7604` edge `0.8137` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.4397` n `31` status `ready` deltaP `37.8344` edge `0.6658` maxDD `-2.178`
- `news_risk_high->metal_24h` score `9.8898` n `31` status `ready` deltaP `33.7702` edge `0.6265` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `6.8283` n `31` status `ready` deltaP `17.6927` edge `0.8992` maxDD `-7.6714`
- `news_risk_high->index_24h` score `6.7197` n `31` status `ready` deltaP `48.6111` edge `0.2359` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.3655` n `31` status `ready` deltaP `45.8782` edge `0.1541` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.7446` n `31` status `ready` deltaP `20.4365` edge `0.1945` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.4128` n `31` status `ready` deltaP `36.7673` edge `0.0653` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7058` n `31` status `ready` deltaP `31.9925` edge `0.0207` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.5016` n `31` status `ready` deltaP `10.31` edge `0.2981` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.2689` n `31` status `ready` deltaP `13.0046` edge `0.2399` maxDD `-1.5232`
- `market_context_high->fx_4h` score `2.1068` n `31` status `ready` deltaP `26.8096` edge `0.0253` maxDD `-0.2774`
- `news_risk_high->metal_1h` score `1.5165` n `31` status `ready` deltaP `29.5827` edge `0.0251` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.0936` n `31` status `ready` deltaP `16.6257` edge `0.0851` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
