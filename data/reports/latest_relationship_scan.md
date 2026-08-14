# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-14T17:53:18.448056+00:00`
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

- `market_context_high->unknown_24h` score `133.694` n `129` status `ready` deltaP `-32.7439` edge `11.6507` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `32.7552` n `32` status `ready` deltaP `-46.5278` edge `4.5846` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `32.7552` n `32` status `ready` deltaP `-46.5278` edge `4.5846` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `10.1331` n `36` status `ready` deltaP `12.3264` edge `0.8002` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.4929` n `36` status `ready` deltaP `39.4817` edge `0.3612` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.9609` n `129` status `ready` deltaP `28.1492` edge `0.2315` maxDD `-0.1266`
- `risk_on_high->commodity_24h` score `4.6456` n `32` status `ready` deltaP `31.25` edge `0.1788` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.6456` n `32` status `ready` deltaP `31.25` edge `0.1788` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.7552` n `32` status `ready` deltaP `19.1311` edge `0.1203` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.7552` n `32` status `ready` deltaP `19.1311` edge `0.1203` maxDD `-0.1258`
- `risk_on_high->crypto_major_24h` score `2.4487` n `32` status `ready` deltaP `18.5764` edge `0.3057` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `2.4487` n `32` status `ready` deltaP `18.5764` edge `0.3057` maxDD `-6.2481`
- `news_risk_high->index_24h` score `2.2793` n `36` status `ready` deltaP `16.1458` edge `0.0823` maxDD `0.0`
- `news_risk_high->index_4h` score `1.8403` n `36` status `ready` deltaP `21.2906` edge `0.0246` maxDD `-0.0546`
- `market_context_high->commodity_4h` score `1.7311` n `129` status `ready` deltaP `16.9751` edge `0.0782` maxDD `-0.7687`
- `news_risk_high->equity_1h` score `1.6962` n `36` status `ready` deltaP `8.2835` edge `0.118` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.2791` n `32` status `ready` deltaP `13.5105` edge `0.0398` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2791` n `32` status `ready` deltaP `13.5105` edge `0.0398` maxDD `-0.1957`
- `risk_on_high->fx_24h` score `1.1031` n `32` status `ready` deltaP `13.1944` edge `0.0224` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.1031` n `32` status `ready` deltaP `13.1944` edge `0.0224` maxDD `-0.1418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
