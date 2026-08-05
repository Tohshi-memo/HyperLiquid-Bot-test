# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T12:37:25.538812+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11648`

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

- `market_context_high->unknown_24h` score `13.9337` n `89` status `ready` deltaP `8.9458` edge `1.1058` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.4131` n `92` status `ready` deltaP `2.2402` edge `0.5357` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.8291` n `92` status `ready` deltaP `18.7433` edge `0.1121` maxDD `-2.7703`
- `market_context_high->fx_24h` score `1.1507` n `89` status `ready` deltaP `27.3604` edge `0.0857` maxDD `-4.3126`
- `market_context_high->metal_24h` score `0.876` n `89` status `ready` deltaP `1.6268` edge `0.2183` maxDD `-2.6802`
- `market_context_high->commodity_1h` score `0.4741` n `98` status `ready` deltaP `7.7417` edge `0.0295` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0731` n `98` status `ready` deltaP `6.6388` edge `-0.0032` maxDD `-0.7973`
- `market_context_high->fx_4h` score `0.0669` n `92` status `ready` deltaP `13.1363` edge `0.007` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5848` n `98` status `ready` deltaP `-2.1783` edge `-0.011` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.6745` n `98` status `ready` deltaP `-2.1111` edge `-0.019` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.94` n `92` status `ready` deltaP `1.1333` edge `-0.0046` maxDD `-3.211`
- `market_context_high->crypto_alt_1h` score `-0.9713` n `98` status `ready` deltaP `-4.5857` edge `-0.0229` maxDD `-3.0178`
- `market_context_high->crypto_alt_24h` score `-1.4617` n `89` status `ready` deltaP `0.6768` edge `-0.0476` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-1.5977` n `92` status `ready` deltaP `-1.0273` edge `-0.059` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.7816` n `98` status `ready` deltaP `2.5144` edge `-0.0916` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.1831` n `92` status `ready` deltaP `-13.6268` edge `-0.0636` maxDD `-4.7021`
- `market_context_high->index_24h` score `-2.5044` n `89` status `ready` deltaP `-11.1287` edge `-0.0274` maxDD `-7.8922`
- `market_context_high->unknown_1h` score `-3.1433` n `98` status `ready` deltaP `4.7477` edge `-0.2489` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.6644` n `98` status `ready` deltaP `-13.5647` edge `-0.0776` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.0222` n `89` status `ready` deltaP `10.998` edge `-0.0304` maxDD `-50.8663`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
