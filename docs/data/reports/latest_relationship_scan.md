# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-10T04:22:16.578867+00:00`
- Price records: `672`
- Market context records: `939`
- Flow alert records: `2630`
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

- `risk_on_high->crypto_major_24h` score `22.0772` n `32` status `ready` deltaP `33.1597` edge `1.6187` maxDD `0.0`
- `risk_on_and_context->crypto_major_24h` score `22.0772` n `32` status `ready` deltaP `33.1597` edge `1.6187` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `14.2038` n `169` status `ready` deltaP `30.2011` edge `1.0157` maxDD `-1.3382`
- `risk_on_high->crypto_alt_24h` score `13.2771` n `32` status `ready` deltaP `6.4236` edge `1.0636` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `13.2771` n `32` status `ready` deltaP `6.4236` edge `1.0636` maxDD `0.0`
- `risk_on_high->equity_24h` score `12.83` n `32` status `ready` deltaP `25.0` edge `0.9025` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `12.83` n `32` status `ready` deltaP `25.0` edge `0.9025` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `7.2219` n `169` status `ready` deltaP `6.4236` edge `0.559` maxDD `0.0`
- `risk_on_high->index_24h` score `3.9509` n `32` status `ready` deltaP `26.7361` edge `0.151` maxDD `0.0`
- `risk_on_and_context->index_24h` score `3.9509` n `32` status `ready` deltaP `26.7361` edge `0.151` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `3.3373` n `32` status `ready` deltaP `24.1616` edge `0.1375` maxDD `-0.6377`
- `risk_on_and_context->crypto_alt_4h` score `3.3373` n `32` status `ready` deltaP `24.1616` edge `0.1375` maxDD `-0.6377`
- `risk_on_high->equity_4h` score `3.0679` n `32` status `ready` deltaP `4.497` edge `0.2622` maxDD `-0.9217`
- `risk_on_and_context->equity_4h` score `3.0679` n `32` status `ready` deltaP `4.497` edge `0.2622` maxDD `-0.9217`
- `risk_on_high->crypto_major_4h` score `2.8919` n `32` status `ready` deltaP `21.4939` edge `0.1349` maxDD `-0.9758`
- `risk_on_and_context->crypto_major_4h` score `2.8919` n `32` status `ready` deltaP `21.4939` edge `0.1349` maxDD `-0.9758`
- `risk_on_high->index_4h` score `2.1509` n `32` status `ready` deltaP `9.8323` edge `0.1225` maxDD `-0.038`
- `risk_on_and_context->index_4h` score `2.1509` n `32` status `ready` deltaP `9.8323` edge `0.1225` maxDD `-0.038`
- `risk_on_high->metal_1h` score `0.9743` n `32` status `ready` deltaP `11.4147` edge `0.0281` maxDD `-0.5074`
- `risk_on_and_context->metal_1h` score `0.9743` n `32` status `ready` deltaP `11.4147` edge `0.0281` maxDD `-0.5074`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
