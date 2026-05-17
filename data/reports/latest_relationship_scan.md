# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T23:14:40.794023+00:00`
- Price records: `672`
- Market context records: `1060`
- Flow alert records: `4957`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8669`

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

- `market_context_high->crypto_major_24h` score `15.0326` n `176` status `ready` deltaP `34.2254` edge `1.0709` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.887` n `176` status `ready` deltaP `11.7673` edge `0.4522` maxDD `-9.5387`
- `market_context_high->equity_24h` score `3.7334` n `176` status `ready` deltaP `11.9019` edge `0.2856` maxDD `-3.6396`
- `market_context_high->index_24h` score `2.9503` n `176` status `ready` deltaP `11.1693` edge `0.2272` maxDD `-2.1308`
- `market_context_high->metal_24h` score `2.435` n `176` status `ready` deltaP `-6.3248` edge `0.4118` maxDD `-6.3373`
- `market_context_high->fx_1h` score `-0.0936` n `178` status `ready` deltaP `5.0209` edge `0.0001` maxDD `-0.3124`
- `market_context_high->crypto_major_1h` score `-0.3035` n `178` status `ready` deltaP `7.4178` edge `0.0186` maxDD `-5.4676`
- `market_context_high->index_1h` score `-0.48` n `178` status `ready` deltaP `3.8686` edge `0.0122` maxDD `-2.2395`
- `market_context_high->equity_1h` score `-0.5156` n `178` status `ready` deltaP `0.3868` edge `0.0272` maxDD `-4.1532`
- `market_context_high->fx_4h` score `-0.7399` n `178` status `ready` deltaP `0.4179` edge `0.002` maxDD `-1.6381`
- `market_context_high->equity_4h` score `-0.788` n `178` status `ready` deltaP `2.4801` edge `0.08` maxDD `-8.3097`
- `market_context_high->commodity_1h` score `-0.8099` n `178` status `ready` deltaP `0.148` edge `0.0123` maxDD `-3.7959`
- `market_context_high->index_4h` score `-0.8182` n `178` status `ready` deltaP `0.8427` edge `0.0444` maxDD `-5.1225`
- `market_context_high->metal_1h` score `-0.8698` n `178` status `ready` deltaP `3.825` edge `-0.0319` maxDD `-5.7425`
- `market_context_high->crypto_alt_1h` score `-1.0442` n `178` status `ready` deltaP `1.6905` edge `0.0103` maxDD `-5.3538`
- `market_context_high->crypto_major_4h` score `-2.3313` n `178` status `ready` deltaP `7.6819` edge `0.064` maxDD `-17.759`
- `market_context_high->crypto_alt_4h` score `-2.5023` n `178` status `ready` deltaP `1.2965` edge `0.0423` maxDD `-13.7573`
- `market_context_high->metal_4h` score `-3.0461` n `178` status `ready` deltaP `0.2518` edge `-0.1405` maxDD `-13.8035`
- `market_context_high->fx_24h` score `-3.1326` n `176` status `ready` deltaP `4.0521` edge `-0.021` maxDD `-19.2774`
- `market_context_high->commodity_4h` score `-3.7804` n `178` status `ready` deltaP `-5.9656` edge `0.0415` maxDD `-13.0076`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
