# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T05:22:34.054619+00:00`
- Price records: `672`
- Market context records: `6359`
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

- `news_risk_high->crypto_alt_24h` score `14.9136` n `32` status `ready` deltaP `40.9722` edge `0.9844` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.2552` n `32` status `ready` deltaP `51.9097` edge `0.1752` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.4639` n `32` status `ready` deltaP `17.7083` edge `0.5322` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `4.09` n `32` status `ready` deltaP `42.4543` edge `0.0624` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.8271` n `32` status `ready` deltaP `33.1597` edge `0.1184` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.338` n `32` status `ready` deltaP `28.1437` edge `0.0211` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.5255` n `32` status `ready` deltaP `15.0262` edge `0.1421` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.9299` n `32` status `ready` deltaP `11.7702` edge `0.0869` maxDD `-1.6923`
- `market_context_high->metal_4h` score `0.7498` n `204` status `ready` deltaP `14.9599` edge `0.0424` maxDD `-2.7056`
- `market_context_high->index_4h` score `0.066` n `204` status `ready` deltaP `7.6399` edge `0.0222` maxDD `-0.4108`
- `market_context_high->unknown_1h` score `-0.1202` n `215` status `ready` deltaP `-7.8457` edge `0.1431` maxDD `-3.7317`
- `market_context_high->metal_1h` score `-0.3904` n `215` status `ready` deltaP `3.7662` edge `0.0026` maxDD `-1.8877`
- `market_context_high->commodity_24h` score `-0.5155` n `129` status `ready` deltaP `-3.9285` edge `0.1465` maxDD `-6.2457`
- `market_context_high->index_1h` score `-0.5856` n `215` status `ready` deltaP `-0.949` edge `0.0032` maxDD `-0.7564`
- `market_context_high->metal_24h` score `-0.6376` n `129` status `ready` deltaP `14.9103` edge `0.0757` maxDD `-11.8809`
- `market_context_high->equity_4h` score `-0.6971` n `204` status `ready` deltaP `5.2516` edge `0.0455` maxDD `-8.2573`
- `news_risk_high->index_24h` score `-0.7034` n `32` status `ready` deltaP `0.5208` edge `-0.0065` maxDD `-2.3058`
- `news_risk_high->unknown_1h` score `-0.7395` n `32` status `ready` deltaP `5.4828` edge `-0.0637` maxDD `-0.7581`
- `news_risk_high->metal_1h` score `-0.7652` n `32` status `ready` deltaP `-3.4431` edge `-0.0254` maxDD `-1.6464`
- `market_context_high->fx_1h` score `-0.7666` n `215` status `ready` deltaP `-1.2749` edge `-0.002` maxDD `-0.9376`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
