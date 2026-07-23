# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T13:22:34.901412+00:00`
- Price records: `672`
- Market context records: `7672`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14690`

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

- `market_context_high->index_1h` score `0.0312` n `146` status `ready` deltaP `6.0616` edge `0.0115` maxDD `-0.8324`
- `market_context_high->crypto_major_1h` score `-0.1542` n `146` status `ready` deltaP `8.1556` edge `0.0219` maxDD `-4.0162`
- `market_context_high->crypto_alt_1h` score `-0.2139` n `146` status `ready` deltaP `2.3542` edge `0.0201` maxDD `-2.7243`
- `market_context_high->fx_24h` score `-0.3208` n `145` status `ready` deltaP `9.4545` edge `0.019` maxDD `-3.0343`
- `market_context_high->commodity_1h` score `-0.4327` n `146` status `ready` deltaP `0.7774` edge `-0.0036` maxDD `-1.5641`
- `market_context_high->equity_1h` score `-0.5158` n `146` status `ready` deltaP `4.9262` edge `0.0524` maxDD `-7.7764`
- `market_context_high->metal_1h` score `-0.6395` n `146` status `ready` deltaP `1.0889` edge `0.0153` maxDD `-1.0307`
- `market_context_high->index_4h` score `-0.7404` n `146` status `ready` deltaP `7.3813` edge `0.026` maxDD `-3.2774`
- `market_context_high->fx_1h` score `-0.7663` n `146` status `ready` deltaP `-1.773` edge `-0.0021` maxDD `-0.6615`
- `market_context_high->commodity_4h` score `-0.844` n `146` status `ready` deltaP `0.5363` edge `0.0006` maxDD `-2.2943`
- `market_context_high->crypto_alt_4h` score `-0.9865` n `146` status `ready` deltaP `2.7397` edge `0.0542` maxDD `-9.5815`
- `market_context_high->crypto_major_4h` score `-1.154` n `146` status `ready` deltaP `9.4366` edge `0.0569` maxDD `-14.4206`
- `market_context_high->commodity_24h` score `-1.2306` n `145` status `ready` deltaP `7.6643` edge `0.0047` maxDD `-7.0012`
- `market_context_high->unknown_1h` score `-1.5541` n `146` status `ready` deltaP `-1.7328` edge `-0.0556` maxDD `-1.3217`
- `market_context_high->metal_4h` score `-1.7045` n `146` status `ready` deltaP `-2.7376` edge `0.0454` maxDD `-4.6535`
- `market_context_high->equity_4h` score `-1.942` n `146` status `ready` deltaP `-0.6912` edge `0.17` maxDD `-20.4824`
- `market_context_high->metal_24h` score `-2.2972` n `146` status `ready` deltaP `-3.2772` edge `0.053` maxDD `-7.3868`
- `market_context_high->fx_4h` score `-2.663` n `146` status `ready` deltaP `-7.2703` edge `-0.005` maxDD `-2.1425`
- `market_context_high->equity_24h` score `-2.8818` n `145` status `ready` deltaP `11.9248` edge `0.0416` maxDD `-34.5784`
- `market_context_high->index_24h` score `-3.6915` n `145` status `ready` deltaP `-21.7818` edge `-0.0433` maxDD `-8.114`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
