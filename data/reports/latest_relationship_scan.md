# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T20:07:34.746690+00:00`
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

- `market_context_high->unknown_1h` score `32268.0974` n `45` status `ready` deltaP `1.4171` edge `2689.0081` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `22071.7153` n `45` status `ready` deltaP `3.1776` edge `1839.3023` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `1033.1425` n `31` status `ready` deltaP `1.6322` edge `86.1019` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `818.7678` n `31` status `ready` deltaP `4.3962` edge `68.207` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `38.4479` n `31` status `ready` deltaP `50.1736` edge `2.8695` maxDD `0.0`
- `news_risk_high->equity_24h` score `36.7573` n `31` status `ready` deltaP `43.5764` edge `2.7726` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `33.9383` n `31` status `ready` deltaP `48.9583` edge `2.5018` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.6727` n `31` status `ready` deltaP `26.3031` edge `0.8844` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.099` n `31` status `ready` deltaP `41.2355` edge `0.6775` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `10.2796` n `31` status `ready` deltaP `34.6332` edge `0.6738` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.2493` n `31` status `ready` deltaP `17.3879` edge `0.9552` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `6.0649` n `31` status `ready` deltaP `51.2601` edge `0.1765` maxDD `-0.0262`
- `news_risk_high->index_24h` score `5.5004` n `31` status `ready` deltaP `41.3194` edge `0.1829` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.4833` n `31` status `ready` deltaP `18.6401` edge `0.1847` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.0563` n `31` status `ready` deltaP `32.9564` edge `0.061` maxDD `-0.4146`
- `market_context_high->fx_4h` score `2.7403` n `45` status `ready` deltaP `33.2893` edge `0.0349` maxDD `-0.2774`
- `news_risk_high->crypto_major_1h` score `2.6597` n `31` status `ready` deltaP `12.1064` edge `0.3064` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.5261` n `31` status `ready` deltaP `30.0464` edge `0.0187` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.3159` n `31` status `ready` deltaP `11.807` edge `0.2539` maxDD `-1.5232`
- `news_risk_high->metal_4h` score `1.6438` n `31` status `ready` deltaP `21.6562` edge `0.1221` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
