# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T13:07:30.667772+00:00`
- Price records: `672`
- Market context records: `4519`
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

- `risk_on_high->unknown_4h` score `144.3656` n `44` status `ready` deltaP `11.9041` edge `12.0702` maxDD `-7.5275`
- `risk_on_and_context->unknown_4h` score `144.3656` n `44` status `ready` deltaP `11.9041` edge `12.0702` maxDD `-7.5275`
- `market_context_high->unknown_1h` score `46.9201` n `191` status `ready` deltaP `6.0139` edge `3.9283` maxDD `-2.3371`
- `market_context_high->unknown_4h` score `27.3716` n `191` status `ready` deltaP `7.2396` edge `2.3893` maxDD `-7.5275`
- `risk_on_high->crypto_major_4h` score `5.9615` n `44` status `ready` deltaP `32.7189` edge `0.3023` maxDD `-0.891`
- `risk_on_and_context->crypto_major_4h` score `5.9615` n `44` status `ready` deltaP `32.7189` edge `0.3023` maxDD `-0.891`
- `risk_on_high->unknown_24h` score `5.6698` n `44` status `ready` deltaP `17.1875` edge `0.3579` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `5.6698` n `44` status `ready` deltaP `17.1875` edge `0.3579` maxDD `0.0`
- `risk_on_high->equity_4h` score `5.2053` n `44` status `ready` deltaP `41.9207` edge `0.1543` maxDD `0.0`
- `risk_on_and_context->equity_4h` score `5.2053` n `44` status `ready` deltaP `41.9207` edge `0.1543` maxDD `0.0`
- `risk_on_high->metal_24h` score `3.1666` n `44` status `ready` deltaP `-9.9906` edge `0.5705` maxDD `-4.834`
- `risk_on_and_context->metal_24h` score `3.1666` n `44` status `ready` deltaP `-9.9906` edge `0.5705` maxDD `-4.834`
- `risk_on_high->metal_4h` score `1.3629` n `44` status `ready` deltaP `16.214` edge `0.1002` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `1.3629` n `44` status `ready` deltaP `16.214` edge `0.1002` maxDD `-1.3516`
- `risk_on_high->equity_1h` score `1.3315` n `44` status `ready` deltaP `15.5144` edge `0.0373` maxDD `-0.7149`
- `risk_on_and_context->equity_1h` score `1.3315` n `44` status `ready` deltaP `15.5144` edge `0.0373` maxDD `-0.7149`
- `risk_on_high->index_24h` score `1.3225` n `44` status `ready` deltaP `20.9281` edge `0.0224` maxDD `-2.4702`
- `risk_on_and_context->index_24h` score `1.3225` n `44` status `ready` deltaP `20.9281` edge `0.0224` maxDD `-2.4702`
- `risk_on_high->crypto_major_1h` score `1.1163` n `44` status `ready` deltaP `8.9684` edge `0.0696` maxDD `-1.5761`
- `risk_on_and_context->crypto_major_1h` score `1.1163` n `44` status `ready` deltaP `8.9684` edge `0.0696` maxDD `-1.5761`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
