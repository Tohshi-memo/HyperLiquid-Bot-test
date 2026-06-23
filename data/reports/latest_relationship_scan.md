# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T15:42:05.116850+00:00`
- Price records: `672`
- Market context records: `4530`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9771`

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

- `risk_on_high->unknown_4h` score `191.7339` n `34` status `ready` deltaP `21.3773` edge `15.9544` maxDD `-7.5275`
- `risk_on_and_context->unknown_4h` score `191.7339` n `34` status `ready` deltaP `21.3773` edge `15.9544` maxDD `-7.5275`
- `market_context_high->unknown_1h` score `51.7014` n `181` status `ready` deltaP `6.4645` edge `4.3154` maxDD `-2.3371`
- `market_context_high->unknown_4h` score `29.8571` n `181` status `ready` deltaP `8.6377` edge `2.5871` maxDD `-7.5275`
- `risk_on_high->crypto_major_4h` score `7.0971` n `34` status `ready` deltaP `37.0158` edge `0.354` maxDD `-0.0812`
- `risk_on_and_context->crypto_major_4h` score `7.0971` n `34` status `ready` deltaP `37.0158` edge `0.354` maxDD `-0.0812`
- `risk_on_high->metal_24h` score `6.8355` n `34` status `ready` deltaP `-2.063` edge `0.6813` maxDD `-4.834`
- `risk_on_and_context->metal_24h` score `6.8355` n `34` status `ready` deltaP `-2.063` edge `0.6813` maxDD `-4.834`
- `risk_on_high->equity_4h` score `5.0892` n `34` status `ready` deltaP `42.2256` edge `0.1426` maxDD `0.0`
- `risk_on_and_context->equity_4h` score `5.0892` n `34` status `ready` deltaP `42.2256` edge `0.1426` maxDD `0.0`
- `risk_on_high->unknown_24h` score `5.0724` n `34` status `ready` deltaP `18.75` edge `0.2977` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `5.0724` n `34` status `ready` deltaP `18.75` edge `0.2977` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `3.3823` n `34` status `ready` deltaP `-0.5208` edge `0.4109` maxDD `-6.0455`
- `risk_on_and_context->crypto_major_24h` score `3.3823` n `34` status `ready` deltaP `-0.5208` edge `0.4109` maxDD `-6.0455`
- `risk_on_high->crypto_alt_4h` score `2.2645` n `34` status `ready` deltaP `12.5718` edge `0.1615` maxDD `-1.8615`
- `risk_on_and_context->crypto_alt_4h` score `2.2645` n `34` status `ready` deltaP `12.5718` edge `0.1615` maxDD `-1.8615`
- `risk_on_high->crypto_major_1h` score `2.2337` n `34` status `ready` deltaP `12.4604` edge `0.1248` maxDD `-0.7379`
- `risk_on_and_context->crypto_major_1h` score `2.2337` n `34` status `ready` deltaP `12.4604` edge `0.1248` maxDD `-0.7379`
- `risk_on_high->equity_1h` score `2.0854` n `34` status `ready` deltaP `21.5305` edge `0.0499` maxDD `-0.2389`
- `risk_on_and_context->equity_1h` score `2.0854` n `34` status `ready` deltaP `21.5305` edge `0.0499` maxDD `-0.2389`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
