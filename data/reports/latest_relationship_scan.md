# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T13:12:07.640236+00:00`
- Price records: `672`
- Market context records: `3895`
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

- `risk_on_high->unknown_4h` score `47.3554` n `72` status `ready` deltaP `5.7418` edge `6.2471` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `47.3554` n `72` status `ready` deltaP `5.7418` edge `6.2471` maxDD `-13.467`
- `risk_on_high->crypto_major_24h` score `34.8156` n `32` status `ready` deltaP `34.375` edge `2.6764` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `34.8156` n `32` status `ready` deltaP `34.375` edge `2.6764` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `27.0815` n `32` status `ready` deltaP `42.0139` edge `1.9767` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `27.0815` n `32` status `ready` deltaP `42.0139` edge `1.9767` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.7173` n `32` status `ready` deltaP `32.2917` edge `1.7763` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.7173` n `32` status `ready` deltaP `32.2917` edge `1.7763` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.2816` n `32` status `ready` deltaP `30.0347` edge `0.7399` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.2816` n `32` status `ready` deltaP `30.0347` edge `0.7399` maxDD `0.0`
- `market_context_high->unknown_4h` score `6.7017` n `209` status `ready` deltaP `-0.9169` edge `1.4062` maxDD `-35.6052`
- `market_context_high->equity_24h` score `6.4389` n `155` status `ready` deltaP `19.4333` edge `0.71` maxDD `-14.5715`
- `risk_on_high->crypto_major_4h` score `5.4288` n `72` status `ready` deltaP `19.3089` edge `0.4359` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `5.4288` n `72` status `ready` deltaP `19.3089` edge `0.4359` maxDD `-5.9781`
- `market_context_high->index_24h` score `4.9341` n `155` status `ready` deltaP `25.5186` edge `0.355` maxDD `-7.1159`
- `market_context_high->metal_24h` score `3.4905` n `155` status `ready` deltaP `23.1071` edge `0.28` maxDD `-9.1203`
- `risk_on_high->equity_4h` score `2.4734` n `72` status `ready` deltaP `24.3394` edge `0.1573` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.4734` n `72` status `ready` deltaP `24.3394` edge `0.1573` maxDD `-5.7426`
- `market_context_high->crypto_major_4h` score `2.326` n `209` status `ready` deltaP `15.4612` edge `0.2672` maxDD `-9.4488`
- `market_context_high->crypto_major_24h` score `2.179` n `155` status `ready` deltaP `5.8871` edge `0.5887` maxDD `-31.0425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
