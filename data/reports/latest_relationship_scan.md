# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T08:22:28.590450+00:00`
- Price records: `672`
- Market context records: `6479`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5869`

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

- `news_risk_high->crypto_alt_24h` score `12.5466` n `32` status `ready` deltaP `33.8542` edge `0.8346` maxDD `-0.5131`
- `market_context_high->unknown_24h` score `6.8389` n `156` status `ready` deltaP `16.266` edge `0.7915` maxDD `-15.0689`
- `news_risk_high->fx_24h` score `6.433` n `32` status `ready` deltaP `53.4722` edge `0.1796` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.2396` n `32` status `ready` deltaP `16.3194` edge `0.5127` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `3.9571` n `37` status `ready` deltaP `41.9331` edge `0.0548` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.1157` n `32` status `ready` deltaP `28.9931` edge `0.0869` maxDD `-0.3101`
- `market_context_high->unknown_1h` score `1.9203` n `177` status `ready` deltaP `-4.7058` edge `0.2815` maxDD `-3.2083`
- `news_risk_high->fx_1h` score `1.8191` n `38` status `ready` deltaP `22.7624` edge `0.0179` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `0.5567` n `38` status `ready` deltaP `4.751` edge `0.0934` maxDD `-2.6299`
- `market_context_high->index_4h` score `0.4721` n `172` status `ready` deltaP `11.8017` edge `0.0283` maxDD `-0.4108`
- `market_context_high->unknown_4h` score `0.2556` n `172` status `ready` deltaP `-15.5453` edge `0.3655` maxDD `-10.5788`
- `market_context_high->crypto_alt_4h` score `0.2512` n `172` status `ready` deltaP `8.5508` edge `0.1193` maxDD `-6.7632`
- `market_context_high->commodity_24h` score `0.2343` n `156` status `ready` deltaP `6.1566` edge `0.1653` maxDD `-5.2791`
- `market_context_high->metal_4h` score `0.1591` n `172` status `ready` deltaP `11.7413` edge `0.0438` maxDD `-2.7056`
- `news_risk_high->crypto_alt_1h` score `0.0555` n `38` status `ready` deltaP `1.2843` edge `0.0495` maxDD `-2.0756`
- `news_risk_high->index_24h` score `-0.4579` n `32` status `ready` deltaP `4.6875` edge `-0.0028` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.4721` n `172` status `ready` deltaP `8.1395` edge `0.0551` maxDD `-8.2573`
- `news_risk_high->unknown_1h` score `-0.4761` n `38` status `ready` deltaP `4.6013` edge `-0.0332` maxDD `-0.9718`
- `market_context_high->metal_1h` score `-0.527` n `177` status `ready` deltaP `1.3642` edge `0.0011` maxDD `-1.8877`
- `market_context_high->index_1h` score `-0.6251` n `177` status `ready` deltaP `-1.8277` edge `0.004` maxDD `-0.7564`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
