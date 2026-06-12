# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T08:37:29.055569+00:00`
- Price records: `672`
- Market context records: `3669`
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

- `risk_on_high->crypto_major_24h` score `34.1373` n `32` status `ready` deltaP `38.5417` edge `2.5921` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `34.1373` n `32` status `ready` deltaP `38.5417` edge `2.5921` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `28.8016` n `32` status `ready` deltaP `40.625` edge `2.1293` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `28.8016` n `32` status `ready` deltaP `40.625` edge `2.1293` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `25.9478` n `32` status `ready` deltaP `37.6736` edge `1.9263` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `25.9478` n `32` status `ready` deltaP `37.6736` edge `1.9263` maxDD `-0.8779`
- `risk_on_high->index_24h` score `16.1392` n `32` status `ready` deltaP `40.625` edge `1.0741` maxDD `0.0`
- `risk_on_and_context->index_24h` score `16.1392` n `32` status `ready` deltaP `40.625` edge `1.0741` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `11.563` n `32` status `ready` deltaP `20.7317` edge `0.9376` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `11.563` n `32` status `ready` deltaP `20.7317` edge `0.9376` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `7.5928` n `32` status `ready` deltaP `26.2153` edge `0.4841` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `7.5928` n `32` status `ready` deltaP `26.2153` edge `0.4841` maxDD `-0.7574`
- `market_context_high->index_24h` score `5.7432` n `157` status `ready` deltaP `25.9753` edge `0.477` maxDD `-11.3924`
- `market_context_high->equity_24h` score `4.5136` n `157` status `ready` deltaP `17.6951` edge `0.8246` maxDD `-35.3144`
- `risk_on_high->crypto_alt_4h` score `2.7262` n `32` status `ready` deltaP `0.9909` edge `0.405` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `2.7262` n `32` status `ready` deltaP `0.9909` edge `0.405` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `2.7035` n `32` status `ready` deltaP `10.747` edge `0.3884` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.7035` n `32` status `ready` deltaP `10.747` edge `0.3884` maxDD `-5.7426`
- `risk_on_high->crypto_major_1h` score `1.2901` n `32` status `ready` deltaP `3.2747` edge `0.2505` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `1.2901` n `32` status `ready` deltaP `3.2747` edge `0.2505` maxDD `-5.8885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
