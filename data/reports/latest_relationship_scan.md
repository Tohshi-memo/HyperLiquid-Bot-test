# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-09T20:37:21.150540+00:00`
- Price records: `672`
- Market context records: `904`
- Flow alert records: `2534`
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

- `risk_on_high->crypto_major_24h` score `21.315` n `32` status `ready` deltaP `31.5972` edge `1.5656` maxDD `0.0`
- `risk_on_and_context->crypto_major_24h` score `21.315` n `32` status `ready` deltaP `31.5972` edge `1.5656` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `13.4416` n `169` status `ready` deltaP `28.6386` edge `0.9626` maxDD `-1.3382`
- `risk_on_high->equity_24h` score `13.0618` n `32` status `ready` deltaP `25.3472` edge `0.9195` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `13.0618` n `32` status `ready` deltaP `25.3472` edge `0.9195` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `12.4131` n `32` status `ready` deltaP `5.2083` edge `0.9997` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `12.4131` n `32` status `ready` deltaP `5.2083` edge `0.9997` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `6.3579` n `169` status `ready` deltaP `5.2083` edge `0.4951` maxDD `0.0`
- `risk_on_high->index_24h` score `4.2137` n `32` status `ready` deltaP `27.9514` edge `0.1648` maxDD `0.0`
- `risk_on_and_context->index_24h` score `4.2137` n `32` status `ready` deltaP `27.9514` edge `0.1648` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.5518` n `32` status `ready` deltaP `8.4604` edge `0.2761` maxDD `-0.9217`
- `risk_on_and_context->equity_4h` score `3.5518` n `32` status `ready` deltaP `8.4604` edge `0.2761` maxDD `-0.9217`
- `risk_on_high->crypto_alt_4h` score `3.4745` n `32` status `ready` deltaP `24.4665` edge `0.1469` maxDD `-0.6377`
- `risk_on_and_context->crypto_alt_4h` score `3.4745` n `32` status `ready` deltaP `24.4665` edge `0.1469` maxDD `-0.6377`
- `risk_on_high->crypto_major_4h` score `2.9723` n `32` status `ready` deltaP `21.4939` edge `0.1416` maxDD `-0.9758`
- `risk_on_and_context->crypto_major_4h` score `2.9723` n `32` status `ready` deltaP `21.4939` edge `0.1416` maxDD `-0.9758`
- `risk_on_high->index_4h` score `2.5156` n `32` status `ready` deltaP `13.4909` edge `0.1285` maxDD `-0.038`
- `risk_on_and_context->index_4h` score `2.5156` n `32` status `ready` deltaP `13.4909` edge `0.1285` maxDD `-0.038`
- `risk_on_high->commodity_24h` score `1.3183` n `32` status `ready` deltaP `-10.5903` edge `0.3142` maxDD `-1.9668`
- `risk_on_and_context->commodity_24h` score `1.3183` n `32` status `ready` deltaP `-10.5903` edge `0.3142` maxDD `-1.9668`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
