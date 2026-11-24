# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T01:22:24.821288+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4560`

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

- `market_context_high->unknown_1h` score `32398.9117` n `45` status `ready` deltaP `2.6147` edge `2699.9013` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22238.5342` n `45` status `ready` deltaP `3.7873` edge `1853.1998` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1189.3823` n `31` status `ready` deltaP `2.8298` edge `99.1139` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1003.181` n `31` status `ready` deltaP `5.0059` edge `83.5707` maxDD `-0.119`
- `news_risk_high->equity_24h` score `37.694` n `31` status `ready` deltaP `43.75` edge `2.8495` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `34.9709` n `31` status `ready` deltaP `45.4861` edge `2.611` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `30.924` n `31` status `ready` deltaP `45.6597` edge `2.2726` maxDD `0.0`
- `news_risk_high->metal_24h` score `12.1311` n `31` status `ready` deltaP `43.666` edge `0.7473` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.646` n `31` status `ready` deltaP `23.864` edge `0.8151` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.6877` n `31` status `ready` deltaP `30.9747` edge `0.5657` maxDD `-2.1911`
- `news_risk_high->fx_24h` score `6.6159` n `31` status `ready` deltaP `56.4684` edge `0.1877` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `6.4979` n `31` status `ready` deltaP `13.4244` edge `0.8853` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.8514` n `31` status `ready` deltaP `41.4931` edge `0.211` maxDD `0.0`
- `market_context_high->fx_4h` score `3.2915` n `45` status `ready` deltaP `39.2344` edge `0.0412` maxDD `-0.2774`
- `news_risk_high->equity_1h` score `3.1605` n `31` status `ready` deltaP `17.5922` edge `0.1648` maxDD `-0.163`
- `news_risk_high->index_4h` score `2.8919` n `31` status `ready` deltaP `32.0417` edge `0.0534` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.4656` n `31` status `ready` deltaP `10.9088` edge `0.2895` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.4626` n `31` status `ready` deltaP `29.4476` edge `0.0174` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.0712` n `31` status `ready` deltaP `9.8609` edge `0.2355` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5446` n `31` status `ready` deltaP `29.8821` edge `0.0267` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
