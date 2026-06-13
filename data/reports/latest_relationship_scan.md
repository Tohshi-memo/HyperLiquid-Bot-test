# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-13T21:36:06.022166+00:00`
- Price records: `672`
- Market context records: `3829`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13802`

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

- `risk_on_high->crypto_major_24h` score `32.6422` n `32` status `ready` deltaP `34.0278` edge `2.4976` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `32.6422` n `32` status `ready` deltaP `34.0278` edge `2.4976` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `26.2655` n `32` status `ready` deltaP `42.0139` edge `1.9087` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `26.2655` n `32` status `ready` deltaP `42.0139` edge `1.9087` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.5635` n `32` status `ready` deltaP `31.9444` edge `1.7658` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.5635` n `32` status `ready` deltaP `31.9444` edge `1.7658` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.3116` n `32` status `ready` deltaP `31.25` edge `0.7343` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.3116` n `32` status `ready` deltaP `31.25` edge `0.7343` maxDD `0.0`
- `market_context_high->equity_24h` score `6.693` n `140` status `ready` deltaP `17.0139` edge `0.7473` maxDD `-14.5715`
- `market_context_high->index_24h` score `5.6418` n `140` status `ready` deltaP `26.25` edge `0.4091` maxDD `-7.1159`
- `risk_on_high->crypto_major_4h` score `4.998` n `46` status `ready` deltaP `7.6684` edge `0.4776` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `4.998` n `46` status `ready` deltaP `7.6684` edge `0.4776` maxDD `-5.9781`
- `market_context_high->metal_24h` score `4.1932` n `140` status `ready` deltaP `24.9454` edge `0.3263` maxDD `-9.1203`
- `market_context_high->crypto_major_24h` score `3.9589` n `140` status `ready` deltaP `3.5814` edge `0.7524` maxDD `-31.0425`
- `risk_on_high->equity_4h` score `2.4066` n `46` status `ready` deltaP `18.465` edge `0.1909` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.4066` n `46` status `ready` deltaP `18.465` edge `0.1909` maxDD `-5.7426`
- `market_context_high->crypto_major_4h` score `1.8001` n `191` status `ready` deltaP `10.1496` edge `0.2724` maxDD `-10.5381`
- `risk_on_high->metal_24h` score `1.408` n `32` status `ready` deltaP `14.4097` edge `0.0474` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `1.408` n `32` status `ready` deltaP `14.4097` edge `0.0474` maxDD `-0.7574`
- `market_context_high->equity_4h` score `1.0691` n `191` status `ready` deltaP `11.4879` edge `0.1829` maxDD `-8.2982`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
