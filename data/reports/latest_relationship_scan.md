# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T09:22:24.265553+00:00`
- Price records: `672`
- Market context records: `6377`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11072`

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

- `news_risk_high->crypto_alt_24h` score `14.2762` n `32` status `ready` deltaP `38.1944` edge `0.9498` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.322` n `32` status `ready` deltaP `52.4306` edge `0.1773` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.295` n `32` status `ready` deltaP `17.5347` edge `0.5117` maxDD `-4.2368`
- `news_risk_high->commodity_24h` score `4.1393` n `32` status `ready` deltaP `35.9375` edge `0.1259` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `3.923` n `32` status `ready` deltaP `40.4726` edge `0.0617` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3859` n `32` status `ready` deltaP `28.7425` edge `0.0211` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.4928` n `32` status `ready` deltaP `14.4274` edge `0.1419` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.8792` n `32` status `ready` deltaP `11.0217` edge `0.0854` maxDD `-1.6923`
- `market_context_high->metal_4h` score `0.472` n `219` status `ready` deltaP `14.8297` edge `0.0413` maxDD `-2.7056`
- `market_context_high->unknown_1h` score `0.2591` n `223` status `ready` deltaP `-5.9088` edge `0.1618` maxDD `-3.7317`
- `market_context_high->index_4h` score `0.1831` n `219` status `ready` deltaP `9.1944` edge `0.0216` maxDD `-0.4108`
- `news_risk_high->unknown_1h` score `-0.2944` n `32` status `ready` deltaP `6.381` edge `-0.0326` maxDD `-0.7581`
- `market_context_high->metal_24h` score `-0.3623` n `141` status `ready` deltaP `18.2846` edge `0.0885` maxDD `-11.8809`
- `market_context_high->metal_1h` score `-0.3789` n `223` status `ready` deltaP `3.9573` edge `0.0028` maxDD `-1.8877`
- `market_context_high->index_1h` score `-0.6444` n `223` status `ready` deltaP `-2.0199` edge `0.0028` maxDD `-0.7564`
- `market_context_high->fx_1h` score `-0.6988` n `223` status `ready` deltaP `-0.5176` edge `-0.0014` maxDD `-0.9376`
- `news_risk_high->metal_1h` score `-0.7169` n `32` status `ready` deltaP `-2.5449` edge `-0.0252` maxDD `-1.6464`
- `news_risk_high->index_24h` score `-0.7292` n `32` status `ready` deltaP `0.5208` edge `-0.0098` maxDD `-2.3058`
- `market_context_high->commodity_24h` score `-0.7418` n `141` status `ready` deltaP `-5.1751` edge `0.1258` maxDD `-6.2457`
- `market_context_high->equity_4h` score `-0.8618` n `219` status `ready` deltaP `7.2245` edge `0.0499` maxDD `-8.2573`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
