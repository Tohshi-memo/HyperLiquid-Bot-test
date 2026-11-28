# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T08:07:31.774667+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3740`

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

- `news_risk_high->unknown_1h` score `3356.7445` n `31` status `ready` deltaP `1.6322` edge `279.7354` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3236.0325` n `31` status `ready` deltaP `3.634` edge `269.6508` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `20.8021` n `31` status `ready` deltaP `32.2357` edge `1.5186` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `14.7449` n `31` status `ready` deltaP `30.156` edge `1.0277` maxDD `0.0`
- `news_risk_high->equity_24h` score `11.8632` n `31` status `ready` deltaP `25.6499` edge `0.8176` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.0215` n `31` status `ready` deltaP `20.9677` edge `0.6157` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `5.2299` n `31` status `ready` deltaP `28.993` edge `0.2906` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `4.9408` n `31` status `ready` deltaP `14.9488` edge `0.6755` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.8605` n `31` status `ready` deltaP `39.716` edge `0.1531` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.5853` n `31` status `ready` deltaP `14.0941` edge `0.2323` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.2981` n `31` status `ready` deltaP `28.3832` edge `0.0283` maxDD `-0.4146`
- `news_risk_high->index_24h` score `2.2691` n `31` status `ready` deltaP `25.3033` edge `0.0204` maxDD `0.0`
- `news_risk_high->index_1h` score `2.2624` n `31` status `ready` deltaP `27.8009` edge `0.0117` maxDD `-0.0136`
- `news_risk_high->equity_1h` score `2.0909` n `31` status `ready` deltaP `13.8497` edge `0.1006` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `1.7868` n `31` status `ready` deltaP `5.3699` edge `0.2394` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.6291` n `31` status `ready` deltaP `8.2142` edge `0.1898` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.0897` n `31` status `ready` deltaP `23.8941` edge `0.0083` maxDD `-0.2315`
- `market_context_high->equity_1h` score `0.6077` n `37` status `ready` deltaP `13.6754` edge `0.0276` maxDD `-1.2685`
- `news_risk_high->commodity_4h` score `0.316` n `31` status `ready` deltaP `8.2169` edge `0.0255` maxDD `-0.5151`
- `news_risk_high->metal_4h` score `0.3035` n `31` status `ready` deltaP `10.9854` edge `0.0214` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
