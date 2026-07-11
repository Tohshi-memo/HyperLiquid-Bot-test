# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T20:22:25.479958+00:00`
- Price records: `672`
- Market context records: `6426`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5871`

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

- `news_risk_high->crypto_alt_24h` score `12.2141` n `32` status `ready` deltaP `31.4236` edge `0.8231` maxDD `-0.5131`
- `market_context_high->unknown_24h` score `7.2304` n `146` status `ready` deltaP `18.7738` edge `0.8074` maxDD `-15.0689`
- `news_risk_high->fx_24h` score `6.5846` n `32` status `ready` deltaP `55.3819` edge `0.1795` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1741` n `32` status `ready` deltaP `43.5213` edge `0.0623` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `4.1276` n `32` status `ready` deltaP `35.4167` edge `0.1284` maxDD `-0.3101`
- `news_risk_high->crypto_major_24h` score `3.5369` n `32` status `ready` deltaP `13.0208` edge `0.4446` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.4841` n `32` status `ready` deltaP `29.9401` edge `0.0213` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.5209` n `32` status `ready` deltaP `14.4274` edge `0.1455` maxDD `-2.0691`
- `market_context_high->unknown_1h` score `0.8835` n `200` status `ready` deltaP `-6.7455` edge `0.2087` maxDD `-3.2083`
- `news_risk_high->crypto_alt_1h` score `0.8661` n `32` status `ready` deltaP `10.1235` edge `0.0897` maxDD `-1.6923`
- `market_context_high->metal_4h` score `0.3128` n `194` status `ready` deltaP `10.2731` edge `0.0414` maxDD `-2.7056`
- `market_context_high->index_4h` score `0.2348` n `194` status `ready` deltaP `9.5848` edge `0.0233` maxDD `-0.4108`
- `news_risk_high->unknown_1h` score `-0.1902` n `32` status `ready` deltaP `7.1295` edge `-0.0289` maxDD `-0.7581`
- `market_context_high->metal_24h` score `-0.3156` n `146` status `ready` deltaP `18.0865` edge `0.0958` maxDD `-11.8809`
- `market_context_high->metal_1h` score `-0.539` n `200` status `ready` deltaP `1.0` edge `0.002` maxDD `-1.8877`
- `news_risk_high->metal_1h` score `-0.5807` n `32` status `ready` deltaP `0.0` edge `-0.0247` maxDD `-1.6464`
- `market_context_high->equity_4h` score `-0.6072` n `194` status `ready` deltaP `6.8613` edge `0.0463` maxDD `-8.2573`
- `market_context_high->commodity_1h` score `-0.6425` n `200` status `ready` deltaP `-1.7485` edge `-0.0024` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.7023` n `200` status `ready` deltaP `-3.1467` edge `0.0029` maxDD `-0.7564`
- `market_context_high->fx_1h` score `-0.7456` n `200` status `ready` deltaP `-1.0599` edge `-0.002` maxDD `-0.9123`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
