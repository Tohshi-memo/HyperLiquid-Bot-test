# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T14:37:31.591680+00:00`
- Price records: `672`
- Market context records: `3901`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11356`

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

- `risk_on_high->unknown_4h` score `47.1253` n `72` status `ready` deltaP `4.8272` edge `6.2237` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `47.1253` n `72` status `ready` deltaP `4.8272` edge `6.2237` maxDD `-13.467`
- `risk_on_high->crypto_major_24h` score `31.9906` n `34` status `ready` deltaP `29.7182` edge `2.4991` maxDD `-1.5069`
- `risk_on_and_context->crypto_major_24h` score `31.9906` n `34` status `ready` deltaP `29.7182` edge `2.4991` maxDD `-1.5069`
- `risk_on_high->equity_24h` score `25.9163` n `34` status `ready` deltaP `42.0139` edge `1.8796` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `25.9163` n `34` status `ready` deltaP `42.0139` edge `1.8796` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `20.8718` n `34` status `ready` deltaP `27.6348` edge `1.6069` maxDD `-3.1453`
- `risk_on_and_context->crypto_alt_24h` score `20.8718` n `34` status `ready` deltaP `27.6348` edge `1.6069` maxDD `-3.1453`
- `risk_on_high->index_24h` score `10.7644` n `34` status `ready` deltaP `30.0347` edge `0.6968` maxDD `0.0`
- `risk_on_and_context->index_24h` score `10.7644` n `34` status `ready` deltaP `30.0347` edge `0.6968` maxDD `0.0`
- `market_context_high->equity_24h` score `6.4739` n `161` status `ready` deltaP `20.2748` edge `0.7073` maxDD `-14.5715`
- `market_context_high->unknown_4h` score `6.4716` n `209` status `ready` deltaP `-1.8315` edge `1.3828` maxDD `-35.6052`
- `risk_on_high->crypto_major_4h` score `5.6916` n `72` status `ready` deltaP `20.2235` edge `0.4517` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `5.6916` n `72` status `ready` deltaP `20.2235` edge `0.4517` maxDD `-5.9781`
- `market_context_high->index_24h` score `4.8408` n `161` status `ready` deltaP `25.6869` edge `0.3461` maxDD `-7.1159`
- `market_context_high->metal_24h` score `3.2335` n `161` status `ready` deltaP `21.8448` edge `0.267` maxDD `-9.1203`
- `risk_on_high->equity_4h` score `2.5941` n `72` status `ready` deltaP `24.9492` edge `0.1633` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.5941` n `72` status `ready` deltaP `24.9492` edge `0.1633` maxDD `-5.7426`
- `market_context_high->crypto_major_4h` score `2.5887` n `209` status `ready` deltaP `16.3758` edge `0.283` maxDD `-9.4488`
- `market_context_high->crypto_major_24h` score `2.008` n `161` status `ready` deltaP `4.3802` edge `0.5845` maxDD `-31.0425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
