# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T19:12:43.628813+00:00`
- Price records: `672`
- Market context records: `4857`
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

- `market_context_high->unknown_1h` score `13.5173` n `110` status `ready` deltaP `10.6206` edge `1.0974` maxDD `-1.674`
- `market_context_high->unknown_4h` score `10.593` n `106` status `ready` deltaP `26.5014` edge `0.7592` maxDD `-1.917`
- `market_context_high->crypto_alt_4h` score `6.0799` n `106` status `ready` deltaP `19.0779` edge `0.5147` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `5.873` n `106` status `ready` deltaP `16.1901` edge `0.5039` maxDD `-7.1265`
- `market_context_high->unknown_24h` score `5.1936` n `91` status `ready` deltaP `25.6429` edge `0.2961` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.4564` n `106` status `ready` deltaP `10.8146` edge `0.1155` maxDD `-1.9651`
- `market_context_high->equity_4h` score `0.8107` n `106` status `ready` deltaP `11.292` edge `0.1668` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.5201` n `106` status `ready` deltaP `10.806` edge `0.0409` maxDD `-0.7006`
- `market_context_high->crypto_major_1h` score `0.4453` n `110` status `ready` deltaP `6.3201` edge `0.1188` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `0.3856` n `110` status `ready` deltaP `7.7218` edge `0.1002` maxDD `-5.5126`
- `market_context_high->equity_1h` score `0.2114` n `110` status `ready` deltaP `4.0855` edge `0.0596` maxDD `-2.779`
- `market_context_high->metal_1h` score `-0.1768` n `110` status `ready` deltaP `0.694` edge `0.0307` maxDD `-1.3057`
- `market_context_high->commodity_1h` score `-0.1934` n `110` status `ready` deltaP `3.7316` edge `0.0163` maxDD `-1.278`
- `market_context_high->fx_4h` score `-0.4282` n `106` status `ready` deltaP `2.8014` edge `0.0063` maxDD `-1.0567`
- `market_context_high->index_1h` score `-0.49` n `110` status `ready` deltaP `0.3103` edge `0.0106` maxDD `-0.7054`
- `market_context_high->commodity_4h` score `-0.7924` n `106` status `ready` deltaP `6.7447` edge `0.0063` maxDD `-4.384`
- `market_context_high->fx_1h` score `-1.3322` n `110` status `ready` deltaP `-6.8672` edge `-0.0039` maxDD `-0.5734`
- `market_context_high->fx_24h` score `-1.9839` n `91` status `ready` deltaP `-7.7248` edge `-0.0128` maxDD `-2.749`
- `market_context_high->index_24h` score `-4.88` n `91` status `ready` deltaP `-9.4018` edge `-0.1544` maxDD `-24.6845`
- `market_context_high->commodity_24h` score `-5.5328` n `91` status `ready` deltaP `9.8118` edge `-0.0156` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
