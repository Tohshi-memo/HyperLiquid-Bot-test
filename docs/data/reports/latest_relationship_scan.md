# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T12:07:26.370807+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3467`

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

- `news_risk_high->unknown_1h` score `3233.694` n `31` status `ready` deltaP `1.7819` edge `269.4802` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3223.1647` n `31` status `ready` deltaP `3.4815` edge `268.5795` maxDD `-0.1191`
- `market_context_high->unknown_1h` score `103.4022` n `31` status `ready` deltaP `1.7819` edge `8.6144` maxDD `-0.4209`
- `news_risk_high->crypto_major_24h` score `35.8385` n `31` status `ready` deltaP `44.2708` edge `2.6914` maxDD `0.0`
- `news_risk_high->equity_24h` score `35.7186` n `31` status `ready` deltaP `43.4028` edge `2.6872` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `30.0217` n `31` status `ready` deltaP `43.5764` edge `2.2113` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `10.8677` n `31` status `ready` deltaP `27.3701` edge `0.8102` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.7022` n `31` status `ready` deltaP `39.5112` edge `0.6765` maxDD `-2.178`
- `news_risk_high->metal_24h` score `8.6255` n `31` status `ready` deltaP `29.9508` edge `0.5466` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `7.0016` n `31` status `ready` deltaP `19.6744` edge `0.9082` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.9581` n `31` status `ready` deltaP `44.7917` edge `0.1979` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.0181` n `31` status `ready` deltaP `42.4059` edge `0.1483` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.8189` n `31` status `ready` deltaP `20.8856` edge `0.1977` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.5358` n `31` status `ready` deltaP `38.1393` edge `0.0664` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7752` n `31` status `ready` deltaP `32.741` edge `0.0215` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.5` n `31` status `ready` deltaP `10.0106` edge `0.2999` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.2549` n `31` status `ready` deltaP `12.8549` edge `0.2391` maxDD `-1.5232`
- `market_context_high->fx_4h` score `1.9728` n `31` status `ready` deltaP `25.2853` edge `0.0243` maxDD `-0.2774`
- `news_risk_high->metal_1h` score `1.4861` n `31` status `ready` deltaP `29.1336` edge `0.0242` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.0298` n `31` status `ready` deltaP `15.8635` edge `0.082` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
