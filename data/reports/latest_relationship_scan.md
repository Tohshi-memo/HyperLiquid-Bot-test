# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T05:22:16.479091+00:00`
- Price records: `672`
- Market context records: `1189`
- Flow alert records: `5329`
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

- `market_context_high->crypto_major_24h` score `18.4756` n `140` status `ready` deltaP `44.4792` edge `1.3563` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `7.8674` n `140` status `ready` deltaP `22.1627` edge `0.7095` maxDD `-15.1306`
- `market_context_high->metal_24h` score `4.2868` n `140` status `ready` deltaP `-3.4127` edge `0.5467` maxDD `-6.3373`
- `market_context_high->unknown_4h` score `3.6462` n `140` status `ready` deltaP `4.5906` edge `0.3949` maxDD `-6.7322`
- `market_context_high->equity_4h` score `2.8391` n `140` status `ready` deltaP `15.0479` edge `0.2026` maxDD `-3.6396`
- `market_context_high->equity_24h` score `2.3464` n `140` status `ready` deltaP `15.8283` edge `0.3227` maxDD `-14.2815`
- `market_context_high->index_24h` score `2.2697` n `140` status `ready` deltaP `15.5208` edge `0.1943` maxDD `-5.3574`
- `market_context_high->index_4h` score `1.0568` n `140` status `ready` deltaP `10.7055` edge `0.085` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.626` n `140` status `ready` deltaP `9.384` edge `0.0213` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.4705` n `140` status `ready` deltaP `4.3156` edge `0.0482` maxDD `-1.3546`
- `market_context_high->fx_1h` score `-0.0942` n `140` status `ready` deltaP `5.1283` edge `-0.0007` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `-0.1065` n `140` status `ready` deltaP `7.1341` edge `0.1309` maxDD `-8.3693`
- `market_context_high->metal_1h` score `-0.1722` n `140` status `ready` deltaP `8.5629` edge `-0.0104` maxDD `-2.2164`
- `market_context_high->commodity_24h` score `-0.1805` n `140` status `ready` deltaP `-4.37` edge `0.4869` maxDD `-33.4728`
- `market_context_high->fx_24h` score `-0.3144` n `140` status `ready` deltaP `7.1578` edge `0.0386` maxDD `-6.1301`
- `market_context_high->crypto_major_1h` score `-0.3509` n `140` status `ready` deltaP `3.3875` edge `0.009` maxDD `-4.1256`
- `market_context_high->crypto_alt_1h` score `-0.4933` n `140` status `ready` deltaP `-0.6544` edge `0.0254` maxDD `-3.4088`
- `market_context_high->fx_4h` score `-0.9312` n `140` status `ready` deltaP `-4.1071` edge `-0.0038` maxDD `-0.7232`
- `market_context_high->commodity_1h` score `-0.9803` n `140` status `ready` deltaP `-3.4217` edge `0.0026` maxDD `-2.252`
- `market_context_high->unknown_24h` score `-1.0973` n `140` status `ready` deltaP `3.2292` edge `0.16` maxDD `-10.1706`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
