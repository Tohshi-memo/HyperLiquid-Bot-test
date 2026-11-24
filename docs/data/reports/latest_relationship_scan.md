# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T00:37:28.476245+00:00`
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

- `market_context_high->unknown_1h` score `32408.0449` n `45` status `ready` deltaP `2.6147` edge `2700.6624` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22242.9464` n `45` status `ready` deltaP `3.6349` edge `1853.5685` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1198.5155` n `31` status `ready` deltaP `2.8298` edge `99.875` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1007.5932` n `31` status `ready` deltaP `4.8535` edge `83.9394` maxDD `-0.119`
- `news_risk_high->equity_24h` score `38.018` n `31` status `ready` deltaP `43.75` edge `2.8765` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `34.9889` n `31` status `ready` deltaP `45.4861` edge `2.6125` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `30.9432` n `31` status `ready` deltaP `45.6597` edge `2.2742` maxDD `0.0`
- `news_risk_high->metal_24h` score `12.2196` n `31` status `ready` deltaP `44.1869` edge `0.7512` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.5712` n `31` status `ready` deltaP `23.5592` edge `0.8109` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.7201` n `31` status `ready` deltaP `30.9747` edge `0.5684` maxDD `-2.1911`
- `news_risk_high->fx_24h` score `6.6123` n `31` status `ready` deltaP `56.4684` edge `0.1874` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `6.4501` n `31` status `ready` deltaP `13.1196` edge `0.8812` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.9025` n `31` status `ready` deltaP `41.6667` edge `0.2141` maxDD `0.0`
- `market_context_high->fx_4h` score `3.3341` n `45` status `ready` deltaP `39.6917` edge `0.0417` maxDD `-0.2774`
- `news_risk_high->equity_1h` score `3.2073` n `31` status `ready` deltaP `17.7419` edge `0.1677` maxDD `-0.163`
- `news_risk_high->index_4h` score `2.9259` n `31` status `ready` deltaP `32.3466` edge `0.0542` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.4937` n `31` status `ready` deltaP `29.747` edge `0.018` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.475` n `31` status `ready` deltaP `10.9088` edge `0.2907` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.068` n `31` status `ready` deltaP `9.8609` edge `0.2351` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5446` n `31` status `ready` deltaP `29.8821` edge `0.0267` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
