# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T19:52:29.489224+00:00`
- Price records: `672`
- Market context records: `4860`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7626`

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

- `market_context_high->unknown_1h` score `13.4586` n `110` status `ready` deltaP `10.1715` edge `1.0955` maxDD `-1.674`
- `market_context_high->unknown_4h` score `10.1624` n `108` status `ready` deltaP `25.0339` edge `0.7331` maxDD `-1.917`
- `market_context_high->crypto_alt_4h` score `6.1868` n `108` status `ready` deltaP `19.6195` edge `0.52` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `5.9306` n `108` status `ready` deltaP `16.8191` edge `0.5045` maxDD `-7.1265`
- `market_context_high->unknown_24h` score `5.1598` n `91` status `ready` deltaP `25.2957` edge `0.2956` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.3735` n `108` status `ready` deltaP `10.2586` edge `0.1123` maxDD `-1.9651`
- `market_context_high->equity_4h` score `0.7986` n `108` status `ready` deltaP `11.4047` edge `0.1645` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.5104` n `108` status `ready` deltaP `10.7837` edge `0.0398` maxDD `-0.7006`
- `market_context_high->crypto_major_1h` score `0.4313` n `110` status `ready` deltaP `6.3201` edge `0.117` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `0.3794` n `110` status `ready` deltaP `7.7218` edge `0.0994` maxDD `-5.5126`
- `market_context_high->equity_1h` score `0.2059` n `110` status `ready` deltaP `4.0855` edge `0.0589` maxDD `-2.779`
- `market_context_high->metal_1h` score `-0.1581` n `110` status `ready` deltaP `0.9934` edge `0.0311` maxDD `-1.3057`
- `market_context_high->commodity_1h` score `-0.2028` n `110` status `ready` deltaP `3.5819` edge `0.0161` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.49` n `110` status `ready` deltaP `0.3103` edge `0.0106` maxDD `-0.7054`
- `market_context_high->fx_4h` score `-0.5312` n `108` status `ready` deltaP `2.1454` edge `0.006` maxDD `-1.0729`
- `market_context_high->commodity_4h` score `-0.6996` n `108` status `ready` deltaP `7.7405` edge `0.0074` maxDD `-4.384`
- `market_context_high->fx_1h` score `-1.3322` n `110` status `ready` deltaP `-6.8672` edge `-0.0039` maxDD `-0.5734`
- `market_context_high->fx_24h` score `-1.9502` n `91` status `ready` deltaP `-7.3776` edge `-0.0123` maxDD `-2.749`
- `market_context_high->index_24h` score `-4.8404` n `91` status `ready` deltaP `-8.8809` edge `-0.1528` maxDD `-24.6845`
- `market_context_high->commodity_24h` score `-5.4371` n `91` status `ready` deltaP `10.3327` edge `-0.0111` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
