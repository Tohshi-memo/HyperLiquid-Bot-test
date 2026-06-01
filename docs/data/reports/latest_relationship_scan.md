# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T07:21:39.185433+00:00`
- Price records: `672`
- Market context records: `2540`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9252`

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

- `market_context_high->crypto_alt_4h` score `5.1704` n `155` status `ready` deltaP `23.6654` edge `0.541` maxDD `-15.4319`
- `market_context_high->crypto_major_24h` score `5.1128` n `116` status `ready` deltaP `13.2663` edge `0.6334` maxDD `-18.662`
- `market_context_high->unknown_24h` score `5.0034` n `116` status `ready` deltaP `19.3307` edge `0.3209` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `3.6067` n `155` status `ready` deltaP `16.9444` edge `0.3686` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `1.8864` n `155` status `ready` deltaP `10.9608` edge `0.1891` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `1.0963` n `155` status `ready` deltaP `9.4939` edge `0.1468` maxDD `-6.1656`
- `market_context_high->equity_24h` score `1.0858` n `116` status `ready` deltaP `20.546` edge `0.0448` maxDD `-4.3031`
- `market_context_high->crypto_major_1h` score `0.613` n `155` status `ready` deltaP `7.9042` edge `0.1178` maxDD `-4.2199`
- `market_context_high->index_24h` score `0.2928` n `116` status `ready` deltaP `4.5259` edge `0.0923` maxDD `-2.5127`
- `market_context_high->crypto_alt_24h` score `0.0164` n `116` status `ready` deltaP `-0.1556` edge `0.6809` maxDD `-42.2204`
- `market_context_high->unknown_1h` score `-0.058` n `155` status `ready` deltaP `3.9869` edge `0.0376` maxDD `-2.8543`
- `market_context_high->index_4h` score `-0.123` n `155` status `ready` deltaP `6.2844` edge `0.032` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.2924` n `155` status `ready` deltaP `2.6753` edge `0.0072` maxDD `-1.2855`
- `market_context_high->commodity_1h` score `-0.3342` n `155` status `ready` deltaP `4.379` edge `0.0158` maxDD `-4.3601`
- `market_context_high->metal_1h` score `-0.4301` n `155` status `ready` deltaP `1.3705` edge `0.0105` maxDD `-2.9823`
- `market_context_high->fx_1h` score `-0.4538` n `155` status `ready` deltaP `1.6593` edge `0.0046` maxDD `-0.278`
- `market_context_high->metal_4h` score `-0.8394` n `155` status `ready` deltaP `3.57` edge `0.045` maxDD `-4.7664`
- `market_context_high->equity_1h` score `-0.8514` n `155` status `ready` deltaP `-0.479` edge `0.0161` maxDD `-2.7085`
- `market_context_high->fx_24h` score `-0.8555` n `116` status `ready` deltaP `3.125` edge `0.0034` maxDD `-2.3798`
- `market_context_high->fx_4h` score `-0.8558` n `155` status `ready` deltaP `0.3226` edge `0.0125` maxDD `-0.8774`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
