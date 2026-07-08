# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T16:22:26.471065+00:00`
- Price records: `672`
- Market context records: `6103`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11115`

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

- `news_risk_high->fx_24h` score `8.1293` n `30` status `ready` deltaP `72.3958` edge `0.1948` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `7.9599` n `30` status `ready` deltaP `34.8264` edge `0.4459` maxDD `-0.5131`
- `news_risk_high->fx_4h` score `4.1897` n `32` status `ready` deltaP `43.5213` edge `0.0636` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3164` n `32` status `ready` deltaP `27.8443` edge `0.0213` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.3119` n `32` status `ready` deltaP `14.128` edge `0.1207` maxDD `-2.0691`
- `market_context_high->equity_4h` score `1.2628` n `195` status `ready` deltaP `8.0183` edge `0.1435` maxDD `-2.671`
- `news_risk_high->crypto_alt_1h` score `0.7273` n `32` status `ready` deltaP `9.5247` edge `0.0759` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.0875` n `30` status `ready` deltaP `9.2361` edge `0.0368` maxDD `-2.3058`
- `news_risk_high->commodity_24h` score `-0.1793` n `30` status `ready` deltaP `15.6598` edge `-0.0988` maxDD `-0.3101`
- `market_context_high->fx_1h` score `-0.3245` n `195` status `ready` deltaP `0.5366` edge `-0.0006` maxDD `-0.5659`
- `market_context_high->equity_1h` score `-0.5733` n `195` status `ready` deltaP `1.6866` edge `0.0268` maxDD `-4.2573`
- `market_context_high->metal_4h` score `-0.5982` n `195` status `ready` deltaP `3.847` edge `0.0164` maxDD `-3.4996`
- `market_context_high->metal_1h` score `-0.6631` n `195` status `ready` deltaP `3.8876` edge `-0.0013` maxDD `-2.0564`
- `news_risk_high->metal_1h` score `-0.6687` n `32` status `ready` deltaP `-1.497` edge `-0.026` maxDD `-1.6464`
- `market_context_high->commodity_1h` score `-0.7404` n `195` status `ready` deltaP `-1.6897` edge `-0.0058` maxDD `-0.5708`
- `market_context_high->index_4h` score `-0.7977` n `195` status `ready` deltaP `2.9182` edge `0.0247` maxDD `-1.381`
- `market_context_high->crypto_alt_1h` score `-0.8486` n `195` status `ready` deltaP `4.5087` edge `0.0364` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.8861` n `195` status `ready` deltaP `4.9133` edge `0.0304` maxDD `-9.807`
- `news_risk_high->index_1h` score `-1.0587` n `32` status `ready` deltaP `-9.0756` edge `-0.0189` maxDD `-1.1725`
- `market_context_high->index_1h` score `-1.1556` n `195` status `ready` deltaP `-2.0083` edge `0.004` maxDD `-0.9531`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
