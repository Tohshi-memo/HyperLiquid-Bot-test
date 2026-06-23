# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T16:22:33.804878+00:00`
- Price records: `672`
- Market context records: `4533`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9932`

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

- `risk_on_high->unknown_4h` score `132.4223` n `32` status `ready` deltaP `20.7317` edge `16.9581` maxDD `-7.5275`
- `risk_on_and_context->unknown_4h` score `132.4223` n `32` status `ready` deltaP `20.7317` edge `16.9581` maxDD `-7.5275`
- `market_context_high->unknown_1h` score `52.3151` n `180` status `ready` deltaP `7.2356` edge `4.3614` maxDD `-2.3371`
- `market_context_high->unknown_4h` score `30.4575` n `178` status `ready` deltaP `8.5828` edge `2.6375` maxDD `-7.5275`
- `risk_on_high->metal_24h` score `7.1007` n `32` status `ready` deltaP `-2.2569` edge `0.7047` maxDD `-4.834`
- `risk_on_and_context->metal_24h` score `7.1007` n `32` status `ready` deltaP `-2.2569` edge `0.7047` maxDD `-4.834`
- `risk_on_high->crypto_major_4h` score `6.8876` n `32` status `ready` deltaP `36.7378` edge `0.3384` maxDD `-0.0812`
- `risk_on_and_context->crypto_major_4h` score `6.8876` n `32` status `ready` deltaP `36.7378` edge `0.3384` maxDD `-0.0812`
- `risk_on_high->unknown_24h` score `5.3157` n `32` status `ready` deltaP `19.2708` edge `0.3145` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `5.3157` n `32` status `ready` deltaP `19.2708` edge `0.3145` maxDD `0.0`
- `risk_on_high->equity_4h` score `5.0412` n `32` status `ready` deltaP `42.2256` edge `0.1386` maxDD `0.0`
- `risk_on_and_context->equity_4h` score `5.0412` n `32` status `ready` deltaP `42.2256` edge `0.1386` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `4.9185` n `32` status `ready` deltaP `2.6042` edge `0.4968` maxDD `-5.0099`
- `risk_on_and_context->crypto_major_24h` score `4.9185` n `32` status `ready` deltaP `2.6042` edge `0.4968` maxDD `-5.0099`
- `risk_on_high->crypto_major_1h` score `2.0753` n `32` status `ready` deltaP `10.2545` edge `0.1263` maxDD `-0.7379`
- `risk_on_and_context->crypto_major_1h` score `2.0753` n `32` status `ready` deltaP `10.2545` edge `0.1263` maxDD `-0.7379`
- `risk_on_high->equity_1h` score `1.9737` n `32` status `ready` deltaP `20.2096` edge `0.0494` maxDD `-0.2389`
- `risk_on_and_context->equity_1h` score `1.9737` n `32` status `ready` deltaP `20.2096` edge `0.0494` maxDD `-0.2389`
- `risk_on_high->crypto_alt_4h` score `1.9382` n `32` status `ready` deltaP `10.5183` edge `0.148` maxDD `-1.8615`
- `risk_on_and_context->crypto_alt_4h` score `1.9382` n `32` status `ready` deltaP `10.5183` edge `0.148` maxDD `-1.8615`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
