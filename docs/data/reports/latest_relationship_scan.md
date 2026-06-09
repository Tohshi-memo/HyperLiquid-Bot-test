# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-09T08:24:46.421451+00:00`
- Price records: `672`
- Market context records: `3365`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13080`

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

- `risk_on_high->crypto_major_24h` score `57.0198` n `32` status `ready` deltaP `60.2431` edge `4.3543` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `57.0198` n `32` status `ready` deltaP `60.2431` edge `4.3543` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `53.7086` n `32` status `ready` deltaP `55.2083` edge `4.1228` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `53.7086` n `32` status `ready` deltaP `55.2083` edge `4.1228` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `46.0641` n `32` status `ready` deltaP `56.7708` edge `3.4602` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `46.0641` n `32` status `ready` deltaP `56.7708` edge `3.4602` maxDD `0.0`
- `risk_on_high->index_24h` score `23.1866` n `32` status `ready` deltaP `50.8681` edge `1.5931` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.1866` n `32` status `ready` deltaP `50.8681` edge `1.5931` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `15.3992` n `32` status `ready` deltaP `28.0488` edge `1.2085` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.3992` n `32` status `ready` deltaP `28.0488` edge `1.2085` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `15.1624` n `32` status `ready` deltaP `33.1597` edge `1.0686` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `15.1624` n `32` status `ready` deltaP `33.1597` edge `1.0686` maxDD `-0.7574`
- `market_context_high->crypto_alt_24h` score `13.1605` n `160` status `ready` deltaP `17.7083` edge `2.4663` maxDD `-64.7687`
- `market_context_high->index_24h` score `12.0309` n `160` status `ready` deltaP `35.8681` edge `1.0189` maxDD `-16.1026`
- `market_context_high->equity_24h` score `10.6947` n `160` status `ready` deltaP `31.1458` edge `2.0051` maxDD `-53.663`
- `risk_on_high->crypto_alt_4h` score `7.3078` n `32` status `ready` deltaP `8.4604` edge `0.737` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.3078` n `32` status `ready` deltaP `8.4604` edge `0.737` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.5589` n `32` status `ready` deltaP `14.253` edge `0.4747` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.5589` n `32` status `ready` deltaP `14.253` edge `0.4747` maxDD `-5.7426`
- `market_context_high->crypto_major_24h` score `2.9005` n `160` status `ready` deltaP `20.8681` edge `2.0662` maxDD `-135.0099`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
