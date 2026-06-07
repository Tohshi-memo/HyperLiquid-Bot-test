# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T00:37:20.468911+00:00`
- Price records: `672`
- Market context records: `3128`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7125`

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

- `market_context_high->commodity_24h` score `14.2677` n `105` status `ready` deltaP `47.505` edge `0.9151` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `11.6773` n `105` status `ready` deltaP `20.5506` edge `0.8849` maxDD `-1.9039`
- `market_context_high->crypto_alt_24h` score `10.9283` n `105` status `ready` deltaP `9.995` edge `2.3124` maxDD `-69.571`
- `market_context_high->index_24h` score `6.4712` n `105` status `ready` deltaP `30.8829` edge `0.8792` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.3851` n `105` status `ready` deltaP `10.9127` edge `1.3214` maxDD `-53.2236`
- `market_context_high->commodity_4h` score `3.0728` n `131` status `ready` deltaP `19.6297` edge `0.171` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `0.0772` n `143` status `ready` deltaP `3.2987` edge `0.0267` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.4152` n `143` status `ready` deltaP `5.093` edge `0.0191` maxDD `-4.5023`
- `market_context_high->fx_24h` score `-0.4844` n `105` status `ready` deltaP `5.0992` edge `-0.0016` maxDD `-0.4876`
- `market_context_high->crypto_alt_1h` score `-0.5406` n `143` status `ready` deltaP `5.093` edge `0.1097` maxDD `-14.7034`
- `market_context_high->equity_1h` score `-0.8694` n `143` status `ready` deltaP `2.5973` edge `0.0198` maxDD `-8.8863`
- `market_context_high->crypto_major_1h` score `-1.1026` n `143` status `ready` deltaP `2.0905` edge `0.071` maxDD `-15.1032`
- `market_context_high->fx_1h` score `-1.1992` n `143` status `ready` deltaP `-11.9897` edge `-0.0056` maxDD `-0.7905`
- `market_context_high->index_4h` score `-1.2286` n `131` status `ready` deltaP `11.9833` edge `0.0535` maxDD `-17.6057`
- `market_context_high->fx_4h` score `-1.4888` n `131` status `ready` deltaP `-14.4305` edge `-0.0084` maxDD `-1.2345`
- `market_context_high->metal_1h` score `-2.068` n `143` status `ready` deltaP `-4.4492` edge `-0.0033` maxDD `-7.4828`
- `market_context_high->unknown_4h` score `-2.2296` n `131` status `ready` deltaP `3.1384` edge `0.0155` maxDD `-14.7778`
- `market_context_high->unknown_1h` score `-3.0587` n `143` status `ready` deltaP `2.1524` edge `-0.0666` maxDD `-14.2111`
- `market_context_high->crypto_alt_4h` score `-3.2287` n `131` status `ready` deltaP `16.0864` edge `0.2833` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-3.5384` n `131` status `ready` deltaP `9.6932` edge `0.0123` maxDD `-36.7784`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
