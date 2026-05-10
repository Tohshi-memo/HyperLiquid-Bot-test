# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-10T04:07:16.047813+00:00`
- Price records: `672`
- Market context records: `938`
- Flow alert records: `2627`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1386`

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

- `risk_on_high->crypto_major_24h` score `21.9901` n `32` status `ready` deltaP `32.9861` edge `1.6126` maxDD `0.0`
- `risk_on_and_context->crypto_major_24h` score `21.9901` n `32` status `ready` deltaP `32.9861` edge `1.6126` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `14.1167` n `169` status `ready` deltaP `30.0275` edge `1.0096` maxDD `-1.3382`
- `risk_on_high->crypto_alt_24h` score `13.172` n `32` status `ready` deltaP `6.25` edge `1.056` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `13.172` n `32` status `ready` deltaP `6.25` edge `1.056` maxDD `0.0`
- `risk_on_high->equity_24h` score `12.8228` n `32` status `ready` deltaP `25.0` edge `0.9019` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `12.8228` n `32` status `ready` deltaP `25.0` edge `0.9019` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `7.1168` n `169` status `ready` deltaP `6.25` edge `0.5514` maxDD `0.0`
- `risk_on_high->index_24h` score `3.9509` n `32` status `ready` deltaP `26.7361` edge `0.151` maxDD `0.0`
- `risk_on_and_context->index_24h` score `3.9509` n `32` status `ready` deltaP `26.7361` edge `0.151` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `3.3071` n `32` status `ready` deltaP `24.0091` edge `0.136` maxDD `-0.6377`
- `risk_on_and_context->crypto_alt_4h` score `3.3071` n `32` status `ready` deltaP `24.0091` edge `0.136` maxDD `-0.6377`
- `risk_on_high->equity_4h` score `3.0885` n `32` status `ready` deltaP `4.6494` edge `0.2629` maxDD `-0.9217`
- `risk_on_and_context->equity_4h` score `3.0885` n `32` status `ready` deltaP `4.6494` edge `0.2629` maxDD `-0.9217`
- `risk_on_high->crypto_major_4h` score `2.8701` n `32` status `ready` deltaP `21.3415` edge `0.1341` maxDD `-0.9758`
- `risk_on_and_context->crypto_major_4h` score `2.8701` n `32` status `ready` deltaP `21.3415` edge `0.1341` maxDD `-0.9758`
- `risk_on_high->index_4h` score `2.1509` n `32` status `ready` deltaP `9.8323` edge `0.1225` maxDD `-0.038`
- `risk_on_and_context->index_4h` score `2.1509` n `32` status `ready` deltaP `9.8323` edge `0.1225` maxDD `-0.038`
- `risk_on_high->metal_1h` score `0.9767` n `32` status `ready` deltaP `11.4147` edge `0.0283` maxDD `-0.5074`
- `risk_on_and_context->metal_1h` score `0.9767` n `32` status `ready` deltaP `11.4147` edge `0.0283` maxDD `-0.5074`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
