# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T03:22:24.849505+00:00`
- Price records: `672`
- Market context records: `6350`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11134`

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

- `news_risk_high->crypto_alt_24h` score `15.108` n `32` status `ready` deltaP `42.1875` edge `0.9925` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.1569` n `32` status `ready` deltaP `51.0417` edge `0.1728` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.4486` n `32` status `ready` deltaP `17.5347` edge `0.5314` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `4.1144` n `32` status `ready` deltaP `42.7591` edge `0.0624` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.694` n `32` status `ready` deltaP `32.2917` edge `0.1131` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.3763` n `32` status `ready` deltaP `28.5928` edge `0.0213` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.5341` n `32` status `ready` deltaP `15.0262` edge `0.1432` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.919` n `32` status `ready` deltaP `11.6205` edge `0.0865` maxDD `-1.6923`
- `market_context_high->metal_4h` score `0.6629` n `196` status `ready` deltaP `13.8595` edge `0.0425` maxDD `-2.7056`
- `market_context_high->unknown_1h` score `0.072` n `208` status `ready` deltaP `-7.2576` edge `0.1552` maxDD `-3.7317`
- `market_context_high->index_4h` score `-0.0433` n `196` status `ready` deltaP `6.2593` edge `0.0223` maxDD `-0.4108`
- `market_context_high->commodity_24h` score `-0.602` n `129` status `ready` deltaP `-4.7965` edge `0.1412` maxDD `-6.2457`
- `market_context_high->metal_1h` score `-0.6029` n `208` status `ready` deltaP `3.7684` edge `0.0024` maxDD `-1.8877`
- `market_context_high->commodity_1h` score `-0.6593` n `208` status `ready` deltaP `-2.2225` edge `-0.0014` maxDD `-2.1314`
- `news_risk_high->index_24h` score `-0.714` n `32` status `ready` deltaP `0.3472` edge `-0.0067` maxDD `-2.3058`
- `market_context_high->metal_24h` score `-0.7148` n `129` status `ready` deltaP `13.6951` edge `0.0739` maxDD `-11.8809`
- `market_context_high->fx_1h` score `-0.7234` n `208` status `ready` deltaP `-0.7341` edge `-0.002` maxDD `-0.9376`
- `news_risk_high->metal_1h` score `-0.7644` n `32` status `ready` deltaP `-3.4431` edge `-0.0253` maxDD `-1.6464`
- `news_risk_high->unknown_1h` score `-0.7923` n `32` status `ready` deltaP `5.4828` edge `-0.0681` maxDD `-0.7581`
- `market_context_high->crypto_alt_1h` score `-0.9692` n `208` status `ready` deltaP `5.1301` edge `0.0168` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
