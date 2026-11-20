# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-20T07:37:29.781215+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2754`

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

- `market_context_high->unknown_1h` score `11995.58` n `108` status `ready` deltaP `1.1367` edge `999.6439` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `7437.6731` n `108` status `ready` deltaP `0.0621` edge `619.8341` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `13.4553` n `102` status `ready` deltaP `30.77` edge `1.3421` maxDD `-29.4102`
- `market_context_high->crypto_alt_24h` score `7.4732` n `102` status `ready` deltaP `16.8812` edge `1.1142` maxDD `-43.6516`
- `market_context_high->crypto_major_4h` score `1.6305` n `108` status `ready` deltaP `4.8554` edge `0.3854` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `1.5752` n `108` status `ready` deltaP `6.5322` edge `0.2953` maxDD `-12.9396`
- `market_context_high->metal_4h` score `0.7189` n `108` status `ready` deltaP `18.9363` edge `0.0681` maxDD `-6.4211`
- `market_context_high->metal_1h` score `-0.0811` n `108` status `ready` deltaP `5.988` edge `0.0198` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.2397` n `108` status `ready` deltaP `3.7148` edge `0.0057` maxDD `-1.2295`
- `market_context_high->crypto_major_1h` score `-0.2882` n `108` status `ready` deltaP `4.8459` edge `0.0704` maxDD `-6.5061`
- `market_context_high->crypto_alt_1h` score `-0.6514` n `108` status `ready` deltaP `-1.1865` edge `0.0466` maxDD `-5.4428`
- `market_context_high->equity_1h` score `-1.0679` n `108` status `ready` deltaP `6.9417` edge `0.0426` maxDD `-10.8962`
- `market_context_high->fx_1h` score `-1.5953` n `108` status `ready` deltaP `-11.2497` edge `-0.002` maxDD `-0.4757`
- `market_context_high->index_4h` score `-1.7602` n `108` status `ready` deltaP `-1.4623` edge `-0.0026` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.3624` n `108` status `ready` deltaP `-9.2205` edge `-0.0272` maxDD `-3.9892`
- `market_context_high->fx_4h` score `-2.3731` n `108` status `ready` deltaP `-14.7979` edge `-0.004` maxDD `-1.794`
- `market_context_high->metal_24h` score `-4.9559` n `102` status `ready` deltaP `14.5425` edge `0.0864` maxDD `-37.7071`
- `market_context_high->fx_24h` score `-6.5498` n `102` status `ready` deltaP `-16.8913` edge `-0.0059` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-8.0178` n `108` status `ready` deltaP `-28.1955` edge `-0.1109` maxDD `-15.5426`
- `market_context_high->equity_4h` score `-9.1581` n `108` status `ready` deltaP `-6.137` edge `-0.0401` maxDD `-44.2396`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
