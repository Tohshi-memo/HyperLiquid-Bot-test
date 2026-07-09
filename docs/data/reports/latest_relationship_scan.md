# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-09T04:07:31.808516+00:00`
- Price records: `672`
- Market context records: `6154`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11131`

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

- `news_risk_high->crypto_alt_24h` score `12.2141` n `30` status `ready` deltaP `42.5534` edge `0.7489` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `7.6025` n `30` status `ready` deltaP `67.0711` edge `0.1864` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.2442` n `32` status `ready` deltaP `44.2019` edge `0.0636` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3962` n `32` status `ready` deltaP `28.8117` edge `0.0215` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.6983` n `195` status `ready` deltaP `1.1912` edge `0.2344` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.291` n `32` status `ready` deltaP `13.7565` edge `0.1205` maxDD `-2.0691`
- `news_risk_high->crypto_major_24h` score `0.7484` n `30` status `ready` deltaP `13.2466` edge `0.0856` maxDD `-4.2368`
- `news_risk_high->crypto_alt_1h` score `0.697` n `32` status `ready` deltaP `9.0013` edge `0.0755` maxDD `-1.6923`
- `market_context_high->equity_4h` score `0.0078` n `195` status `ready` deltaP `2.7702` edge `0.0739` maxDD `-2.671`
- `market_context_high->unknown_4h` score `-0.222` n `195` status `ready` deltaP `-1.7656` edge `0.2465` maxDD `-11.925`
- `news_risk_high->index_24h` score `-0.2233` n `30` status `ready` deltaP `7.5794` edge `0.008` maxDD `-2.3058`
- `market_context_high->metal_24h` score `-0.2462` n `195` status `ready` deltaP `18.7166` edge `0.1005` maxDD `-11.8809`
- `market_context_high->fx_1h` score `-0.2726` n `195` status `ready` deltaP `1.504` edge `-0.0004` maxDD `-0.5659`
- `market_context_high->metal_4h` score `-0.5694` n `195` status `ready` deltaP `4.2361` edge `0.0175` maxDD `-3.4996`
- `news_risk_high->commodity_24h` score `-0.6093` n `30` status `ready` deltaP `14.0497` edge `-0.1239` maxDD `-0.3101`
- `news_risk_high->metal_1h` score `-0.7269` n `32` status `ready` deltaP `-2.4664` edge `-0.027` maxDD `-1.6464`
- `market_context_high->commodity_1h` score `-0.7425` n `195` status `ready` deltaP `-1.911` edge `-0.0045` maxDD `-0.5708`
- `market_context_high->metal_1h` score `-0.7526` n `195` status `ready` deltaP `2.9182` edge `-0.0023` maxDD `-2.0564`
- `market_context_high->equity_1h` score `-0.8682` n `195` status `ready` deltaP `-1.6742` edge `0.0114` maxDD `-4.2573`
- `market_context_high->crypto_alt_1h` score `-0.8789` n `195` status `ready` deltaP `3.9853` edge `0.036` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
