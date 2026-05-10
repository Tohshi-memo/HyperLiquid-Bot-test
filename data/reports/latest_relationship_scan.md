# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-10T01:22:16.004228+00:00`
- Price records: `672`
- Market context records: `926`
- Flow alert records: `2594`
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

- `risk_on_high->crypto_major_24h` score `21.2932` n `32` status `ready` deltaP `31.25` edge `1.5661` maxDD `0.0`
- `risk_on_and_context->crypto_major_24h` score `21.2932` n `32` status `ready` deltaP `31.25` edge `1.5661` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `13.4198` n `169` status `ready` deltaP `28.2914` edge `0.9631` maxDD `-1.3382`
- `risk_on_high->equity_24h` score `12.8132` n `32` status `ready` deltaP `25.0` edge `0.9011` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `12.8132` n `32` status `ready` deltaP `25.0` edge `0.9011` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `12.3474` n `32` status `ready` deltaP `4.6875` edge `0.9977` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `12.3474` n `32` status `ready` deltaP `4.6875` edge `0.9977` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `6.2922` n `169` status `ready` deltaP `4.6875` edge `0.4931` maxDD `0.0`
- `risk_on_high->index_24h` score `4.0616` n `32` status `ready` deltaP `27.4306` edge `0.1556` maxDD `0.0`
- `risk_on_and_context->index_24h` score `4.0616` n `32` status `ready` deltaP `27.4306` edge `0.1556` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.262` n `32` status `ready` deltaP `6.1738` edge `0.2672` maxDD `-0.9217`
- `risk_on_and_context->equity_4h` score `3.262` n `32` status `ready` deltaP `6.1738` edge `0.2672` maxDD `-0.9217`
- `risk_on_high->crypto_alt_4h` score `3.1503` n `32` status `ready` deltaP `23.3994` edge `0.127` maxDD `-0.6377`
- `risk_on_and_context->crypto_alt_4h` score `3.1503` n `32` status `ready` deltaP `23.3994` edge `0.127` maxDD `-0.6377`
- `risk_on_high->crypto_major_4h` score `2.7576` n `32` status `ready` deltaP `20.5793` edge `0.1298` maxDD `-0.9758`
- `risk_on_and_context->crypto_major_4h` score `2.7576` n `32` status `ready` deltaP `20.5793` edge `0.1298` maxDD `-0.9758`
- `risk_on_high->index_4h` score `2.2639` n `32` status `ready` deltaP `10.8994` edge `0.1248` maxDD `-0.038`
- `risk_on_and_context->index_4h` score `2.2639` n `32` status `ready` deltaP `10.8994` edge `0.1248` maxDD `-0.038`
- `risk_on_high->commodity_24h` score `1.0356` n `32` status `ready` deltaP `-12.8472` edge `0.293` maxDD `-1.9668`
- `risk_on_and_context->commodity_24h` score `1.0356` n `32` status `ready` deltaP `-12.8472` edge `0.293` maxDD `-1.9668`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
