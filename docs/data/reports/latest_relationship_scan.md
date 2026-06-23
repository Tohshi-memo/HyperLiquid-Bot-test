# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T15:07:36.191887+00:00`
- Price records: `672`
- Market context records: `4527`
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

- `risk_on_high->unknown_4h` score `180.8955` n `36` status `ready` deltaP `22.0528` edge `15.0467` maxDD `-7.5275`
- `risk_on_and_context->unknown_4h` score `180.8955` n `36` status `ready` deltaP `22.0528` edge `15.0467` maxDD `-7.5275`
- `market_context_high->unknown_1h` score `50.5515` n `183` status `ready` deltaP `5.7459` edge `4.2327` maxDD `-2.3371`
- `market_context_high->unknown_4h` score `29.4285` n `183` status `ready` deltaP `8.6649` edge `2.5512` maxDD `-7.5275`
- `risk_on_high->crypto_major_4h` score `7.227` n `36` status `ready` deltaP `37.3645` edge `0.3625` maxDD `-0.0812`
- `risk_on_and_context->crypto_major_4h` score `7.227` n `36` status `ready` deltaP `37.3645` edge `0.3625` maxDD `-0.0812`
- `risk_on_high->metal_24h` score `6.289` n `36` status `ready` deltaP `-4.5139` edge `0.6521` maxDD `-4.834`
- `risk_on_and_context->metal_24h` score `6.289` n `36` status `ready` deltaP `-4.5139` edge `0.6521` maxDD `-4.834`
- `risk_on_high->equity_4h` score `5.178` n `36` status `ready` deltaP `42.2256` edge `0.15` maxDD `0.0`
- `risk_on_and_context->equity_4h` score `5.178` n `36` status `ready` deltaP `42.2256` edge `0.15` maxDD `0.0`
- `risk_on_high->unknown_24h` score `5.1706` n `36` status `ready` deltaP `18.4028` edge `0.3082` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `5.1706` n `36` status `ready` deltaP `18.4028` edge `0.3082` maxDD `0.0`
- `risk_on_high->metal_4h` score `2.5672` n `36` status `ready` deltaP `20.0542` edge `0.1138` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `2.5672` n `36` status `ready` deltaP `20.0542` edge `0.1138` maxDD `-1.3516`
- `risk_on_high->crypto_major_1h` score `2.3259` n `36` status `ready` deltaP `14.1218` edge `0.1214` maxDD `-0.7379`
- `risk_on_and_context->crypto_major_1h` score `2.3259` n `36` status `ready` deltaP `14.1218` edge `0.1214` maxDD `-0.7379`
- `risk_on_high->equity_1h` score `2.202` n `36` status `ready` deltaP `22.5383` edge `0.0529` maxDD `-0.2389`
- `risk_on_and_context->equity_1h` score `2.202` n `36` status `ready` deltaP `22.5383` edge `0.0529` maxDD `-0.2389`
- `risk_on_high->crypto_alt_4h` score `2.0586` n `36` status `ready` deltaP `11.6023` edge `0.1508` maxDD `-1.8615`
- `risk_on_and_context->crypto_alt_4h` score `2.0586` n `36` status `ready` deltaP `11.6023` edge `0.1508` maxDD `-1.8615`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
