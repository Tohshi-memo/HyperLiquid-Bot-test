# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T11:52:32.190693+00:00`
- Price records: `672`
- Market context records: `3889`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13657`

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

- `risk_on_high->unknown_4h` score `47.3953` n `72` status `ready` deltaP `5.8943` edge `6.2512` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `47.3953` n `72` status `ready` deltaP `5.8943` edge `6.2512` maxDD `-13.467`
- `risk_on_high->crypto_major_24h` score `34.5106` n `32` status `ready` deltaP `34.0278` edge `2.6533` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `34.5106` n `32` status `ready` deltaP `34.0278` edge `2.6533` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `26.9447` n `32` status `ready` deltaP `42.0139` edge `1.9653` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `26.9447` n `32` status `ready` deltaP `42.0139` edge `1.9653` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.3814` n `32` status `ready` deltaP `31.4236` edge `1.7541` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.3814` n `32` status `ready` deltaP `31.4236` edge `1.7541` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.2024` n `32` status `ready` deltaP `30.0347` edge `0.7333` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.2024` n `32` status `ready` deltaP `30.0347` edge `0.7333` maxDD `0.0`
- `market_context_high->unknown_4h` score `6.9248` n `207` status `ready` deltaP `-1.2313` edge `1.4369` maxDD `-35.6052`
- `market_context_high->equity_24h` score `6.3427` n `150` status `ready` deltaP `18.6806` edge `0.707` maxDD `-14.5715`
- `risk_on_high->crypto_major_4h` score `5.3638` n `72` status `ready` deltaP `19.1565` edge `0.4315` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `5.3638` n `72` status `ready` deltaP `19.1565` edge `0.4315` maxDD `-5.9781`
- `market_context_high->index_24h` score `4.9989` n `150` status `ready` deltaP `25.368` edge `0.3614` maxDD `-7.1159`
- `market_context_high->metal_24h` score `3.571` n `150` status `ready` deltaP `23.0625` edge `0.287` maxDD `-9.1203`
- `risk_on_high->equity_4h` score `2.4398` n `72` status `ready` deltaP `24.3394` edge `0.1545` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.4398` n `72` status `ready` deltaP `24.3394` edge `0.1545` maxDD `-5.7426`
- `market_context_high->crypto_major_4h` score `2.2559` n `207` status `ready` deltaP `14.9899` edge `0.2645` maxDD `-9.4488`
- `market_context_high->crypto_major_24h` score `2.2048` n `150` status `ready` deltaP `5.8195` edge `0.5913` maxDD `-31.0425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
