# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T13:22:32.872274+00:00`
- Price records: `672`
- Market context records: `3896`
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

- `risk_on_high->unknown_4h` score `47.3194` n `72` status `ready` deltaP `5.5894` edge `6.2435` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `47.3194` n `72` status `ready` deltaP `5.5894` edge `6.2435` maxDD `-13.467`
- `risk_on_high->crypto_major_24h` score `34.9182` n `32` status `ready` deltaP `34.5486` edge `2.6838` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `34.9182` n `32` status `ready` deltaP `34.5486` edge `2.6838` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `27.1247` n `32` status `ready` deltaP `42.0139` edge `1.9803` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `27.1247` n `32` status `ready` deltaP `42.0139` edge `1.9803` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.8151` n `32` status `ready` deltaP `32.4653` edge `1.7833` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.8151` n `32` status `ready` deltaP `32.4653` edge `1.7833` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.3056` n `32` status `ready` deltaP `30.0347` edge `0.7419` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.3056` n `32` status `ready` deltaP `30.0347` edge `0.7419` maxDD `0.0`
- `market_context_high->unknown_4h` score `6.6657` n `209` status `ready` deltaP `-1.0693` edge `1.4026` maxDD `-35.6052`
- `market_context_high->equity_24h` score `6.4649` n `156` status `ready` deltaP `19.578` edge `0.7112` maxDD `-14.5715`
- `risk_on_high->crypto_major_4h` score `5.4674` n `72` status `ready` deltaP `19.4613` edge `0.4381` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `5.4674` n `72` status `ready` deltaP `19.4613` edge `0.4381` maxDD `-5.9781`
- `market_context_high->index_24h` score `4.9256` n `156` status `ready` deltaP `25.5475` edge `0.3541` maxDD `-7.1159`
- `market_context_high->metal_24h` score `3.4326` n `156` status `ready` deltaP `22.743` edge `0.2776` maxDD `-9.1203`
- `risk_on_high->equity_4h` score `2.4854` n `72` status `ready` deltaP `24.3394` edge `0.1583` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.4854` n `72` status `ready` deltaP `24.3394` edge `0.1583` maxDD `-5.7426`
- `market_context_high->crypto_major_4h` score `2.3646` n `209` status `ready` deltaP `15.6136` edge `0.2694` maxDD `-9.4488`
- `market_context_high->crypto_major_24h` score `2.1566` n `156` status `ready` deltaP `5.6223` edge `0.5886` maxDD `-31.0425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
