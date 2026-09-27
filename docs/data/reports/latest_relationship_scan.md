# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T01:37:25.546742+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11444`

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

- `news_risk_high->unknown_24h` score `3142.32` n `98` status `ready` deltaP `1.2153` edge `261.8519` maxDD `0.0`
- `market_context_high->unknown_1h` score `74.7975` n `44` status `ready` deltaP `10.1524` edge `6.1701` maxDD `-0.0395`
- `market_context_high->crypto_major_24h` score `51.2881` n `44` status `ready` deltaP `27.5884` edge `4.1252` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `27.8142` n `44` status `ready` deltaP `14.9148` edge `2.2564` maxDD `-2.7051`
- `market_context_high->equity_24h` score `27.7168` n `44` status `ready` deltaP `36.0954` edge `2.1005` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.6745` n `44` status `ready` deltaP `31.5815` edge `0.4378` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.6669` n `44` status `ready` deltaP `31.7866` edge `0.1175` maxDD `-0.2401`
- `market_context_high->index_4h` score `3.4005` n `44` status `ready` deltaP `38.1374` edge `0.0362` maxDD `-0.2323`
- `market_context_high->equity_4h` score `3.0498` n `44` status `ready` deltaP `18.5837` edge `0.1679` maxDD `-1.3444`
- `market_context_high->crypto_alt_4h` score `1.4281` n `44` status `ready` deltaP `9.6175` edge `0.1175` maxDD `-3.3417`
- `news_risk_high->index_24h` score `1.3123` n `98` status `ready` deltaP `18.5481` edge `0.0469` maxDD `-2.2287`
- `market_context_high->crypto_major_1h` score `1.1815` n `44` status `ready` deltaP `9.2678` edge `0.1101` maxDD `-4.5405`
- `market_context_high->equity_1h` score `1.1294` n `44` status `ready` deltaP `12.466` edge `0.0513` maxDD `-1.5564`
- `news_risk_high->metal_24h` score `1.1129` n `98` status `ready` deltaP `25.9425` edge `0.1345` maxDD `-6.8481`
- `market_context_high->crypto_major_4h` score `1.0528` n `44` status `ready` deltaP `7.6774` edge `0.127` maxDD `-5.2359`
- `market_context_high->index_1h` score `0.8152` n `44` status `ready` deltaP `12.3163` edge `0.0095` maxDD `-0.2275`
- `market_context_high->metal_1h` score `0.2599` n `44` status `ready` deltaP `6.3146` edge `0.0112` maxDD `-0.1976`
- `market_context_high->crypto_alt_1h` score `0.1662` n `44` status `ready` deltaP `4.4502` edge `0.0731` maxDD `-5.7799`
- `market_context_high->fx_1h` score `0.1469` n `44` status `ready` deltaP `7.2128` edge `0.0064` maxDD `-0.1854`
- `news_risk_high->index_1h` score `-0.1058` n `139` status `ready` deltaP `2.5223` edge `0.0035` maxDD `-0.3305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
