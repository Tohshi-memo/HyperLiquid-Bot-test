# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T14:07:36.162706+00:00`
- Price records: `672`
- Market context records: `3693`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12897`

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

- `risk_on_high->crypto_major_24h` score `31.3957` n `32` status `ready` deltaP `34.7222` edge `2.3891` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `31.3957` n `32` status `ready` deltaP `34.7222` edge `2.3891` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `24.5991` n `32` status `ready` deltaP `36.9792` edge `1.8034` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `24.5991` n `32` status `ready` deltaP `36.9792` edge `1.8034` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.1727` n `32` status `ready` deltaP `33.8542` edge `1.7205` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.1727` n `32` status `ready` deltaP `33.8542` edge `1.7205` maxDD `-0.8779`
- `risk_on_high->index_24h` score `13.3952` n `32` status `ready` deltaP `36.8056` edge `0.8709` maxDD `0.0`
- `risk_on_and_context->index_24h` score `13.3952` n `32` status `ready` deltaP `36.8056` edge `0.8709` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `10.4753` n `32` status `ready` deltaP `18.4451` edge `0.8622` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `10.4753` n `32` status `ready` deltaP `18.4451` edge `0.8622` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `4.0029` n `32` status `ready` deltaP `22.3958` edge `0.2104` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `4.0029` n `32` status `ready` deltaP `22.3958` edge `0.2104` maxDD `-0.7574`
- `market_context_high->index_24h` score `2.9992` n `157` status `ready` deltaP `22.1559` edge `0.2738` maxDD `-11.3924`
- `risk_on_high->equity_4h` score `1.9149` n `32` status `ready` deltaP `8.9177` edge `0.2995` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `1.9149` n `32` status `ready` deltaP `8.9177` edge `0.2995` maxDD `-5.7426`
- `risk_on_high->crypto_alt_4h` score `1.7405` n `32` status `ready` deltaP `-1.2957` edge `0.3381` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `1.7405` n `32` status `ready` deltaP `-1.2957` edge `0.3381` maxDD `-11.7537`
- `risk_on_high->crypto_major_1h` score `1.1498` n `32` status `ready` deltaP `2.2268` edge `0.2395` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `1.1498` n `32` status `ready` deltaP `2.2268` edge `0.2395` maxDD `-5.8885`
- `risk_on_high->commodity_4h` score `0.7219` n `32` status `ready` deltaP `11.0518` edge `0.0732` maxDD `-3.6044`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
