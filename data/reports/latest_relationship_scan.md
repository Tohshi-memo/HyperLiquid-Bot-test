# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T19:22:35.177714+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `2886`

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

- `news_risk_high->unknown_1h` score `3287.8045` n `31` status `ready` deltaP `1.6322` edge `273.9904` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3181.7133` n `31` status `ready` deltaP `3.3191` edge `265.1263` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `16.3795` n `31` status `ready` deltaP `25.8232` edge `1.1928` maxDD `0.0`
- `news_risk_high->equity_24h` score `12.6053` n `31` status `ready` deltaP `23.9168` edge `0.891` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `12.0072` n `31` status `ready` deltaP `25.6499` edge `0.8296` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.073` n `31` status `ready` deltaP `20.8916` edge `0.6205` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `5.4029` n `31` status `ready` deltaP `29.6853` edge `0.3004` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `4.9596` n `31` status `ready` deltaP `13.3451` edge `0.6886` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.655` n `31` status `ready` deltaP `38.6762` edge `0.1429` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.776` n `31` status `ready` deltaP `12.1877` edge `0.2609` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.3402` n `31` status `ready` deltaP `28.9243` edge `0.0282` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.2481` n `31` status `ready` deltaP `27.6512` edge `0.0115` maxDD `-0.0136`
- `news_risk_high->index_24h` score `2.228` n `31` status `ready` deltaP `24.6101` edge `0.0216` maxDD `0.0`
- `news_risk_high->equity_1h` score `2.1855` n `31` status `ready` deltaP `15.0473` edge `0.1005` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `1.8437` n `31` status `ready` deltaP `5.9687` edge `0.2427` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.6446` n `31` status `ready` deltaP `8.5136` edge `0.1898` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1434` n `31` status `ready` deltaP `24.7923` edge `0.0092` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.4284` n `31` status `ready` deltaP `10.4237` edge `0.0252` maxDD `-0.5151`
- `news_risk_high->metal_4h` score `0.3734` n `31` status `ready` deltaP `11.6708` edge `0.0258` maxDD `-0.7918`
- `news_risk_high->commodity_1h` score `-0.322` n `31` status `ready` deltaP `-1.7626` edge `0.0111` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
