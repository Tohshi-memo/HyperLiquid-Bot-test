# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T01:37:31.632121+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3540`

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

- `news_risk_high->unknown_1h` score `3210.8172` n `31` status `ready` deltaP `1.7819` edge `267.5738` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3175.1514` n `31` status `ready` deltaP `4.3962` edge `264.5723` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `26.2236` n `31` status `ready` deltaP `35.0694` edge `1.9515` maxDD `0.0`
- `news_risk_high->equity_24h` score `23.3787` n `31` status `ready` deltaP `34.5486` edge `1.7179` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `20.1241` n `31` status `ready` deltaP `34.2014` edge `1.449` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.4866` n `31` status `ready` deltaP `23.7116` edge `0.7195` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.2049` n `31` status `ready` deltaP `34.7856` edge `0.4999` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `6.2231` n `31` status `ready` deltaP `16.7781` edge `0.8277` maxDD `-7.6714`
- `news_risk_high->metal_24h` score `6.1878` n `31` status `ready` deltaP `21.9646` edge `0.3967` maxDD `-0.1986`
- `news_risk_high->fx_24h` score `4.9592` n `31` status `ready` deltaP `42.0587` edge `0.1457` maxDD `-0.0262`
- `news_risk_high->index_24h` score `4.1453` n `31` status `ready` deltaP `36.1111` edge `0.1047` maxDD `0.0`
- `news_risk_high->equity_1h` score `2.9998` n `31` status `ready` deltaP `17.7419` edge `0.1504` maxDD `-0.1621`
- `news_risk_high->index_4h` score `2.9013` n `31` status `ready` deltaP `32.8039` edge `0.0491` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.538` n `31` status `ready` deltaP `30.4955` edge `0.0167` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.1906` n `31` status `ready` deltaP `7.4657` edge `0.2772` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.9572` n `31` status `ready` deltaP `10.4597` edge `0.2169` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.2805` n `31` status `ready` deltaP `26.5887` edge `0.0148` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.5825` n `31` status `ready` deltaP `12.6623` edge `0.046` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.1839` n `31` status `ready` deltaP `8.8267` edge `0.0045` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.5377` n `31` status `ready` deltaP `-3.7087` edge `0.0061` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
