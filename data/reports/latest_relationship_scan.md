# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T07:52:26.939153+00:00`
- Price records: `672`
- Market context records: `4496`
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

- `risk_on_high->unknown_4h` score `124.8015` n `49` status `ready` deltaP `4.4829` edge `10.5533` maxDD `-10.9781`
- `risk_on_and_context->unknown_4h` score `124.8015` n `49` status `ready` deltaP `4.4829` edge `10.5533` maxDD `-10.9781`
- `market_context_high->unknown_1h` score `37.0648` n `212` status `ready` deltaP `3.8216` edge `3.2138` maxDD `-9.7103`
- `market_context_high->unknown_4h` score `16.4211` n `212` status `ready` deltaP `2.3843` edge `1.899` maxDD `-36.0512`
- `risk_on_high->equity_4h` score `4.7751` n `49` status `ready` deltaP `40.5488` edge `0.1276` maxDD `0.0`
- `risk_on_and_context->equity_4h` score `4.7751` n `49` status `ready` deltaP `40.5488` edge `0.1276` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `3.2455` n `49` status `ready` deltaP `23.0712` edge `0.1832` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `3.2455` n `49` status `ready` deltaP `23.0712` edge `0.1832` maxDD `-2.6576`
- `risk_on_high->unknown_24h` score `2.4351` n `49` status `ready` deltaP `12.3228` edge `0.2011` maxDD `-5.0928`
- `risk_on_and_context->unknown_24h` score `2.4351` n `49` status `ready` deltaP `12.3228` edge `0.2011` maxDD `-5.0928`
- `risk_on_high->metal_24h` score `2.3239` n `49` status `ready` deltaP `-14.0908` edge `0.4898` maxDD `-4.834`
- `risk_on_and_context->metal_24h` score `2.3239` n `49` status `ready` deltaP `-14.0908` edge `0.4898` maxDD `-4.834`
- `risk_on_high->metal_4h` score `1.8686` n `49` status `ready` deltaP `14.6963` edge `0.0913` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `1.8686` n `49` status `ready` deltaP `14.6963` edge `0.0913` maxDD `-1.3516`
- `risk_on_high->equity_1h` score `1.304` n `49` status `ready` deltaP `15.74` edge `0.038` maxDD `-0.7415`
- `risk_on_and_context->equity_1h` score `1.304` n `49` status `ready` deltaP `15.74` edge `0.038` maxDD `-0.7415`
- `risk_on_high->fx_4h` score `0.6229` n `49` status `ready` deltaP `15.5519` edge `0.0073` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.6229` n `49` status `ready` deltaP `15.5519` edge `0.0073` maxDD `-0.3925`
- `risk_on_high->index_24h` score `0.6052` n `49` status `ready` deltaP `18.4417` edge `-0.0208` maxDD `-2.4702`
- `risk_on_and_context->index_24h` score `0.6052` n `49` status `ready` deltaP `18.4417` edge `-0.0208` maxDD `-2.4702`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
