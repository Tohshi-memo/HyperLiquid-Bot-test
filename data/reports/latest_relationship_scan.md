# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T03:52:16.004656+00:00`
- Price records: `672`
- Market context records: `1183`
- Flow alert records: `5310`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8768`

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

- `market_context_high->crypto_major_24h` score `18.8869` n `144` status `ready` deltaP `44.4445` edge `1.3908` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `8.465` n `144` status `ready` deltaP `22.2223` edge `0.7589` maxDD `-15.1306`
- `market_context_high->metal_24h` score `4.5548` n `144` status `ready` deltaP `-2.7778` edge `0.5648` maxDD `-6.3373`
- `market_context_high->equity_24h` score `3.0338` n `144` status `ready` deltaP `15.7986` edge `0.3642` maxDD `-13.3364`
- `market_context_high->index_24h` score `3.0151` n `144` status `ready` deltaP `15.4514` edge `0.2467` maxDD `-4.8763`
- `market_context_high->equity_4h` score `2.7391` n `145` status `ready` deltaP `14.5028` edge `0.1979` maxDD `-3.6396`
- `market_context_high->unknown_4h` score `2.1346` n `145` status `ready` deltaP `5.4048` edge `0.2635` maxDD `-6.7322`
- `market_context_high->index_4h` score `1.149` n `145` status `ready` deltaP `10.3574` edge `0.095` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.7118` n `145` status `ready` deltaP `9.7212` edge `0.0262` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.3273` n `145` status `ready` deltaP `3.0064` edge `0.045` maxDD `-1.3546`
- `market_context_high->fx_1h` score `-0.0176` n `145` status `ready` deltaP `6.5569` edge `-0.0004` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `-0.1169` n `145` status `ready` deltaP `7.2341` edge `0.1289` maxDD `-8.3693`
- `market_context_high->crypto_major_1h` score `-0.2314` n `145` status `ready` deltaP `4.5148` edge `0.0168` maxDD `-4.1256`
- `market_context_high->metal_1h` score `-0.2544` n `145` status `ready` deltaP `7.5511` edge `-0.0105` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.4136` n `145` status `ready` deltaP `0.2323` edge `0.0297` maxDD `-3.4088`
- `market_context_high->commodity_1h` score `-0.7747` n `145` status `ready` deltaP `-4.1834` edge `-0.0032` maxDD `-2.7917`
- `market_context_high->fx_24h` score `-0.9977` n `144` status `ready` deltaP `5.3819` edge `0.0216` maxDD `-9.1647`
- `market_context_high->fx_4h` score `-1.0576` n `145` status `ready` deltaP `-4.9906` edge `-0.0065` maxDD `-1.3319`
- `market_context_high->crypto_alt_4h` score `-1.4035` n `145` status `ready` deltaP `2.8427` edge `0.0976` maxDD `-16.7194`
- `market_context_high->metal_4h` score `-1.8835` n `145` status `ready` deltaP `4.5342` edge `-0.0763` maxDD `-9.2991`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
