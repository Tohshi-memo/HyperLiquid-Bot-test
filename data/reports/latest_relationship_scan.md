# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T21:52:30.052635+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11754`

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

- `news_risk_high->unknown_24h` score `4436.3472` n `85` status `ready` deltaP `1.2153` edge `369.6875` maxDD `0.0`
- `market_context_high->unknown_1h` score `70.4359` n `45` status `ready` deltaP `10.2029` edge `5.8063` maxDD `-0.0395`
- `market_context_high->crypto_major_24h` score `49.4758` n `45` status `ready` deltaP `25.0347` edge `3.9912` maxDD `-2.4756`
- `market_context_high->equity_24h` score `27.0334` n `45` status `ready` deltaP `35.2778` edge `2.049` maxDD `-2.1786`
- `market_context_high->crypto_alt_24h` score `26.8019` n `45` status `ready` deltaP `14.9653` edge `2.1717` maxDD `-2.7051`
- `market_context_high->index_24h` score `7.412` n `45` status `ready` deltaP `30.0695` edge `0.426` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.5516` n `45` status `ready` deltaP `30.5556` edge `0.1161` maxDD `-0.2401`
- `market_context_high->index_4h` score `3.314` n `45` status `ready` deltaP `37.2357` edge `0.035` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.9268` n `45` status `ready` deltaP `18.391` edge `0.1631` maxDD `-1.3444`
- `news_risk_high->index_24h` score `2.0562` n `85` status `ready` deltaP `24.0564` edge `0.068` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `1.4139` n `85` status `ready` deltaP `30.4249` edge `0.1432` maxDD `-6.8481`
- `market_context_high->equity_1h` score `1.196` n `45` status `ready` deltaP `13.3733` edge `0.0508` maxDD `-1.5564`
- `market_context_high->crypto_major_1h` score `1.0964` n `45` status `ready` deltaP `8.503` edge `0.1081` maxDD `-4.5405`
- `market_context_high->crypto_alt_4h` score `1.0816` n `45` status `ready` deltaP `8.6111` edge `0.0995` maxDD `-3.3417`
- `market_context_high->crypto_major_4h` score `0.965` n `45` status `ready` deltaP `7.5846` edge `0.1203` maxDD `-5.2359`
- `news_risk_high->crypto_alt_24h` score `0.8832` n `85` status `ready` deltaP `8.9522` edge `0.4091` maxDD `-29.2814`
- `market_context_high->index_1h` score `0.7163` n `45` status `ready` deltaP `11.7498` edge `0.0092` maxDD `-0.2275`
- `market_context_high->metal_1h` score `0.2005` n `45` status `ready` deltaP `5.6021` edge `0.011` maxDD `-0.1976`
- `market_context_high->fx_1h` score `0.1896` n `45` status `ready` deltaP `7.974` edge `0.0068` maxDD `-0.1854`
- `market_context_high->crypto_alt_1h` score `0.1803` n `45` status `ready` deltaP `4.7605` edge `0.0722` maxDD `-5.7799`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
