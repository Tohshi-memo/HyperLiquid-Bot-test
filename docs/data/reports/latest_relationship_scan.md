# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-09T09:22:29.926310+00:00`
- Price records: `672`
- Market context records: `3369`
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

- `risk_on_high->crypto_major_24h` score `56.6114` n `32` status `ready` deltaP `59.5486` edge `4.3249` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `56.6114` n `32` status `ready` deltaP `59.5486` edge `4.3249` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `53.5517` n `32` status `ready` deltaP `54.6875` edge `4.1132` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `53.5517` n `32` status `ready` deltaP `54.6875` edge `4.1132` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `45.9153` n `32` status `ready` deltaP `56.7708` edge `3.4478` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `45.9153` n `32` status `ready` deltaP `56.7708` edge `3.4478` maxDD `0.0`
- `risk_on_high->index_24h` score `23.153` n `32` status `ready` deltaP `50.8681` edge `1.5903` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.153` n `32` status `ready` deltaP `50.8681` edge `1.5903` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `15.4052` n `32` status `ready` deltaP `28.0488` edge `1.209` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.4052` n `32` status `ready` deltaP `28.0488` edge `1.209` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `14.886` n `32` status `ready` deltaP `32.4653` edge `1.0502` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `14.886` n `32` status `ready` deltaP `32.4653` edge `1.0502` maxDD `-0.7574`
- `market_context_high->crypto_alt_24h` score `13.8819` n `156` status `ready` deltaP `18.7099` edge `2.5012` maxDD `-60.6961`
- `market_context_high->index_24h` score `11.8453` n `156` status `ready` deltaP `35.4835` edge `1.006` maxDD `-16.1026`
- `market_context_high->equity_24h` score `10.6231` n `156` status `ready` deltaP `30.4887` edge `2.0003` maxDD `-53.663`
- `risk_on_high->crypto_alt_4h` score `7.3512` n `32` status `ready` deltaP `8.6128` edge `0.7396` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.3512` n `32` status `ready` deltaP `8.6128` edge `0.7396` maxDD `-11.7537`
- `market_context_high->crypto_major_24h` score `4.9314` n `156` status `ready` deltaP `21.648` edge `2.1398` maxDD `-121.8173`
- `risk_on_high->equity_4h` score `3.5447` n `32` status `ready` deltaP `14.1006` edge `0.4739` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.5447` n `32` status `ready` deltaP `14.1006` edge `0.4739` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
