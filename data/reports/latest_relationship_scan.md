# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T05:07:27.171072+00:00`
- Price records: `672`
- Market context records: `3655`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13201`

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

- `risk_on_high->crypto_major_24h` score `35.7237` n `32` status `ready` deltaP `40.9722` edge `2.7081` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `35.7237` n `32` status `ready` deltaP `40.9722` edge `2.7081` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `31.684` n `32` status `ready` deltaP `43.0556` edge `2.3533` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `31.684` n `32` status `ready` deltaP `43.0556` edge `2.3533` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `27.8007` n `32` status `ready` deltaP `40.1042` edge `2.0645` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `27.8007` n `32` status `ready` deltaP `40.1042` edge `2.0645` maxDD `-0.8779`
- `risk_on_high->index_24h` score `17.9776` n `32` status `ready` deltaP `43.0556` edge `1.2111` maxDD `0.0`
- `risk_on_and_context->index_24h` score `17.9776` n `32` status `ready` deltaP `43.0556` edge `1.2111` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `11.2886` n `32` status `ready` deltaP `20.122` edge `0.9188` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `11.2886` n `32` status `ready` deltaP `20.122` edge `0.9188` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `9.7145` n `32` status `ready` deltaP `28.6458` edge `0.6447` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `9.7145` n `32` status `ready` deltaP `28.6458` edge `0.6447` maxDD `-0.7574`
- `market_context_high->index_24h` score `7.5816` n `157` status `ready` deltaP `28.4059` edge `0.614` maxDD `-11.3924`
- `market_context_high->equity_24h` score `7.3961` n `157` status `ready` deltaP `20.1257` edge `1.0486` maxDD `-35.3144`
- `risk_on_high->crypto_alt_4h` score `2.6032` n `32` status `ready` deltaP `0.5335` edge `0.3978` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `2.6032` n `32` status `ready` deltaP `0.5335` edge `0.3978` maxDD `-11.7537`
- `market_context_high->metal_24h` score `2.5335` n `157` status `ready` deltaP `22.9531` edge `0.567` maxDD `-21.6171`
- `risk_on_high->equity_4h` score `2.4755` n `32` status `ready` deltaP `9.5274` edge `0.3673` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.4755` n `32` status `ready` deltaP `9.5274` edge `0.3673` maxDD `-5.7426`
- `market_context_high->crypto_major_24h` score `1.7187` n `157` status `ready` deltaP `7.1545` edge `0.8022` maxDD `-49.5335`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
