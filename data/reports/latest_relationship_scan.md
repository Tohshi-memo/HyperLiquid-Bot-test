# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T22:52:27.481922+00:00`
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

- `news_risk_high->unknown_24h` score `4212.0132` n `87` status `ready` deltaP `1.2153` edge `350.993` maxDD `0.0`
- `market_context_high->unknown_1h` score `70.5355` n `45` status `ready` deltaP `10.2029` edge `5.8146` maxDD `-0.0395`
- `market_context_high->crypto_major_24h` score `49.6418` n `45` status `ready` deltaP `25.7292` edge `4.0004` maxDD `-2.4756`
- `market_context_high->equity_24h` score `27.1034` n `45` status `ready` deltaP `35.9722` edge `2.0502` maxDD `-2.1786`
- `market_context_high->crypto_alt_24h` score `26.8775` n `45` status `ready` deltaP `14.9653` edge `2.178` maxDD `-2.7051`
- `market_context_high->index_24h` score `7.4596` n `45` status `ready` deltaP `30.5903` edge `0.4265` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.6108` n `45` status `ready` deltaP `31.25` edge `0.1164` maxDD `-0.2401`
- `market_context_high->index_4h` score `3.3006` n `45` status `ready` deltaP `37.0833` edge `0.0349` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.9366` n `45` status `ready` deltaP `18.5434` edge `0.1629` maxDD `-1.3444`
- `news_risk_high->index_24h` score `1.8799` n `87` status `ready` deltaP `22.4677` edge `0.0639` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `1.3439` n `87` status `ready` deltaP `29.3343` edge `0.1415` maxDD `-6.8481`
- `market_context_high->crypto_alt_4h` score `1.1866` n `45` status `ready` deltaP `9.0684` edge `0.1052` maxDD `-3.3417`
- `market_context_high->equity_1h` score `1.1804` n `45` status `ready` deltaP `13.2236` edge `0.0505` maxDD `-1.5564`
- `market_context_high->crypto_major_1h` score `1.1239` n `45` status `ready` deltaP `8.6527` edge `0.1094` maxDD `-4.5405`
- `market_context_high->crypto_major_4h` score `0.952` n `45` status `ready` deltaP `7.7371` edge `0.1182` maxDD `-5.2359`
- `market_context_high->index_1h` score `0.6684` n `45` status `ready` deltaP `11.151` edge `0.0092` maxDD `-0.2275`
- `news_risk_high->crypto_alt_24h` score `0.4471` n `87` status `ready` deltaP `9.1415` edge `0.3715` maxDD `-29.2814`
- `market_context_high->crypto_alt_1h` score `0.2162` n `45` status `ready` deltaP `4.9102` edge `0.0742` maxDD `-5.7799`
- `market_context_high->fx_1h` score `0.1888` n `45` status `ready` deltaP `7.974` edge `0.0067` maxDD `-0.1854`
- `market_context_high->metal_1h` score `0.1766` n `45` status `ready` deltaP `5.3027` edge `0.011` maxDD `-0.1976`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
