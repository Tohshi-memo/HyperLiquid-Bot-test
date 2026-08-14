# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-14T18:07:29.497763+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11796`

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

- `market_context_high->unknown_24h` score `136.1173` n `128` status `ready` deltaP `-33.2466` edge `11.856` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `32.7552` n `32` status `ready` deltaP `-46.5278` edge `4.5846` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `32.7552` n `32` status `ready` deltaP `-46.5278` edge `4.5846` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `10.1782` n `36` status `ready` deltaP `12.5` edge `0.8028` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.5291` n `36` status `ready` deltaP `39.6341` edge `0.3632` maxDD `0.0`
- `market_context_high->commodity_24h` score `5.0496` n `128` status `ready` deltaP `28.7326` edge `0.235` maxDD `-0.1266`
- `risk_on_high->commodity_24h` score `4.6257` n `32` status `ready` deltaP `31.0764` edge `0.1783` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.6257` n `32` status `ready` deltaP `31.0764` edge `0.1783` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.737` n `32` status `ready` deltaP `18.9787` edge `0.1198` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.737` n `32` status `ready` deltaP `18.9787` edge `0.1198` maxDD `-0.1258`
- `risk_on_high->crypto_major_24h` score `2.4952` n `32` status `ready` deltaP `18.75` edge `0.3105` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `2.4952` n `32` status `ready` deltaP `18.75` edge `0.3105` maxDD `-6.2481`
- `news_risk_high->index_24h` score `2.2968` n `36` status `ready` deltaP `16.3194` edge `0.0826` maxDD `0.0`
- `news_risk_high->index_4h` score `1.8573` n `36` status `ready` deltaP `21.4431` edge `0.025` maxDD `-0.0546`
- `market_context_high->commodity_4h` score `1.7892` n `128` status `ready` deltaP `17.4162` edge `0.0801` maxDD `-0.7687`
- `news_risk_high->equity_1h` score `1.695` n `36` status `ready` deltaP `8.2835` edge `0.1179` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.2791` n `32` status `ready` deltaP `13.5105` edge `0.0398` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2791` n `32` status `ready` deltaP `13.5105` edge `0.0398` maxDD `-0.1957`
- `risk_on_high->fx_24h` score `1.1019` n `32` status `ready` deltaP `13.1944` edge `0.0223` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.1019` n `32` status `ready` deltaP `13.1944` edge `0.0223` maxDD `-0.1418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
