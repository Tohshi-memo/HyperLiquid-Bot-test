# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T17:37:28.162775+00:00`
- Price records: `672`
- Market context records: `7691`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14676`

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

- `market_context_high->equity_24h` score `3.3605` n `133` status `ready` deltaP `18.7695` edge `0.2891` maxDD `-6.0681`
- `market_context_high->crypto_major_4h` score `1.1498` n `134` status `ready` deltaP `15.0778` edge `0.1671` maxDD `-6.7444`
- `market_context_high->crypto_major_1h` score `1.0197` n `134` status `ready` deltaP `12.5369` edge `0.0455` maxDD `-1.5286`
- `market_context_high->equity_4h` score `0.7113` n `134` status `ready` deltaP `3.2361` edge `0.2712` maxDD `-7.4596`
- `market_context_high->crypto_alt_4h` score `0.6682` n `134` status `ready` deltaP `7.92` edge `0.1146` maxDD `-3.9374`
- `market_context_high->equity_1h` score `0.5868` n `134` status `ready` deltaP `8.0588` edge `0.0811` maxDD `-4.2072`
- `market_context_high->index_1h` score `0.3549` n `134` status `ready` deltaP `8.5182` edge `0.0158` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.0528` n `134` status `ready` deltaP `3.137` edge `0.0296` maxDD `-1.6893`
- `market_context_high->index_4h` score `-0.1262` n `134` status `ready` deltaP `12.3808` edge `0.0471` maxDD `-1.3325`
- `market_context_high->fx_24h` score `-0.1544` n `133` status `ready` deltaP `10.2696` edge `0.0205` maxDD `-3.0343`
- `market_context_high->commodity_1h` score `-0.2608` n `134` status `ready` deltaP `2.9357` edge `0.0046` maxDD `-0.6722`
- `market_context_high->commodity_4h` score `-0.3983` n `134` status `ready` deltaP `2.2594` edge `0.0111` maxDD `-1.0817`
- `market_context_high->fx_1h` score `-0.4274` n `134` status `ready` deltaP `0.6051` edge `-0.0009` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.8212` n `134` status `ready` deltaP `1.8009` edge `0.0199` maxDD `-0.6936`
- `market_context_high->metal_24h` score `-0.9348` n `134` status `ready` deltaP `2.1818` edge `0.1222` maxDD `-2.5051`
- `market_context_high->unknown_1h` score `-1.2757` n `134` status `ready` deltaP `-0.1497` edge `-0.0463` maxDD `-1.054`
- `market_context_high->metal_4h` score `-1.476` n `134` status `ready` deltaP `1.372` edge `0.0745` maxDD `-1.5318`
- `market_context_high->fx_4h` score `-1.5192` n `134` status `ready` deltaP `-4.295` edge `-0.0033` maxDD `-1.6936`
- `market_context_high->commodity_24h` score `-1.6528` n `133` status `ready` deltaP `5.8225` edge `-0.0182` maxDD `-7.0012`
- `market_context_high->unknown_4h` score `-2.4464` n `134` status `ready` deltaP `14.8366` edge `-0.1697` maxDD `-1.9798`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
