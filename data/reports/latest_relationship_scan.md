# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T20:22:32.088274+00:00`
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

- `market_context_high->unknown_1h` score `32268.095` n `45` status `ready` deltaP `1.4171` edge `2689.0079` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `22063.5901` n `45` status `ready` deltaP `3.1776` edge `1838.6252` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `1033.1401` n `31` status `ready` deltaP `1.6322` edge `86.1017` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `810.6426` n `31` status `ready` deltaP `4.3962` edge `67.5299` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `38.4923` n `31` status `ready` deltaP `50.1736` edge `2.8732` maxDD `0.0`
- `news_risk_high->equity_24h` score `36.8449` n `31` status `ready` deltaP `43.5764` edge `2.7799` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `34.0067` n `31` status `ready` deltaP `48.9583` edge `2.5075` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.7101` n `31` status `ready` deltaP `26.4555` edge `0.8865` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.099` n `31` status `ready` deltaP `41.2355` edge `0.6775` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `10.3192` n `31` status `ready` deltaP `34.6332` edge `0.6771` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.2759` n `31` status `ready` deltaP `17.5403` edge `0.9576` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `6.0426` n `31` status `ready` deltaP `51.0865` edge `0.1758` maxDD `-0.0262`
- `news_risk_high->index_24h` score `5.5214` n `31` status `ready` deltaP `41.4931` edge `0.1835` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.5205` n `31` status `ready` deltaP `18.7898` edge `0.1868` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.0599` n `31` status `ready` deltaP `32.9564` edge `0.0613` maxDD `-0.4146`
- `market_context_high->fx_4h` score `2.7403` n `45` status `ready` deltaP `33.2893` edge `0.0349` maxDD `-0.2774`
- `news_risk_high->crypto_major_1h` score `2.6776` n `31` status `ready` deltaP `12.2561` edge `0.3077` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.5416` n `31` status `ready` deltaP `30.1961` edge `0.019` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.3369` n `31` status `ready` deltaP `11.9567` edge `0.2556` maxDD `-1.5232`
- `news_risk_high->metal_4h` score `1.6525` n `31` status `ready` deltaP `21.8086` edge `0.1222` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
