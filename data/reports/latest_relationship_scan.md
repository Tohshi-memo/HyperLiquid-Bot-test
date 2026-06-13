# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-13T01:22:31.939899+00:00`
- Price records: `672`
- Market context records: `3741`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13153`

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

- `risk_on_high->crypto_major_24h` score `28.594` n `32` status `ready` deltaP `29.3403` edge `2.1915` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `28.594` n `32` status `ready` deltaP `29.3403` edge `2.1915` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `22.2771` n `32` status `ready` deltaP `33.3333` edge `1.6342` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `22.2771` n `32` status `ready` deltaP `33.3333` edge `1.6342` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `21.1052` n `32` status `ready` deltaP `30.5556` edge `1.5702` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `21.1052` n `32` status `ready` deltaP `30.5556` edge `1.5702` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.4515` n `32` status `ready` deltaP `31.4236` edge `0.7448` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.4515` n `32` status `ready` deltaP `31.4236` edge `0.7448` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `10.1007` n `32` status `ready` deltaP `18.2927` edge `0.832` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `10.1007` n `32` status `ready` deltaP `18.2927` edge `0.832` maxDD `-5.9781`
- `market_context_high->equity_24h` score `6.421` n `157` status `ready` deltaP `18.0467` edge `0.65` maxDD `-12.8184`
- `market_context_high->index_24h` score `5.4626` n `157` status `ready` deltaP `26.965` edge `0.3894` maxDD `-7.1159`
- `market_context_high->crypto_major_24h` score `4.6106` n `157` status `ready` deltaP `6.9876` edge `0.784` maxDD `-31.0425`
- `market_context_high->metal_24h` score `4.59` n `157` status `ready` deltaP `27.5356` edge `0.3421` maxDD `-9.1203`
- `market_context_high->crypto_major_4h` score `1.8394` n `168` status `ready` deltaP `9.0665` edge `0.2829` maxDD `-10.5381`
- `risk_on_high->metal_24h` score `1.4273` n `32` status `ready` deltaP `14.7569` edge `0.0467` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `1.4273` n `32` status `ready` deltaP `14.7569` edge `0.0467` maxDD `-0.7574`
- `risk_on_high->crypto_alt_4h` score `1.3993` n `32` status `ready` deltaP `-0.686` edge `0.3056` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `1.3993` n `32` status `ready` deltaP `-0.686` edge `0.3056` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `1.2343` n `32` status `ready` deltaP `7.3933` edge `0.2224` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
