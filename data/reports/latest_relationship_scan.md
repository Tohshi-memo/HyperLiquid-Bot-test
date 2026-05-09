# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-09T23:37:14.747750+00:00`
- Price records: `672`
- Market context records: `919`
- Flow alert records: `2572`
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

- `risk_on_high->crypto_major_24h` score `21.2632` n `32` status `ready` deltaP `31.25` edge `1.5636` maxDD `0.0`
- `risk_on_and_context->crypto_major_24h` score `21.2632` n `32` status `ready` deltaP `31.25` edge `1.5636` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `13.3898` n `169` status `ready` deltaP `28.2914` edge `0.9606` maxDD `-1.3382`
- `risk_on_high->equity_24h` score `12.9382` n `32` status `ready` deltaP `25.3472` edge `0.9092` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `12.9382` n `32` status `ready` deltaP `25.3472` edge `0.9092` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `12.2838` n `32` status `ready` deltaP `4.6875` edge `0.9924` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `12.2838` n `32` status `ready` deltaP `4.6875` edge `0.9924` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `6.2286` n `169` status `ready` deltaP `4.6875` edge `0.4878` maxDD `0.0`
- `risk_on_high->index_24h` score `4.1561` n `32` status `ready` deltaP `27.9514` edge `0.16` maxDD `0.0`
- `risk_on_and_context->index_24h` score `4.1561` n `32` status `ready` deltaP `27.9514` edge `0.16` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.3846` n `32` status `ready` deltaP `7.2409` edge `0.2703` maxDD `-0.9217`
- `risk_on_and_context->equity_4h` score `3.3846` n `32` status `ready` deltaP `7.2409` edge `0.2703` maxDD `-0.9217`
- `risk_on_high->crypto_alt_4h` score `3.2247` n `32` status `ready` deltaP `23.3994` edge `0.1332` maxDD `-0.6377`
- `risk_on_and_context->crypto_alt_4h` score `3.2247` n `32` status `ready` deltaP `23.3994` edge `0.1332` maxDD `-0.6377`
- `risk_on_high->crypto_major_4h` score `2.7996` n `32` status `ready` deltaP `20.5793` edge `0.1333` maxDD `-0.9758`
- `risk_on_and_context->crypto_major_4h` score `2.7996` n `32` status `ready` deltaP `20.5793` edge `0.1333` maxDD `-0.9758`
- `risk_on_high->index_4h` score `2.372` n `32` status `ready` deltaP `11.9665` edge `0.1267` maxDD `-0.038`
- `risk_on_and_context->index_4h` score `2.372` n `32` status `ready` deltaP `11.9665` edge `0.1267` maxDD `-0.038`
- `risk_on_high->commodity_24h` score `1.1012` n `32` status `ready` deltaP `-12.5` edge `0.2991` maxDD `-1.9668`
- `risk_on_and_context->commodity_24h` score `1.1012` n `32` status `ready` deltaP `-12.5` edge `0.2991` maxDD `-1.9668`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
