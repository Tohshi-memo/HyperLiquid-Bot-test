# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T13:52:34.498661+00:00`
- Price records: `672`
- Market context records: `3898`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11118`

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

- `risk_on_high->unknown_4h` score `47.2404` n `72` status `ready` deltaP `5.2845` edge `6.2354` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `47.2404` n `72` status `ready` deltaP `5.2845` edge `6.2354` maxDD `-13.467`
- `risk_on_high->crypto_major_24h` score `35.1236` n `32` status `ready` deltaP `34.8958` edge `2.6986` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `35.1236` n `32` status `ready` deltaP `34.8958` edge `2.6986` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `27.1967` n `32` status `ready` deltaP `42.0139` edge `1.9863` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `27.1967` n `32` status `ready` deltaP `42.0139` edge `1.9863` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.9989` n `32` status `ready` deltaP `32.8125` edge `1.7963` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.9989` n `32` status `ready` deltaP `32.8125` edge `1.7963` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.3476` n `32` status `ready` deltaP `30.0347` edge `0.7454` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.3476` n `32` status `ready` deltaP `30.0347` edge `0.7454` maxDD `0.0`
- `market_context_high->unknown_4h` score `6.5866` n `209` status `ready` deltaP `-1.3742` edge `1.3945` maxDD `-35.6052`
- `market_context_high->equity_24h` score `6.4876` n `158` status `ready` deltaP `19.862` edge `0.7112` maxDD `-14.5715`
- `risk_on_high->crypto_major_4h` score `5.559` n `72` status `ready` deltaP `19.7662` edge `0.4437` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `5.559` n `72` status `ready` deltaP `19.7662` edge `0.4437` maxDD `-5.9781`
- `market_context_high->index_24h` score `4.8966` n `158` status `ready` deltaP `25.6043` edge `0.3513` maxDD `-7.1159`
- `market_context_high->metal_24h` score `3.3815` n `158` status `ready` deltaP `22.4947` edge `0.275` maxDD `-9.1203`
- `risk_on_high->equity_4h` score `2.541` n `72` status `ready` deltaP `24.6443` edge `0.1609` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.541` n `72` status `ready` deltaP `24.6443` edge `0.1609` maxDD `-5.7426`
- `market_context_high->crypto_major_4h` score `2.4562` n `209` status `ready` deltaP `15.9185` edge `0.275` maxDD `-9.4488`
- `market_context_high->crypto_major_24h` score `2.1312` n `158` status `ready` deltaP `5.1094` edge `0.5899` maxDD `-31.0425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
