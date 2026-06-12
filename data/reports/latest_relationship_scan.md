# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T13:55:57.482734+00:00`
- Price records: `672`
- Market context records: `3692`
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

- `risk_on_high->crypto_major_24h` score `31.4996` n `32` status `ready` deltaP `34.8958` edge `2.3966` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `31.4996` n `32` status `ready` deltaP `34.8958` edge `2.3966` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `24.7354` n `32` status `ready` deltaP `37.1528` edge `1.8136` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `24.7354` n `32` status `ready` deltaP `37.1528` edge `1.8136` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.2705` n `32` status `ready` deltaP `34.0278` edge `1.7275` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.2705` n `32` status `ready` deltaP `34.0278` edge `1.7275` maxDD `-0.8779`
- `risk_on_high->index_24h` score `13.4859` n `32` status `ready` deltaP `36.9792` edge `0.8773` maxDD `0.0`
- `risk_on_and_context->index_24h` score `13.4859` n `32` status `ready` deltaP `36.9792` edge `0.8773` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `10.5017` n `32` status `ready` deltaP `18.4451` edge `0.8644` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `10.5017` n `32` status `ready` deltaP `18.4451` edge `0.8644` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `4.1223` n `32` status `ready` deltaP `22.5694` edge `0.2192` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `4.1223` n `32` status `ready` deltaP `22.5694` edge `0.2192` maxDD `-0.7574`
- `market_context_high->index_24h` score `3.0899` n `157` status `ready` deltaP `22.3295` edge `0.2802` maxDD `-11.3924`
- `risk_on_high->equity_4h` score `1.9321` n `32` status `ready` deltaP `8.9177` edge `0.3017` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `1.9321` n `32` status `ready` deltaP `8.9177` edge `0.3017` maxDD `-5.7426`
- `risk_on_high->crypto_alt_4h` score `1.7477` n `32` status `ready` deltaP `-1.2957` edge `0.3387` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `1.7477` n `32` status `ready` deltaP `-1.2957` edge `0.3387` maxDD `-11.7537`
- `risk_on_high->crypto_major_1h` score `1.163` n `32` status `ready` deltaP `2.3765` edge `0.2402` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `1.163` n `32` status `ready` deltaP `2.3765` edge `0.2402` maxDD `-5.8885`
- `risk_on_high->commodity_4h` score `0.7797` n `32` status `ready` deltaP `11.2043` edge `0.077` maxDD `-3.6044`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
