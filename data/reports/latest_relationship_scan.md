# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T17:52:48.936835+00:00`
- Price records: `672`
- Market context records: `6306`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11133`

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

- `news_risk_high->crypto_alt_24h` score `15.219` n `32` status `ready` deltaP `43.2292` edge `0.9948` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `5.9941` n `32` status `ready` deltaP `50.5208` edge `0.1627` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1985` n `32` status `ready` deltaP `43.8262` edge `0.0623` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `4.1812` n `32` status `ready` deltaP `16.6667` edge `0.5029` maxDD `-4.2368`
- `news_risk_high->commodity_24h` score `3.1803` n `32` status `ready` deltaP `28.6458` edge `0.0946` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.4003` n `32` status `ready` deltaP `28.8922` edge `0.0213` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.4507` n `32` status `ready` deltaP `14.2777` edge `0.1375` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.919` n `32` status `ready` deltaP `11.6205` edge `0.0865` maxDD `-1.6923`
- `market_context_high->unknown_1h` score `0.8387` n `208` status `ready` deltaP `-2.9537` edge `0.1904` maxDD `-3.7317`
- `market_context_high->metal_4h` score `0.0144` n `196` status `ready` deltaP `9.0032` edge `0.0375` maxDD `-2.7056`
- `market_context_high->metal_24h` score `-0.1229` n `166` status `ready` deltaP `20.9526` edge `0.1014` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.4313` n `32` status `ready` deltaP `5.0347` edge `-0.0017` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.4474` n `208` status `ready` deltaP `2.9249` edge `0.0009` maxDD `-1.8877`
- `market_context_high->commodity_1h` score `-0.5819` n `208` status `ready` deltaP `-0.7485` edge `-0.0013` maxDD `-2.1314`
- `market_context_high->fx_1h` score `-0.7146` n `208` status `ready` deltaP `-0.9155` edge `-0.0021` maxDD `-0.7747`
- `news_risk_high->metal_1h` score `-0.7278` n `32` status `ready` deltaP `-2.8443` edge `-0.0246` maxDD `-1.6464`
- `market_context_high->equity_4h` score `-0.7829` n `196` status `ready` deltaP `4.2466` edge `0.0412` maxDD `-8.2573`
- `market_context_high->index_1h` score `-0.805` n `208` status `ready` deltaP `-2.7896` edge `0.0023` maxDD `-0.9531`
- `market_context_high->index_4h` score `-0.9258` n `196` status `ready` deltaP `1.7609` edge `0.016` maxDD `-1.381`
- `market_context_high->equity_1h` score `-0.9544` n `208` status `ready` deltaP `-1.6064` edge `-0.0001` maxDD `-4.2573`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
