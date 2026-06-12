# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T15:52:33.816792+00:00`
- Price records: `672`
- Market context records: `3700`
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

- `risk_on_high->crypto_major_24h` score `30.6529` n `32` status `ready` deltaP `33.5069` edge `2.3353` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `30.6529` n `32` status `ready` deltaP `33.5069` edge `2.3353` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `23.5875` n `32` status `ready` deltaP `35.7639` edge `1.7272` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `23.5875` n `32` status `ready` deltaP `35.7639` edge `1.7272` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `22.5234` n `32` status `ready` deltaP `32.6389` edge `1.6745` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `22.5234` n `32` status `ready` deltaP `32.6389` edge `1.6745` maxDD `-0.8779`
- `risk_on_high->index_24h` score `12.7136` n `32` status `ready` deltaP `35.5903` edge `0.8222` maxDD `0.0`
- `risk_on_and_context->index_24h` score `12.7136` n `32` status `ready` deltaP `35.5903` edge `0.8222` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `9.9833` n `32` status `ready` deltaP `17.5305` edge `0.8273` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `9.9833` n `32` status `ready` deltaP `17.5305` edge `0.8273` maxDD `-5.9781`
- `market_context_high->index_24h` score `4.0919` n `157` status `ready` deltaP `22.8514` edge `0.3026` maxDD `-7.1159`
- `risk_on_high->metal_24h` score `3.2528` n `32` status `ready` deltaP `21.1806` edge `0.156` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `3.2528` n `32` status `ready` deltaP `21.1806` edge `0.156` maxDD `-0.7574`
- `market_context_high->equity_24h` score `2.8287` n `157` status `ready` deltaP `14.7448` edge `0.5446` maxDD `-23.5737`
- `risk_on_high->equity_4h` score `1.7168` n `32` status `ready` deltaP `8.9177` edge `0.2741` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `1.7168` n `32` status `ready` deltaP `8.9177` edge `0.2741` maxDD `-5.7426`
- `risk_on_high->crypto_alt_4h` score `1.3555` n `32` status `ready` deltaP `-2.0579` edge `0.3111` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `1.3555` n `32` status `ready` deltaP `-2.0579` edge `0.3111` maxDD `-11.7537`
- `risk_on_high->crypto_major_1h` score `1.0149` n `32` status `ready` deltaP `1.9274` edge `0.2242` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `1.0149` n `32` status `ready` deltaP `1.9274` edge `0.2242` maxDD `-5.8885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
