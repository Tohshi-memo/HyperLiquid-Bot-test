# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T13:37:34.927729+00:00`
- Price records: `672`
- Market context records: `3690`
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

- `risk_on_high->crypto_major_24h` score `31.6143` n `32` status `ready` deltaP `35.0694` edge `2.405` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `31.6143` n `32` status `ready` deltaP `35.0694` edge `2.405` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `24.8753` n `32` status `ready` deltaP `37.3264` edge `1.8241` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `24.8753` n `32` status `ready` deltaP `37.3264` edge `1.8241` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.3744` n `32` status `ready` deltaP `34.2014` edge `1.735` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.3744` n `32` status `ready` deltaP `34.2014` edge `1.735` maxDD `-0.8779`
- `risk_on_high->index_24h` score `13.5778` n `32` status `ready` deltaP `37.1528` edge `0.8838` maxDD `0.0`
- `risk_on_and_context->index_24h` score `13.5778` n `32` status `ready` deltaP `37.1528` edge `0.8838` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `10.5413` n `32` status `ready` deltaP `18.4451` edge `0.8677` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `10.5413` n `32` status `ready` deltaP `18.4451` edge `0.8677` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `4.237` n `32` status `ready` deltaP `22.7431` edge `0.2276` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `4.237` n `32` status `ready` deltaP `22.7431` edge `0.2276` maxDD `-0.7574`
- `market_context_high->index_24h` score `3.1818` n `157` status `ready` deltaP `22.5031` edge `0.2867` maxDD `-11.3924`
- `risk_on_high->equity_4h` score `1.9477` n `32` status `ready` deltaP `8.9177` edge `0.3037` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `1.9477` n `32` status `ready` deltaP `8.9177` edge `0.3037` maxDD `-5.7426`
- `risk_on_high->crypto_alt_4h` score `1.7621` n `32` status `ready` deltaP `-1.2957` edge `0.3399` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `1.7621` n `32` status `ready` deltaP `-1.2957` edge `0.3399` maxDD `-11.7537`
- `risk_on_high->crypto_major_1h` score `1.1677` n `32` status `ready` deltaP `2.3765` edge `0.2408` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `1.1677` n `32` status `ready` deltaP `2.3765` edge `0.2408` maxDD `-5.8885`
- `risk_on_high->commodity_4h` score `0.8363` n `32` status `ready` deltaP `11.3567` edge `0.0807` maxDD `-3.6044`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
