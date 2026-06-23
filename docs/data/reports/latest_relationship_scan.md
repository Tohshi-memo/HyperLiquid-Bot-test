# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T14:52:26.732134+00:00`
- Price records: `672`
- Market context records: `4526`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9771`

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

- `risk_on_high->unknown_4h` score `175.9357` n `37` status `ready` deltaP `22.3509` edge `14.6314` maxDD `-7.5275`
- `risk_on_and_context->unknown_4h` score `175.9357` n `37` status `ready` deltaP `22.3509` edge `14.6314` maxDD `-7.5275`
- `market_context_high->unknown_1h` score `50.0747` n `184` status `ready` deltaP `5.7863` edge `4.1927` maxDD `-2.3371`
- `market_context_high->unknown_4h` score `29.2253` n `184` status `ready` deltaP `8.6758` edge `2.5342` maxDD `-7.5275`
- `risk_on_high->crypto_major_4h` score `7.198` n `37` status `ready` deltaP `37.5124` edge `0.3591` maxDD `-0.0812`
- `risk_on_and_context->crypto_major_4h` score `7.198` n `37` status `ready` deltaP `37.5124` edge `0.3591` maxDD `-0.0812`
- `risk_on_high->unknown_24h` score `5.3031` n `37` status `ready` deltaP `18.2292` edge `0.3204` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `5.3031` n `37` status `ready` deltaP `18.2292` edge `0.3204` maxDD `0.0`
- `risk_on_high->equity_4h` score `5.2128` n `37` status `ready` deltaP `42.2256` edge `0.1529` maxDD `0.0`
- `risk_on_and_context->equity_4h` score `5.2128` n `37` status `ready` deltaP `42.2256` edge `0.1529` maxDD `0.0`
- `risk_on_high->metal_24h` score `3.9287` n `37` status `ready` deltaP `-5.6401` edge `0.6392` maxDD `-4.834`
- `risk_on_and_context->metal_24h` score `3.9287` n `37` status `ready` deltaP `-5.6401` edge `0.6392` maxDD `-4.834`
- `risk_on_high->metal_4h` score `2.3884` n `37` status `ready` deltaP `18.3298` edge `0.1104` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `2.3884` n `37` status `ready` deltaP `18.3298` edge `0.1104` maxDD `-1.3516`
- `risk_on_high->crypto_major_1h` score `2.35` n `37` status `ready` deltaP `14.873` edge `0.1184` maxDD `-0.7379`
- `risk_on_and_context->crypto_major_1h` score `2.35` n `37` status `ready` deltaP `14.873` edge `0.1184` maxDD `-0.7379`
- `risk_on_high->equity_1h` score `2.2405` n `37` status `ready` deltaP `22.9892` edge `0.0531` maxDD `-0.2389`
- `risk_on_and_context->equity_1h` score `2.2405` n `37` status `ready` deltaP `22.9892` edge `0.0531` maxDD `-0.2389`
- `risk_on_high->crypto_alt_4h` score `1.7814` n `37` status `ready` deltaP `10.0281` edge `0.1382` maxDD `-1.8615`
- `risk_on_and_context->crypto_alt_4h` score `1.7814` n `37` status `ready` deltaP `10.0281` edge `0.1382` maxDD `-1.8615`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
