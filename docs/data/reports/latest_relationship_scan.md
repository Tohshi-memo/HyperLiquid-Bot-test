# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T13:37:31.842798+00:00`
- Price records: `672`
- Market context records: `4521`
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

- `risk_on_high->unknown_4h` score `152.5687` n `42` status `ready` deltaP `15.3673` edge `12.7307` maxDD `-7.5275`
- `risk_on_and_context->unknown_4h` score `152.5687` n `42` status `ready` deltaP `15.3673` edge `12.7307` maxDD `-7.5275`
- `market_context_high->unknown_1h` score `47.8248` n `189` status `ready` deltaP `6.1774` edge `4.0026` maxDD `-2.3371`
- `market_context_high->unknown_4h` score `27.9525` n `189` status `ready` deltaP `7.9599` edge `2.4329` maxDD `-7.5275`
- `risk_on_high->crypto_major_4h` score `6.7854` n `42` status `ready` deltaP `36.5708` edge `0.3318` maxDD `-0.1455`
- `risk_on_and_context->crypto_major_4h` score `6.7854` n `42` status `ready` deltaP `36.5708` edge `0.3318` maxDD `-0.1455`
- `risk_on_high->unknown_24h` score `5.6765` n `42` status `ready` deltaP `17.3611` edge `0.3573` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `5.6765` n `42` status `ready` deltaP `17.3611` edge `0.3573` maxDD `0.0`
- `risk_on_high->equity_4h` score `5.322` n `42` status `ready` deltaP `42.2256` edge `0.162` maxDD `0.0`
- `risk_on_and_context->equity_4h` score `5.322` n `42` status `ready` deltaP `42.2256` edge `0.162` maxDD `0.0`
- `risk_on_high->metal_24h` score `3.4142` n `42` status `ready` deltaP `-8.259` edge `0.5907` maxDD `-4.834`
- `risk_on_and_context->metal_24h` score `3.4142` n `42` status `ready` deltaP `-8.259` edge `0.5907` maxDD `-4.834`
- `risk_on_high->crypto_major_1h` score `1.8774` n `42` status `ready` deltaP `11.8905` edge `0.0989` maxDD `-0.7379`
- `risk_on_and_context->crypto_major_1h` score `1.8774` n `42` status `ready` deltaP `11.8905` edge `0.0989` maxDD `-0.7379`
- `risk_on_high->equity_1h` score `1.8206` n `42` status `ready` deltaP `18.7197` edge `0.048` maxDD `-0.3533`
- `risk_on_and_context->equity_1h` score `1.8206` n `42` status `ready` deltaP `18.7197` edge `0.048` maxDD `-0.3533`
- `risk_on_high->crypto_alt_4h` score `1.4665` n `42` status `ready` deltaP `7.847` edge `0.1265` maxDD `-1.8615`
- `risk_on_and_context->crypto_alt_4h` score `1.4665` n `42` status `ready` deltaP `7.847` edge `0.1265` maxDD `-1.8615`
- `risk_on_high->metal_4h` score `1.4547` n `42` status `ready` deltaP `17.124` edge `0.1059` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `1.4547` n `42` status `ready` deltaP `17.124` edge `0.1059` maxDD `-1.3516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
