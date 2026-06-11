# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-11T04:56:44.425686+00:00`
- Price records: `672`
- Market context records: `3552`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13202`

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

- `risk_on_high->crypto_major_24h` score `52.0214` n `32` status `ready` deltaP `57.0136` edge `3.9593` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `52.0214` n `32` status `ready` deltaP `57.0136` edge `3.9593` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `46.7561` n `32` status `ready` deltaP `56.667` edge `3.5337` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `46.7561` n `32` status `ready` deltaP `56.667` edge `3.5337` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `44.7977` n `32` status `ready` deltaP `54.2461` edge `3.3715` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `44.7977` n `32` status `ready` deltaP `54.2461` edge `3.3715` maxDD `0.0`
- `risk_on_high->index_24h` score `25.6084` n `32` status `ready` deltaP `53.8995` edge `1.7747` maxDD `0.0`
- `risk_on_and_context->index_24h` score `25.6084` n `32` status `ready` deltaP `53.8995` edge `1.7747` maxDD `0.0`
- `market_context_high->equity_24h` score `19.1537` n `156` status `ready` deltaP `31.1692` edge `2.0296` maxDD `-40.9667`
- `risk_on_high->metal_24h` score `18.6583` n `32` status `ready` deltaP `37.0342` edge `1.3341` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `18.6583` n `32` status `ready` deltaP `37.0342` edge `1.3341` maxDD `-0.7574`
- `market_context_high->crypto_major_24h` score `16.5874` n `156` status `ready` deltaP `22.3181` edge `2.0066` maxDD `-54.8486`
- `market_context_high->index_24h` score `14.2237` n `156` status `ready` deltaP `38.5149` edge `1.1502` maxDD `-15.0661`
- `risk_on_high->crypto_major_4h` score `14.1942` n `32` status `ready` deltaP `26.9817` edge `1.1152` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `14.1942` n `32` status `ready` deltaP `26.9817` edge `1.1152` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `12.6689` n `156` status `ready` deltaP `16.8433` edge `1.7477` maxDD `-56.6728`
- `market_context_high->metal_24h` score `7.6194` n `156` status `ready` deltaP `31.1047` edge `1.2235` maxDD `-25.9879`
- `risk_on_high->crypto_alt_4h` score `5.8002` n `32` status `ready` deltaP `7.2409` edge `0.6195` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `5.8002` n `32` status `ready` deltaP `7.2409` edge `0.6195` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.8844` n `32` status `ready` deltaP `16.3872` edge `0.5022` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
