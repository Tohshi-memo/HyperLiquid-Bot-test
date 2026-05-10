# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-10T02:37:12.192482+00:00`
- Price records: `672`
- Market context records: `932`
- Flow alert records: `2609`
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

- `risk_on_high->crypto_major_24h` score `21.4904` n `32` status `ready` deltaP `31.9444` edge `1.5779` maxDD `0.0`
- `risk_on_and_context->crypto_major_24h` score `21.4904` n `32` status `ready` deltaP `31.9444` edge `1.5779` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `13.6169` n `169` status `ready` deltaP `28.9858` edge `0.9749` maxDD `-1.3382`
- `risk_on_high->equity_24h` score `12.7856` n `32` status `ready` deltaP `25.0` edge `0.8988` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `12.7856` n `32` status `ready` deltaP `25.0` edge `0.8988` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `12.6051` n `32` status `ready` deltaP `5.2083` edge `1.0157` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `12.6051` n `32` status `ready` deltaP `5.2083` edge `1.0157` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `6.5499` n `169` status `ready` deltaP `5.2083` edge `0.5111` maxDD `0.0`
- `risk_on_high->index_24h` score `3.9641` n `32` status `ready` deltaP `26.7361` edge `0.1521` maxDD `0.0`
- `risk_on_and_context->index_24h` score `3.9641` n `32` status `ready` deltaP `26.7361` edge `0.1521` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `3.1923` n `32` status `ready` deltaP `23.3994` edge `0.1305` maxDD `-0.6377`
- `risk_on_and_context->crypto_alt_4h` score `3.1923` n `32` status `ready` deltaP `23.3994` edge `0.1305` maxDD `-0.6377`
- `risk_on_high->equity_4h` score `3.1831` n `32` status `ready` deltaP `5.4116` edge `0.2657` maxDD `-0.9217`
- `risk_on_and_context->equity_4h` score `3.1831` n `32` status `ready` deltaP `5.4116` edge `0.2657` maxDD `-0.9217`
- `risk_on_high->crypto_major_4h` score `2.7962` n `32` status `ready` deltaP `20.7317` edge `0.132` maxDD `-0.9758`
- `risk_on_and_context->crypto_major_4h` score `2.7962` n `32` status `ready` deltaP `20.7317` edge `0.132` maxDD `-0.9758`
- `risk_on_high->index_4h` score `2.1849` n `32` status `ready` deltaP `10.1372` edge `0.1233` maxDD `-0.038`
- `risk_on_and_context->index_4h` score `2.1849` n `32` status `ready` deltaP `10.1372` edge `0.1233` maxDD `-0.038`
- `risk_on_high->commodity_24h` score `0.9961` n `32` status `ready` deltaP `-13.0208` edge `0.2891` maxDD `-1.9668`
- `risk_on_and_context->commodity_24h` score `0.9961` n `32` status `ready` deltaP `-13.0208` edge `0.2891` maxDD `-1.9668`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
