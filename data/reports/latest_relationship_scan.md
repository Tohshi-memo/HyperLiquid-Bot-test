# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T19:07:28.851710+00:00`
- Price records: `672`
- Market context records: `4856`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7632`

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

- `market_context_high->unknown_1h` score `13.5149` n `110` status `ready` deltaP `10.6206` edge `1.0972` maxDD `-1.674`
- `market_context_high->unknown_4h` score `10.599` n `106` status `ready` deltaP `26.5014` edge `0.7597` maxDD `-1.917`
- `market_context_high->crypto_alt_4h` score `6.0487` n `106` status `ready` deltaP `19.0779` edge `0.5121` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `5.8418` n `106` status `ready` deltaP `16.1901` edge `0.5013` maxDD `-7.1265`
- `market_context_high->unknown_24h` score `5.1924` n `91` status `ready` deltaP `25.6429` edge `0.296` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.454` n `106` status `ready` deltaP `10.8146` edge `0.1153` maxDD `-1.9651`
- `market_context_high->equity_4h` score `0.8036` n `106` status `ready` deltaP `11.292` edge `0.1659` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.4767` n `106` status `ready` deltaP `10.015` edge `0.0406` maxDD `-0.7006`
- `market_context_high->crypto_major_1h` score `0.4492` n `110` status `ready` deltaP `6.3201` edge `0.1193` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `0.3973` n `110` status `ready` deltaP `7.8715` edge `0.1007` maxDD `-5.5126`
- `market_context_high->equity_1h` score `0.2122` n `110` status `ready` deltaP `4.0855` edge `0.0597` maxDD `-2.779`
- `market_context_high->metal_1h` score `-0.176` n `110` status `ready` deltaP `0.694` edge `0.0308` maxDD `-1.3057`
- `market_context_high->commodity_1h` score `-0.1934` n `110` status `ready` deltaP `3.7316` edge `0.0163` maxDD `-1.278`
- `market_context_high->fx_4h` score `-0.3552` n `106` status `ready` deltaP `3.5924` edge `0.0062` maxDD `-1.0547`
- `market_context_high->index_1h` score `-0.49` n `110` status `ready` deltaP `0.3103` edge `0.0106` maxDD `-0.7054`
- `market_context_high->commodity_4h` score `-0.7917` n `106` status `ready` deltaP `6.7447` edge `0.0063` maxDD `-4.3791`
- `market_context_high->fx_1h` score `-1.3442` n `110` status `ready` deltaP `-7.0169` edge `-0.0039` maxDD `-0.5734`
- `market_context_high->fx_24h` score `-1.9839` n `91` status `ready` deltaP `-7.7248` edge `-0.0128` maxDD `-2.749`
- `market_context_high->index_24h` score `-4.8792` n `91` status `ready` deltaP `-9.4018` edge `-0.1543` maxDD `-24.6845`
- `market_context_high->commodity_24h` score `-5.5328` n `91` status `ready` deltaP `9.8118` edge `-0.0156` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
