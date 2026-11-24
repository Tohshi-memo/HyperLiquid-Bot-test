# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T19:22:36.316025+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4092`

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

- `market_context_high->unknown_1h` score `32271.4706` n `45` status `ready` deltaP `1.4171` edge `2689.2892` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `22082.2225` n `45` status `ready` deltaP `3.1776` edge `1840.1779` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `1036.5157` n `31` status `ready` deltaP `1.6322` edge `86.383` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `829.275` n `31` status `ready` deltaP `4.3962` edge `69.0826` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `38.2979` n `31` status `ready` deltaP `50.1736` edge `2.857` maxDD `0.0`
- `news_risk_high->equity_24h` score `36.4684` n `31` status `ready` deltaP `43.0556` edge `2.752` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `33.718` n `31` status `ready` deltaP `48.7847` edge `2.4846` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.5451` n `31` status `ready` deltaP `25.9982` edge `0.8758` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.1026` n `31` status `ready` deltaP `41.2355` edge `0.6778` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `10.109` n `31` status `ready` deltaP `34.4808` edge `0.6606` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.1593` n `31` status `ready` deltaP `17.083` edge `0.9457` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `6.1329` n `31` status `ready` deltaP `51.7809` edge `0.1787` maxDD `-0.0262`
- `news_risk_high->index_24h` score `5.4419` n `31` status `ready` deltaP `40.7986` edge `0.1815` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.4114` n `31` status `ready` deltaP `18.191` edge `0.1817` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.0431` n `31` status `ready` deltaP `32.9564` edge `0.0599` maxDD `-0.4146`
- `market_context_high->fx_4h` score `2.7671` n `45` status `ready` deltaP `33.5942` edge `0.0351` maxDD `-0.2774`
- `news_risk_high->crypto_major_1h` score `2.6075` n `31` status `ready` deltaP `11.6573` edge `0.3027` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.4853` n `31` status `ready` deltaP `29.5973` edge `0.0183` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.2582` n `31` status `ready` deltaP `11.3579` edge `0.2495` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.6241` n `31` status `ready` deltaP `30.4809` edge `0.0329` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
