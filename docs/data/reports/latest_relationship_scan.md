# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T22:37:24.827452+00:00`
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

- `news_risk_high->unknown_24h` score `4322.832` n `86` status `ready` deltaP `1.2153` edge `360.2279` maxDD `0.0`
- `market_context_high->unknown_1h` score `70.5379` n `45` status `ready` deltaP `10.2029` edge `5.8148` maxDD `-0.0395`
- `market_context_high->crypto_major_24h` score `49.5967` n `45` status `ready` deltaP `25.5556` edge `3.9978` maxDD `-2.4756`
- `market_context_high->equity_24h` score `27.0847` n `45` status `ready` deltaP `35.7986` edge `2.0498` maxDD `-2.1786`
- `market_context_high->crypto_alt_24h` score `26.8631` n `45` status `ready` deltaP `14.9653` edge `2.1768` maxDD `-2.7051`
- `market_context_high->index_24h` score `7.4434` n `45` status `ready` deltaP `30.4167` edge `0.4263` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.5957` n `45` status `ready` deltaP `31.0764` edge `0.1163` maxDD `-0.2401`
- `market_context_high->index_4h` score `3.3018` n `45` status `ready` deltaP `37.0833` edge `0.035` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.9548` n `45` status `ready` deltaP `18.6958` edge `0.1634` maxDD `-1.3444`
- `news_risk_high->index_24h` score `1.9734` n `86` status `ready` deltaP `23.3366` edge `0.0659` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `1.3885` n `86` status `ready` deltaP `30.0428` edge `0.1425` maxDD `-6.8481`
- `market_context_high->crypto_alt_4h` score `1.2034` n `45` status `ready` deltaP `9.0684` edge `0.1066` maxDD `-3.3417`
- `market_context_high->equity_1h` score `1.1816` n `45` status `ready` deltaP `13.2236` edge `0.0506` maxDD `-1.5564`
- `market_context_high->crypto_major_1h` score `1.1227` n `45` status `ready` deltaP `8.6527` edge `0.1093` maxDD `-4.5405`
- `market_context_high->crypto_major_4h` score `0.9918` n `45` status `ready` deltaP `7.8895` edge `0.1205` maxDD `-5.2359`
- `news_risk_high->crypto_alt_24h` score `0.688` n `86` status `ready` deltaP `9.048` edge `0.3922` maxDD `-29.2814`
- `market_context_high->index_1h` score `0.6803` n `45` status `ready` deltaP `11.3007` edge `0.0092` maxDD `-0.2275`
- `market_context_high->crypto_alt_1h` score `0.215` n `45` status `ready` deltaP `4.9102` edge `0.0741` maxDD `-5.7799`
- `market_context_high->fx_1h` score `0.1896` n `45` status `ready` deltaP `7.974` edge `0.0068` maxDD `-0.1854`
- `market_context_high->metal_1h` score `0.1766` n `45` status `ready` deltaP `5.3027` edge `0.011` maxDD `-0.1976`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
