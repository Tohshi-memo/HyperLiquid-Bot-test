# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-09T05:07:26.436847+00:00`
- Price records: `672`
- Market context records: `3351`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13151`

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

- `risk_on_high->crypto_major_24h` score `58.5024` n `32` status `ready` deltaP `62.5` edge `4.4628` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `58.5024` n `32` status `ready` deltaP `62.5` edge `4.4628` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `54.4573` n `32` status `ready` deltaP `57.2917` edge `4.1713` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `54.4573` n `32` status `ready` deltaP `57.2917` edge `4.1713` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `46.6041` n `32` status `ready` deltaP `56.7708` edge `3.5052` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `46.6041` n `32` status `ready` deltaP `56.7708` edge `3.5052` maxDD `0.0`
- `risk_on_high->index_24h` score `23.2358` n `32` status `ready` deltaP `50.8681` edge `1.5972` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.2358` n `32` status `ready` deltaP `50.8681` edge `1.5972` maxDD `0.0`
- `risk_on_high->metal_24h` score `15.9897` n `32` status `ready` deltaP `35.4167` edge `1.1225` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `15.9897` n `32` status `ready` deltaP `35.4167` edge `1.1225` maxDD `-0.7574`
- `risk_on_high->crypto_major_4h` score `15.9199` n `32` status `ready` deltaP `29.878` edge `1.2397` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.9199` n `32` status `ready` deltaP `29.878` edge `1.2397` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `12.4042` n `164` status `ready` deltaP `17.7338` edge `2.4562` maxDD `-70.3986`
- `market_context_high->index_24h` score `12.2509` n `164` status `ready` deltaP `36.234` edge `1.0348` maxDD `-16.1026`
- `market_context_high->equity_24h` score `10.9698` n `164` status `ready` deltaP `31.7708` edge `2.0362` maxDD `-53.663`
- `risk_on_high->crypto_alt_4h` score `7.7821` n `32` status `ready` deltaP `9.6799` edge `0.7684` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.7821` n `32` status `ready` deltaP `9.6799` edge `0.7684` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.6997` n `32` status `ready` deltaP `14.7104` edge `0.4897` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.6997` n `32` status `ready` deltaP `14.7104` edge `0.4897` maxDD `-5.7426`
- `risk_on_high->crypto_major_1h` score `2.0494` n `32` status `ready` deltaP `6.5681` edge `0.3259` maxDD `-5.8885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
