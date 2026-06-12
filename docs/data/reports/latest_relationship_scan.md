# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T17:22:30.863524+00:00`
- Price records: `672`
- Market context records: `3707`
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

- `risk_on_high->crypto_major_24h` score `30.0392` n `32` status `ready` deltaP `32.4653` edge `2.2911` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `30.0392` n `32` status `ready` deltaP `32.4653` edge `2.2911` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `22.9174` n `32` status `ready` deltaP `34.7222` edge `1.6783` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `22.9174` n `32` status `ready` deltaP `34.7222` edge `1.6783` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `22.0429` n `32` status `ready` deltaP `31.5972` edge `1.6414` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `22.0429` n `32` status `ready` deltaP `31.5972` edge `1.6414` maxDD `-0.8779`
- `risk_on_high->index_24h` score `12.2163` n `32` status `ready` deltaP `34.5486` edge `0.7877` maxDD `0.0`
- `risk_on_and_context->index_24h` score `12.2163` n `32` status `ready` deltaP `34.5486` edge `0.7877` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `9.8371` n `32` status `ready` deltaP `16.7683` edge `0.8202` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `9.8371` n `32` status `ready` deltaP `16.7683` edge `0.8202` maxDD `-5.9781`
- `market_context_high->index_24h` score `4.5797` n `161` status `ready` deltaP `23.3685` edge `0.3398` maxDD `-7.1159`
- `market_context_high->equity_24h` score `3.9938` n `161` status `ready` deltaP `15.4675` edge `0.5792` maxDD `-19.6266`
- `risk_on_high->metal_24h` score `2.6403` n `32` status `ready` deltaP `20.1389` edge `0.1119` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `2.6403` n `32` status `ready` deltaP `20.1389` edge `0.1119` maxDD `-0.7574`
- `risk_on_high->equity_4h` score `1.6033` n `32` status `ready` deltaP `8.4604` edge `0.2626` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `1.6033` n `32` status `ready` deltaP `8.4604` edge `0.2626` maxDD `-5.7426`
- `risk_on_high->crypto_alt_4h` score `1.3965` n `32` status `ready` deltaP `-1.9055` edge `0.3135` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `1.3965` n `32` status `ready` deltaP `-1.9055` edge `0.3135` maxDD `-11.7537`
- `market_context_high->metal_24h` score `1.3256` n `161` status `ready` deltaP `18.4696` edge `0.2493` maxDD `-12.6241`
- `risk_on_high->crypto_major_1h` score `1.0383` n `32` status `ready` deltaP `1.9274` edge `0.2272` maxDD `-5.8885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
