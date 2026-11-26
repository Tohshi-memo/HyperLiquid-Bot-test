# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T07:37:23.301402+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4007`

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

- `news_risk_high->unknown_4h` score `3242.7847` n `31` status `ready` deltaP `3.4815` edge `270.2145` maxDD `-0.1191`
- `news_risk_high->unknown_1h` score `3219.1729` n `31` status `ready` deltaP `1.6322` edge `268.2711` maxDD `-0.7395`
- `market_context_high->unknown_1h` score `88.881` n `31` status `ready` deltaP `1.6322` edge `7.4053` maxDD `-0.4209`
- `news_risk_high->equity_24h` score `40.0798` n `31` status `ready` deltaP `46.5278` edge `3.0298` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `38.5209` n `31` status `ready` deltaP `47.3958` edge `2.8941` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `32.9093` n `31` status `ready` deltaP `46.7014` edge `2.4311` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `10.9455` n `31` status `ready` deltaP `27.2177` edge `0.8177` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.5688` n `31` status `ready` deltaP `38.4442` edge `0.6725` maxDD `-2.178`
- `news_risk_high->metal_24h` score `9.6423` n `31` status `ready` deltaP `33.0758` edge `0.6105` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `6.8794` n `31` status `ready` deltaP `18.1501` edge `0.9027` maxDD `-7.6714`
- `news_risk_high->index_24h` score `6.5921` n `31` status `ready` deltaP `47.9167` edge `0.2299` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.3329` n `31` status `ready` deltaP `45.5309` edge `0.1537` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.7566` n `31` status `ready` deltaP `20.4365` edge `0.1955` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.4748` n `31` status `ready` deltaP `37.3771` edge `0.0664` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7321` n `31` status `ready` deltaP `32.2919` edge `0.0209` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.5008` n `31` status `ready` deltaP `10.1603` edge `0.299` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.3032` n `31` status `ready` deltaP `13.4537` edge `0.2413` maxDD `-1.5232`
- `market_context_high->fx_4h` score `2.1372` n `31` status `ready` deltaP `27.1145` edge `0.0258` maxDD `-0.2774`
- `news_risk_high->metal_1h` score `1.5079` n `31` status `ready` deltaP `29.433` edge `0.025` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.1054` n `31` status `ready` deltaP `16.7781` edge `0.0856` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
