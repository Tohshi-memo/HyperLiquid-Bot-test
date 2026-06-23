# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T16:07:38.568119+00:00`
- Price records: `672`
- Market context records: `4532`
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

- `risk_on_high->unknown_4h` score `132.3925` n `32` status `ready` deltaP `20.5793` edge `16.9553` maxDD `-7.5275`
- `risk_on_and_context->unknown_4h` score `132.3925` n `32` status `ready` deltaP `20.5793` edge `16.9553` maxDD `-7.5275`
- `market_context_high->unknown_1h` score `52.255` n `180` status `ready` deltaP `6.8297` edge `4.3591` maxDD `-2.3371`
- `market_context_high->unknown_4h` score `30.2635` n `179` status `ready` deltaP `8.603` edge `2.6212` maxDD `-7.5275`
- `risk_on_high->metal_24h` score `7.0863` n `32` status `ready` deltaP `-2.2569` edge `0.7035` maxDD `-4.834`
- `risk_on_and_context->metal_24h` score `7.0863` n `32` status `ready` deltaP `-2.2569` edge `0.7035` maxDD `-4.834`
- `risk_on_high->crypto_major_4h` score `6.8671` n `32` status `ready` deltaP `36.5854` edge `0.3377` maxDD `-0.0812`
- `risk_on_and_context->crypto_major_4h` score `6.8671` n `32` status `ready` deltaP `36.5854` edge `0.3377` maxDD `-0.0812`
- `risk_on_high->unknown_24h` score `5.2802` n `32` status `ready` deltaP `19.0972` edge `0.3127` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `5.2802` n `32` status `ready` deltaP `19.0972` edge `0.3127` maxDD `0.0`
- `risk_on_high->equity_4h` score `5.0568` n `32` status `ready` deltaP `42.2256` edge `0.1399` maxDD `0.0`
- `risk_on_and_context->equity_4h` score `5.0568` n `32` status `ready` deltaP `42.2256` edge `0.1399` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `4.8537` n `32` status `ready` deltaP `2.6042` edge `0.4914` maxDD `-5.0099`
- `risk_on_and_context->crypto_major_24h` score `4.8537` n `32` status `ready` deltaP `2.6042` edge `0.4914` maxDD `-5.0099`
- `risk_on_high->crypto_major_1h` score `2.0969` n `32` status `ready` deltaP `10.4042` edge `0.1271` maxDD `-0.7379`
- `risk_on_and_context->crypto_major_1h` score `2.0969` n `32` status `ready` deltaP `10.4042` edge `0.1271` maxDD `-0.7379`
- `risk_on_high->equity_1h` score `1.9809` n `32` status `ready` deltaP `20.2096` edge `0.05` maxDD `-0.2389`
- `risk_on_and_context->equity_1h` score `1.9809` n `32` status `ready` deltaP `20.2096` edge `0.05` maxDD `-0.2389`
- `risk_on_high->crypto_alt_4h` score `1.9346` n `32` status `ready` deltaP `10.5183` edge `0.1477` maxDD `-1.8615`
- `risk_on_and_context->crypto_alt_4h` score `1.9346` n `32` status `ready` deltaP `10.5183` edge `0.1477` maxDD `-1.8615`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
