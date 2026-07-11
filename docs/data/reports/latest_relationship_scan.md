# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T17:52:23.979620+00:00`
- Price records: `672`
- Market context records: `6415`
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

- `news_risk_high->crypto_alt_24h` score `12.9242` n `32` status `ready` deltaP `33.1597` edge `0.8707` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.6871` n `32` status `ready` deltaP `56.4236` edge `0.1811` maxDD `0.0`
- `market_context_high->unknown_24h` score `5.1822` n `146` status `ready` deltaP `14.1719` edge `0.6674` maxDD `-15.0689`
- `news_risk_high->fx_4h` score `4.2289` n `32` status `ready` deltaP `44.1311` edge `0.0628` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `4.1904` n `32` status `ready` deltaP `36.1111` edge `0.129` maxDD `-0.3101`
- `news_risk_high->crypto_major_24h` score `3.8549` n `32` status `ready` deltaP `14.7569` edge `0.4738` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.4841` n `32` status `ready` deltaP `29.9401` edge `0.0213` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.5076` n `32` status `ready` deltaP `14.4274` edge `0.1438` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.859` n `32` status `ready` deltaP `10.2732` edge `0.0878` maxDD `-1.6923`
- `market_context_high->unknown_1h` score `0.7061` n `205` status `ready` deltaP `-5.8266` edge `0.1985` maxDD `-3.7317`
- `market_context_high->metal_4h` score `0.3779` n `204` status `ready` deltaP `11.1012` edge `0.0413` maxDD `-2.7056`
- `market_context_high->index_4h` score `0.1437` n `204` status `ready` deltaP `8.5665` edge `0.0225` maxDD `-0.4108`
- `market_context_high->metal_24h` score `-0.2883` n `146` status `ready` deltaP `18.5978` edge `0.0959` maxDD `-11.8809`
- `news_risk_high->unknown_1h` score `-0.2884` n `32` status `ready` deltaP `6.2313` edge `-0.0311` maxDD `-0.7581`
- `market_context_high->metal_1h` score `-0.5056` n `205` status `ready` deltaP `1.5963` edge `0.0023` maxDD `-1.8877`
- `news_risk_high->metal_1h` score `-0.6126` n `32` status `ready` deltaP `-0.5988` edge `-0.0248` maxDD `-1.6464`
- `market_context_high->commodity_1h` score `-0.709` n `205` status `ready` deltaP `-2.9823` edge `-0.0027` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.7428` n `205` status `ready` deltaP `-3.8805` edge `0.0026` maxDD `-0.7564`
- `news_risk_high->index_24h` score `-0.7541` n `32` status `ready` deltaP `0.5208` edge `-0.013` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.7584` n `205` status `ready` deltaP `-1.1575` edge `-0.0021` maxDD `-0.9376`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
