# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T21:37:29.728033+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4068`

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

- `market_context_high->unknown_1h` score `32267.7998` n `45` status `ready` deltaP `1.4171` edge `2688.9833` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `22032.6217` n `45` status `ready` deltaP `3.1776` edge `1836.0445` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `1032.8449` n `31` status `ready` deltaP `1.6322` edge `86.0771` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `779.6742` n `31` status `ready` deltaP `4.3962` edge `64.9492` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `38.6351` n `31` status `ready` deltaP `50.1736` edge `2.8851` maxDD `0.0`
- `news_risk_high->equity_24h` score `37.2579` n `31` status `ready` deltaP `43.9236` edge `2.812` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `34.2575` n `31` status `ready` deltaP `48.9583` edge `2.5284` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.8115` n `31` status `ready` deltaP `26.9128` edge `0.8919` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.099` n `31` status `ready` deltaP `41.2355` edge `0.6775` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `10.4717` n `31` status `ready` deltaP `34.7856` edge `0.6888` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.3291` n `31` status `ready` deltaP `17.6927` edge `0.9634` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `5.9323` n `31` status `ready` deltaP `50.2184` edge `0.1724` maxDD `-0.0262`
- `news_risk_high->index_24h` score `5.5768` n `31` status `ready` deltaP `41.8403` edge `0.1858` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.5996` n `31` status `ready` deltaP `18.9395` edge `0.1924` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.0707` n `31` status `ready` deltaP `32.9564` edge `0.0622` maxDD `-0.4146`
- `market_context_high->fx_4h` score `2.7367` n `45` status `ready` deltaP `33.2893` edge `0.0346` maxDD `-0.2774`
- `news_risk_high->crypto_major_1h` score `2.6909` n `31` status `ready` deltaP `12.4058` edge `0.3084` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.5596` n `31` status `ready` deltaP `30.3458` edge `0.0195` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.358` n `31` status `ready` deltaP `12.1064` edge `0.2573` maxDD `-1.5232`
- `news_risk_high->metal_4h` score `1.6447` n `31` status `ready` deltaP `21.8086` edge `0.1212` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
