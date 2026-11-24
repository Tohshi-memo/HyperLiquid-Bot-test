# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T09:07:41.775142+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4584`

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

- `market_context_high->unknown_1h` score `32333.2287` n `45` status `ready` deltaP `1.4171` edge `2694.4357` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22198.545` n `45` status `ready` deltaP `2.5678` edge `1849.8755` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1123.6993` n `31` status `ready` deltaP `1.6322` edge `93.6483` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `963.1919` n `31` status `ready` deltaP `3.7864` edge `80.2464` maxDD `-0.119`
- `news_risk_high->crypto_major_24h` score `35.3402` n `31` status `ready` deltaP `47.2222` edge `2.6302` maxDD `0.0`
- `news_risk_high->equity_24h` score `34.7018` n `31` status `ready` deltaP `41.4931` edge `2.6152` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `30.5756` n `31` status `ready` deltaP `44.9653` edge `2.2482` maxDD `0.0`
- `news_risk_high->metal_24h` score `11.4153` n `31` status `ready` deltaP `41.4091` edge `0.7027` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.4094` n `31` status `ready` deltaP `22.797` edge `0.8025` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.7963` n `31` status `ready` deltaP `31.432` edge `0.5717` maxDD `-2.1911`
- `news_risk_high->fx_24h` score `6.7011` n `31` status `ready` deltaP `56.4684` edge `0.1948` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `6.5679` n `31` status `ready` deltaP `14.0342` edge `0.8902` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.2406` n `31` status `ready` deltaP `39.0625` edge `0.1763` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.2145` n `31` status `ready` deltaP `17.7419` edge `0.1683` maxDD `-0.163`
- `market_context_high->fx_4h` score `2.9908` n `45` status `ready` deltaP `35.8807` edge `0.0385` maxDD `-0.2774`
- `news_risk_high->index_4h` score `2.7594` n `31` status `ready` deltaP `30.6698` edge `0.0515` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.4937` n `31` status `ready` deltaP `10.7591` edge `0.2941` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.4614` n `31` status `ready` deltaP `29.4476` edge `0.0173` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.1062` n `31` status `ready` deltaP `10.31` edge `0.237` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.6349` n `31` status `ready` deltaP `31.0797` edge `0.0303` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
