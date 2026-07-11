# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T05:07:30.413760+00:00`
- Price records: `672`
- Market context records: `6358`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11122`

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

- `news_risk_high->crypto_alt_24h` score `14.9419` n `32` status `ready` deltaP `41.1458` edge `0.9856` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.2377` n `32` status `ready` deltaP `51.7361` edge `0.1749` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.4639` n `32` status `ready` deltaP `17.7083` edge `0.5322` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `4.09` n `32` status `ready` deltaP `42.4543` edge `0.0624` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.8036` n `32` status `ready` deltaP `32.9861` edge `0.1176` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.35` n `32` status `ready` deltaP `28.2934` edge `0.0211` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.513` n `32` status `ready` deltaP `14.8765` edge `0.1415` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.9158` n `32` status `ready` deltaP `11.6205` edge `0.0861` maxDD `-1.6923`
- `market_context_high->metal_4h` score `0.7391` n `203` status `ready` deltaP `14.8271` edge `0.0424` maxDD `-2.7056`
- `market_context_high->index_4h` score `0.0526` n `203` status `ready` deltaP `7.4733` edge `0.0222` maxDD `-0.4108`
- `market_context_high->unknown_1h` score `-0.0658` n `214` status `ready` deltaP `-7.6305` edge `0.1462` maxDD `-3.7317`
- `market_context_high->metal_1h` score `-0.3843` n `214` status `ready` deltaP `3.8838` edge `0.0026` maxDD `-1.8877`
- `market_context_high->commodity_24h` score `-0.5308` n `129` status `ready` deltaP `-4.1021` edge `0.1457` maxDD `-6.2457`
- `market_context_high->index_1h` score `-0.5976` n `214` status `ready` deltaP `-1.1794` edge `0.0032` maxDD `-0.7564`
- `market_context_high->metal_24h` score `-0.6384` n `129` status `ready` deltaP `14.9103` edge `0.0756` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.7027` n `32` status `ready` deltaP `0.5208` edge `-0.0064` maxDD `-2.3058`
- `news_risk_high->unknown_1h` score `-0.7335` n `32` status `ready` deltaP `5.4828` edge `-0.0632` maxDD `-0.7581`
- `news_risk_high->metal_1h` score `-0.773` n `32` status `ready` deltaP `-3.5928` edge `-0.0254` maxDD `-1.6464`
- `market_context_high->fx_1h` score `-0.7762` n `214` status `ready` deltaP `-1.3795` edge `-0.0021` maxDD `-0.9376`
- `market_context_high->unknown_4h` score `-0.9596` n `203` status `ready` deltaP `-12.7846` edge `0.2196` maxDD `-11.925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
