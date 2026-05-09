# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-09T22:52:13.192987+00:00`
- Price records: `672`
- Market context records: `915`
- Flow alert records: `2562`
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

- `risk_on_high->crypto_major_24h` score `21.244` n `32` status `ready` deltaP `31.25` edge `1.562` maxDD `0.0`
- `risk_on_and_context->crypto_major_24h` score `21.244` n `32` status `ready` deltaP `31.25` edge `1.562` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `13.3706` n `169` status `ready` deltaP `28.2914` edge `0.959` maxDD `-1.3382`
- `risk_on_high->equity_24h` score `12.967` n `32` status `ready` deltaP `25.3472` edge `0.9116` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `12.967` n `32` status `ready` deltaP `25.3472` edge `0.9116` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `12.2488` n `32` status `ready` deltaP `4.3403` edge `0.9918` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `12.2488` n `32` status `ready` deltaP `4.3403` edge `0.9918` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `6.1936` n `169` status `ready` deltaP `4.3403` edge `0.4872` maxDD `0.0`
- `risk_on_high->index_24h` score `4.1729` n `32` status `ready` deltaP `27.9514` edge `0.1614` maxDD `0.0`
- `risk_on_and_context->index_24h` score `4.1729` n `32` status `ready` deltaP `27.9514` edge `0.1614` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.4428` n `32` status `ready` deltaP `7.6982` edge `0.2721` maxDD `-0.9217`
- `risk_on_and_context->equity_4h` score `3.4428` n `32` status `ready` deltaP `7.6982` edge `0.2721` maxDD `-0.9217`
- `risk_on_high->crypto_alt_4h` score `3.2811` n `32` status `ready` deltaP `23.3994` edge `0.1379` maxDD `-0.6377`
- `risk_on_and_context->crypto_alt_4h` score `3.2811` n `32` status `ready` deltaP `23.3994` edge `0.1379` maxDD `-0.6377`
- `risk_on_high->crypto_major_4h` score `2.8332` n `32` status `ready` deltaP `20.5793` edge `0.1361` maxDD `-0.9758`
- `risk_on_and_context->crypto_major_4h` score `2.8332` n `32` status `ready` deltaP `20.5793` edge `0.1361` maxDD `-0.9758`
- `risk_on_high->index_4h` score `2.4158` n `32` status `ready` deltaP `12.4238` edge `0.1273` maxDD `-0.038`
- `risk_on_and_context->index_4h` score `2.4158` n `32` status `ready` deltaP `12.4238` edge `0.1273` maxDD `-0.038`
- `risk_on_high->commodity_24h` score `1.1548` n `32` status `ready` deltaP `-11.9792` edge `0.3025` maxDD `-1.9668`
- `risk_on_and_context->commodity_24h` score `1.1548` n `32` status `ready` deltaP `-11.9792` edge `0.3025` maxDD `-1.9668`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
