# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T07:37:35.831432+00:00`
- Price records: `672`
- Market context records: `3871`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13656`

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

- `risk_on_high->unknown_4h` score `48.3232` n `72` status `ready` deltaP `7.4187` edge `6.36` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `48.3232` n `72` status `ready` deltaP `7.4187` edge `6.36` maxDD `-13.467`
- `risk_on_high->crypto_major_24h` score `34.2802` n `32` status `ready` deltaP `34.0278` edge `2.6341` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `34.2802` n `32` status `ready` deltaP `34.0278` edge `2.6341` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `26.8655` n `32` status `ready` deltaP `42.0139` edge `1.9587` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `26.8655` n `32` status `ready` deltaP `42.0139` edge `1.9587` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.2967` n `32` status `ready` deltaP `31.25` edge `1.7482` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.2967` n `32` status `ready` deltaP `31.25` edge `1.7482` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.1496` n `32` status `ready` deltaP `30.0347` edge `0.7289` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.1496` n `32` status `ready` deltaP `30.0347` edge `0.7289` maxDD `0.0`
- `market_context_high->unknown_4h` score `7.6506` n `206` status `ready` deltaP `-0.4292` edge `1.5246` maxDD `-35.6052`
- `market_context_high->equity_24h` score `6.555` n `139` status `ready` deltaP `16.834` edge `0.737` maxDD `-14.5715`
- `risk_on_high->crypto_major_4h` score `5.6346` n `72` status `ready` deltaP `19.7662` edge `0.45` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `5.6346` n `72` status `ready` deltaP `19.7662` edge `0.45` maxDD `-5.9781`
- `market_context_high->index_24h` score `5.4769` n `139` status `ready` deltaP `24.9987` edge `0.4037` maxDD `-7.1159`
- `market_context_high->metal_24h` score `3.3962` n `139` status `ready` deltaP `20.8034` edge `0.2875` maxDD `-9.1203`
- `risk_on_high->equity_4h` score `2.6021` n `72` status `ready` deltaP `25.5589` edge `0.1599` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.6021` n `72` status `ready` deltaP `25.5589` edge `0.1599` maxDD `-5.7426`
- `market_context_high->crypto_major_24h` score `2.3436` n `139` status `ready` deltaP `3.3399` edge `0.6194` maxDD `-31.0425`
- `market_context_high->crypto_major_4h` score `1.973` n `206` status `ready` deltaP `13.496` edge `0.2645` maxDD `-10.5381`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
