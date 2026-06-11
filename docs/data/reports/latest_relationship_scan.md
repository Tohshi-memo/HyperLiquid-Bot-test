# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-11T19:22:36.529732+00:00`
- Price records: `672`
- Market context records: `3613`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13162`

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

- `risk_on_high->crypto_major_24h` score `43.7894` n `32` status `ready` deltaP `47.7431` edge `3.3351` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `43.7894` n `32` status `ready` deltaP `47.7431` edge `3.3351` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `40.7733` n `32` status `ready` deltaP `49.8264` edge `3.0656` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `40.7733` n `32` status `ready` deltaP `49.8264` edge `3.0656` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `36.6799` n `32` status `ready` deltaP `46.875` edge `2.7593` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `36.6799` n `32` status `ready` deltaP `46.875` edge `2.7593` maxDD `-0.8779`
- `risk_on_high->index_24h` score `23.7417` n `32` status `ready` deltaP `49.8264` edge `1.6463` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.7417` n `32` status `ready` deltaP `49.8264` edge `1.6463` maxDD `0.0`
- `risk_on_high->metal_24h` score `16.6233` n `32` status `ready` deltaP `35.4167` edge `1.1753` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `16.6233` n `32` status `ready` deltaP `35.4167` edge `1.1753` maxDD `-0.7574`
- `market_context_high->equity_24h` score `15.0433` n `158` status `ready` deltaP `26.4087` edge `1.7188` maxDD `-40.9667`
- `risk_on_high->crypto_major_4h` score `12.9339` n `32` status `ready` deltaP `23.9329` edge `1.0305` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `12.9339` n `32` status `ready` deltaP `23.9329` edge `1.0305` maxDD `-5.9781`
- `market_context_high->index_24h` score `12.3918` n `158` status `ready` deltaP `34.6365` edge `1.0234` maxDD `-15.0661`
- `market_context_high->crypto_major_24h` score `8.4668` n `158` status `ready` deltaP `13.5263` edge `1.3885` maxDD `-54.8486`
- `market_context_high->metal_24h` score `6.3296` n `158` status `ready` deltaP `29.3249` edge `1.07` maxDD `-25.9879`
- `risk_on_high->crypto_alt_4h` score `4.5943` n `32` status `ready` deltaP `4.497` edge `0.5373` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `4.5943` n `32` status `ready` deltaP `4.497` edge `0.5373` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.3916` n `32` status `ready` deltaP `13.7957` edge `0.4563` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.3916` n `32` status `ready` deltaP `13.7957` edge `0.4563` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
