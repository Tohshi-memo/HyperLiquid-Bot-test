# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T15:22:42.959115+00:00`
- Price records: `672`
- Market context records: `4528`
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

- `risk_on_high->unknown_4h` score `186.1736` n `35` status `ready` deltaP `21.7291` edge `15.4887` maxDD `-7.5275`
- `risk_on_and_context->unknown_4h` score `186.1736` n `35` status `ready` deltaP `21.7291` edge `15.4887` maxDD `-7.5275`
- `market_context_high->unknown_1h` score `51.1209` n `182` status `ready` deltaP `6.1032` edge `4.2736` maxDD `-2.3371`
- `market_context_high->unknown_4h` score `29.6423` n `182` status `ready` deltaP `8.6522` edge `2.5691` maxDD `-7.5275`
- `risk_on_high->crypto_major_4h` score `7.2678` n `35` status `ready` deltaP `37.1994` edge `0.367` maxDD `-0.0812`
- `risk_on_and_context->crypto_major_4h` score `7.2678` n `35` status `ready` deltaP `37.1994` edge `0.367` maxDD `-0.0812`
- `risk_on_high->metal_24h` score `6.5114` n `35` status `ready` deltaP `-3.3235` edge `0.6627` maxDD `-4.834`
- `risk_on_and_context->metal_24h` score `6.5114` n `35` status `ready` deltaP `-3.3235` edge `0.6627` maxDD `-4.834`
- `risk_on_high->equity_4h` score `5.1456` n `35` status `ready` deltaP `42.2256` edge `0.1473` maxDD `0.0`
- `risk_on_and_context->equity_4h` score `5.1456` n `35` status `ready` deltaP `42.2256` edge `0.1473` maxDD `0.0`
- `risk_on_high->unknown_24h` score `5.0501` n `35` status `ready` deltaP `18.5764` edge `0.297` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `5.0501` n `35` status `ready` deltaP `18.5764` edge `0.297` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `2.3738` n `35` status `ready` deltaP `13.4277` edge `0.1649` maxDD `-1.8615`
- `risk_on_and_context->crypto_alt_4h` score `2.3738` n `35` status `ready` deltaP `13.4277` edge `0.1649` maxDD `-1.8615`
- `risk_on_high->crypto_major_1h` score `2.282` n `35` status `ready` deltaP `13.3191` edge `0.1231` maxDD `-0.7379`
- `risk_on_and_context->crypto_major_1h` score `2.282` n `35` status `ready` deltaP `13.3191` edge `0.1231` maxDD `-0.7379`
- `risk_on_high->metal_4h` score `2.2455` n `35` status `ready` deltaP `19.3336` edge `0.0918` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `2.2455` n `35` status `ready` deltaP `19.3336` edge `0.0918` maxDD `-1.3516`
- `risk_on_high->equity_1h` score `2.138` n `35` status `ready` deltaP `22.0531` edge `0.0508` maxDD `-0.2389`
- `risk_on_and_context->equity_1h` score `2.138` n `35` status `ready` deltaP `22.0531` edge `0.0508` maxDD `-0.2389`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
