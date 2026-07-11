# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T18:07:28.762919+00:00`
- Price records: `672`
- Market context records: `6416`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5869`

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

- `news_risk_high->crypto_alt_24h` score `12.8719` n `32` status `ready` deltaP `32.9861` edge `0.8675` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.6847` n `32` status `ready` deltaP `56.4236` edge `0.1809` maxDD `0.0`
- `market_context_high->unknown_24h` score `5.4295` n `146` status `ready` deltaP `14.6832` edge `0.6846` maxDD `-15.0689`
- `news_risk_high->fx_4h` score `4.2289` n `32` status `ready` deltaP `44.1311` edge `0.0628` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `4.1729` n `32` status `ready` deltaP `35.9375` edge `0.1287` maxDD `-0.3101`
- `news_risk_high->crypto_major_24h` score `3.8342` n `32` status `ready` deltaP `14.5833` edge `0.4723` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.4721` n `32` status `ready` deltaP `29.7904` edge `0.0213` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.51` n `32` status `ready` deltaP `14.4274` edge `0.1441` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.8637` n `32` status `ready` deltaP `10.2732` edge `0.0884` maxDD `-1.6923`
- `market_context_high->unknown_1h` score `0.7073` n `205` status `ready` deltaP `-5.8266` edge `0.1986` maxDD `-3.7317`
- `market_context_high->metal_4h` score `0.3768` n `203` status `ready` deltaP `11.0725` edge `0.0414` maxDD `-2.7056`
- `market_context_high->index_4h` score `0.1597` n `203` status `ready` deltaP `8.7521` edge `0.0226` maxDD `-0.4108`
- `market_context_high->metal_24h` score `-0.2883` n `146` status `ready` deltaP `18.5978` edge `0.0959` maxDD `-11.8809`
- `news_risk_high->unknown_1h` score `-0.2884` n `32` status `ready` deltaP `6.2313` edge `-0.0311` maxDD `-0.7581`
- `market_context_high->metal_1h` score `-0.524` n `205` status `ready` deltaP `1.2582` edge `0.0022` maxDD `-1.8877`
- `news_risk_high->metal_1h` score `-0.6048` n `32` status `ready` deltaP `-0.4491` edge `-0.0248` maxDD `-1.6464`
- `market_context_high->fx_1h` score `-0.7285` n `205` status `ready` deltaP `-0.8194` edge `-0.0019` maxDD `-0.9342`
- `market_context_high->index_1h` score `-0.7428` n `205` status `ready` deltaP `-3.8805` edge `0.0026` maxDD `-0.7564`
- `news_risk_high->index_24h` score `-0.7534` n `32` status `ready` deltaP `0.5208` edge `-0.0129` maxDD `-2.3058`
- `market_context_high->commodity_24h` score `-0.7682` n `146` status `ready` deltaP `-3.232` edge `0.1152` maxDD `-5.7046`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
