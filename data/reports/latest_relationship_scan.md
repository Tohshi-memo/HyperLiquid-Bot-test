# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T11:07:34.475279+00:00`
- Price records: `672`
- Market context records: `3886`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13657`

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

- `risk_on_high->unknown_4h` score `47.4055` n `72` status `ready` deltaP `5.8943` edge `6.2525` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `47.4055` n `72` status `ready` deltaP `5.8943` edge `6.2525` maxDD `-13.467`
- `risk_on_high->crypto_major_24h` score `34.4122` n `32` status `ready` deltaP `34.0278` edge `2.6451` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `34.4122` n `32` status `ready` deltaP `34.0278` edge `2.6451` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `26.9003` n `32` status `ready` deltaP `42.0139` edge `1.9616` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `26.9003` n `32` status `ready` deltaP `42.0139` edge `1.9616` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.2305` n `32` status `ready` deltaP `30.9028` edge `1.745` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.2305` n `32` status `ready` deltaP `30.9028` edge `1.745` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.1664` n `32` status `ready` deltaP `30.0347` edge `0.7303` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.1664` n `32` status `ready` deltaP `30.0347` edge `0.7303` maxDD `0.0`
- `market_context_high->unknown_4h` score `7.1044` n `205` status `ready` deltaP `-1.7073` edge `1.4631` maxDD `-35.6052`
- `market_context_high->equity_24h` score `6.3571` n `148` status `ready` deltaP `18.3653` edge `0.7103` maxDD `-14.5715`
- `risk_on_high->crypto_major_4h` score `5.4134` n `72` status `ready` deltaP `19.4613` edge `0.4336` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `5.4134` n `72` status `ready` deltaP `19.4613` edge `0.4336` maxDD `-5.9781`
- `market_context_high->index_24h` score `5.0814` n `148` status `ready` deltaP `25.305` edge `0.3687` maxDD `-7.1159`
- `market_context_high->metal_24h` score `3.5999` n `148` status `ready` deltaP `23.0199` edge `0.2897` maxDD `-9.1203`
- `risk_on_high->equity_4h` score `2.4398` n `72` status `ready` deltaP `24.3394` edge `0.1545` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.4398` n `72` status `ready` deltaP `24.3394` edge `0.1545` maxDD `-5.7426`
- `market_context_high->crypto_major_4h` score `2.2698` n `205` status `ready` deltaP `14.9695` edge `0.2658` maxDD `-9.4488`
- `market_context_high->crypto_major_24h` score `2.2537` n `148` status `ready` deltaP `5.396` edge `0.5982` maxDD `-31.0425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
