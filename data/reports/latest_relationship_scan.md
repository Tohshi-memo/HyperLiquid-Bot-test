# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T22:22:32.284570+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9857`

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

- `market_context_high->unknown_24h` score `18.7056` n `78` status `ready` deltaP `18.5096` edge `1.4397` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.4025` n `90` status `ready` deltaP `1.7479` edge `0.5381` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.609` n `90` status `ready` deltaP `17.5373` edge `0.1018` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.8776` n `78` status `ready` deltaP `-1.0283` edge `0.2362` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.7455` n `78` status `ready` deltaP `21.0069` edge `0.0761` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.2989` n `90` status `ready` deltaP `5.7917` edge `0.0279` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.1111` n `90` status `ready` deltaP `7.1557` edge `-0.0036` maxDD `-0.7878`
- `market_context_high->fx_4h` score `0.1108` n `90` status `ready` deltaP `13.9194` edge `0.0074` maxDD `-1.8797`
- `market_context_high->crypto_alt_24h` score `-0.3633` n `78` status `ready` deltaP `5.5689` edge `0.0606` maxDD `-4.5445`
- `market_context_high->metal_1h` score `-0.5511` n `90` status `ready` deltaP `-1.7565` edge `-0.0095` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.5651` n `90` status `ready` deltaP `-0.0066` edge `-0.019` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.7235` n `90` status `ready` deltaP `3.0318` edge `0.0105` maxDD `-3.211`
- `market_context_high->crypto_alt_1h` score `-0.7289` n `90` status `ready` deltaP `-2.159` edge `-0.008` maxDD `-3.0178`
- `market_context_high->crypto_alt_4h` score `-0.9347` n `90` status `ready` deltaP `3.6382` edge `-0.0051` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.6838` n `90` status `ready` deltaP `4.6507` edge `-0.0933` maxDD `-10.619`
- `market_context_high->index_24h` score `-1.9969` n `78` status `ready` deltaP `-7.5187` edge `0.0136` maxDD `-7.8922`
- `market_context_high->index_4h` score `-2.0185` n `90` status `ready` deltaP `-11.8259` edge `-0.0545` maxDD `-4.7021`
- `market_context_high->crypto_major_1h` score `-3.3877` n `90` status `ready` deltaP `-11.2608` edge `-0.0699` maxDD `-7.6533`
- `market_context_high->unknown_1h` score `-3.4336` n `90` status `ready` deltaP `1.8995` edge `-0.2541` maxDD `-1.2421`
- `market_context_high->commodity_24h` score `-4.8146` n `78` status `ready` deltaP `7.7724` edge `-0.0747` maxDD `-36.8831`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
