# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T07:22:17.048225+00:00`
- Price records: `672`
- Market context records: `1095`
- Flow alert records: `5058`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8686`

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

- `market_context_high->crypto_major_24h` score `16.6519` n `150` status `ready` deltaP `36.1667` edge `1.1929` maxDD `-3.3749`
- `market_context_high->equity_24h` score `6.0527` n `150` status `ready` deltaP `15.6527` edge `0.4497` maxDD `-3.6396`
- `market_context_high->crypto_alt_24h` score `5.879` n `150` status `ready` deltaP `12.5277` edge `0.5298` maxDD `-9.5387`
- `market_context_high->metal_24h` score `5.1659` n `150` status `ready` deltaP `-3.1041` edge `0.6179` maxDD `-6.3373`
- `market_context_high->index_24h` score `4.7853` n `150` status `ready` deltaP `15.1319` edge `0.3287` maxDD `-2.1308`
- `market_context_high->equity_4h` score `2.1299` n `165` status `ready` deltaP `11.808` edge `0.1651` maxDD `-3.6396`
- `market_context_high->index_4h` score `1.1309` n `165` status `ready` deltaP `9.6961` edge `0.0979` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.5732` n `168` status `ready` deltaP `8.2442` edge `0.0245` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.4144` n `168` status `ready` deltaP `3.1793` edge `0.0511` maxDD `-1.3546`
- `market_context_high->crypto_major_4h` score `0.3524` n `165` status `ready` deltaP `9.0817` edge `0.147` maxDD `-7.2544`
- `market_context_high->fx_1h` score `0.1256` n `168` status `ready` deltaP `8.1658` edge `0.0016` maxDD `-0.3124`
- `market_context_high->crypto_major_1h` score `0.0777` n `168` status `ready` deltaP `7.2819` edge `0.0345` maxDD `-4.1256`
- `market_context_high->metal_1h` score `-0.0937` n `168` status `ready` deltaP `7.5492` edge `0.0029` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.3018` n `168` status `ready` deltaP `2.7944` edge `0.0405` maxDD `-3.4088`
- `market_context_high->fx_4h` score `-0.6384` n `165` status `ready` deltaP `2.4002` edge `0.0018` maxDD `-1.6381`
- `market_context_high->commodity_1h` score `-0.7458` n `168` status `ready` deltaP `-1.6253` edge `-0.004` maxDD `-3.7959`
- `market_context_high->crypto_alt_4h` score `-0.8545` n `165` status `ready` deltaP `5.3788` edge `0.1279` maxDD `-14.8652`
- `market_context_high->metal_4h` score `-2.2263` n `165` status `ready` deltaP `7.6616` edge `-0.0412` maxDD `-9.2991`
- `market_context_high->unknown_4h` score `-2.5392` n `165` status `ready` deltaP `9.8327` edge `-0.1555` maxDD `-6.7322`
- `market_context_high->commodity_4h` score `-3.111` n `165` status `ready` deltaP `-10.558` edge `-0.0117` maxDD `-13.0076`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
