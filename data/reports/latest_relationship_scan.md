# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-10T03:07:18.859990+00:00`
- Price records: `672`
- Market context records: `934`
- Flow alert records: `2615`
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

- `risk_on_high->crypto_major_24h` score `21.6381` n `32` status `ready` deltaP `32.2917` edge `1.5879` maxDD `0.0`
- `risk_on_and_context->crypto_major_24h` score `21.6381` n `32` status `ready` deltaP `32.2917` edge `1.5879` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `13.7647` n `169` status `ready` deltaP `29.3331` edge `0.9849` maxDD `-1.3382`
- `risk_on_high->equity_24h` score `12.794` n `32` status `ready` deltaP `25.0` edge `0.8995` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `12.794` n `32` status `ready` deltaP `25.0` edge `0.8995` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `12.7708` n `32` status `ready` deltaP `5.5556` edge `1.0272` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `12.7708` n `32` status `ready` deltaP `5.5556` edge `1.0272` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `6.7156` n `169` status `ready` deltaP `5.5556` edge `0.5226` maxDD `0.0`
- `risk_on_high->index_24h` score `3.9581` n `32` status `ready` deltaP `26.7361` edge `0.1516` maxDD `0.0`
- `risk_on_and_context->index_24h` score `3.9581` n `32` status `ready` deltaP `26.7361` edge `0.1516` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `3.2261` n `32` status `ready` deltaP `23.5518` edge `0.1323` maxDD `-0.6377`
- `risk_on_and_context->crypto_alt_4h` score `3.2261` n `32` status `ready` deltaP `23.5518` edge `0.1323` maxDD `-0.6377`
- `risk_on_high->equity_4h` score `3.1649` n `32` status `ready` deltaP `5.2591` edge `0.2652` maxDD `-0.9217`
- `risk_on_and_context->equity_4h` score `3.1649` n `32` status `ready` deltaP `5.2591` edge `0.2652` maxDD `-0.9217`
- `risk_on_high->crypto_major_4h` score `2.8192` n `32` status `ready` deltaP `20.8841` edge `0.1329` maxDD `-0.9758`
- `risk_on_and_context->crypto_major_4h` score `2.8192` n `32` status `ready` deltaP `20.8841` edge `0.1329` maxDD `-0.9758`
- `risk_on_high->index_4h` score `2.1679` n `32` status `ready` deltaP `9.9848` edge `0.1229` maxDD `-0.038`
- `risk_on_and_context->index_4h` score `2.1679` n `32` status `ready` deltaP `9.9848` edge `0.1229` maxDD `-0.038`
- `risk_on_high->metal_1h` score `0.9934` n `32` status `ready` deltaP `11.5644` edge `0.0287` maxDD `-0.5074`
- `risk_on_and_context->metal_1h` score `0.9934` n `32` status `ready` deltaP `11.5644` edge `0.0287` maxDD `-0.5074`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
