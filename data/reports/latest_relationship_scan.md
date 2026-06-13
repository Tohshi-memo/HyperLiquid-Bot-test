# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-13T20:22:29.264501+00:00`
- Price records: `672`
- Market context records: `3824`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13781`

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

- `risk_on_high->crypto_major_24h` score `32.3746` n `32` status `ready` deltaP `34.0278` edge `2.4753` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `32.3746` n `32` status `ready` deltaP `34.0278` edge `2.4753` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `26.1995` n `32` status `ready` deltaP `42.0139` edge `1.9032` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `26.1995` n `32` status `ready` deltaP `42.0139` edge `1.9032` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.5527` n `32` status `ready` deltaP `31.9444` edge `1.7649` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.5527` n `32` status `ready` deltaP `31.9444` edge `1.7649` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.3488` n `32` status `ready` deltaP `31.25` edge `0.7374` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.3488` n `32` status `ready` deltaP `31.25` edge `0.7374` maxDD `0.0`
- `market_context_high->equity_24h` score `6.684` n `145` status `ready` deltaP `17.876` edge `0.7408` maxDD `-14.5715`
- `market_context_high->index_24h` score `5.5164` n `145` status `ready` deltaP `26.4224` edge `0.3975` maxDD `-7.1159`
- `risk_on_high->crypto_major_4h` score `5.1862` n `41` status `ready` deltaP `2.8964` edge `0.5251` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `5.1862` n `41` status `ready` deltaP `2.8964` edge `0.5251` maxDD `-5.9781`
- `market_context_high->crypto_major_24h` score `4.5807` n `145` status `ready` deltaP `4.739` edge `0.7965` maxDD `-31.0425`
- `market_context_high->metal_24h` score `4.2431` n `145` status `ready` deltaP `25.6597` edge `0.3257` maxDD `-9.1203`
- `risk_on_high->equity_4h` score `2.1985` n `41` status `ready` deltaP `15.5487` edge `0.193` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.1985` n `41` status `ready` deltaP `15.5487` edge `0.193` maxDD `-5.7426`
- `market_context_high->crypto_major_4h` score `1.9657` n `191` status `ready` deltaP `10.1496` edge `0.2862` maxDD `-10.5381`
- `risk_on_high->metal_24h` score `1.4104` n `32` status `ready` deltaP `14.4097` edge `0.0476` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `1.4104` n `32` status `ready` deltaP `14.4097` edge `0.0476` maxDD `-0.7574`
- `market_context_high->equity_4h` score `1.0895` n `191` status `ready` deltaP `11.4879` edge `0.1846` maxDD `-8.2982`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
