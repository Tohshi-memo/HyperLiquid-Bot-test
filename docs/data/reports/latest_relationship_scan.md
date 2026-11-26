# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T11:07:28.361068+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3455`

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

- `news_risk_high->unknown_4h` score `3234.5947` n `31` status `ready` deltaP `3.4815` edge `269.532` maxDD `-0.1191`
- `news_risk_high->unknown_1h` score `3233.3377` n `31` status `ready` deltaP `1.4825` edge `269.4525` maxDD `-0.7395`
- `market_context_high->unknown_1h` score `103.0459` n `31` status `ready` deltaP `1.4825` edge `8.5867` maxDD `-0.4209`
- `news_risk_high->equity_24h` score `36.8038` n `31` status `ready` deltaP `44.0972` edge `2.773` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `36.5192` n `31` status `ready` deltaP `44.9653` edge `2.7435` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `30.7925` n `31` status `ready` deltaP `44.2708` edge `2.2709` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.0424` n `31` status `ready` deltaP `27.9799` edge `0.8207` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.8694` n `31` status `ready` deltaP `39.8161` edge `0.6884` maxDD `-2.178`
- `news_risk_high->metal_24h` score `8.8562` n `31` status `ready` deltaP `30.6452` edge `0.5612` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `7.0712` n `31` status `ready` deltaP `19.9793` edge `0.9151` maxDD `-7.6714`
- `news_risk_high->index_24h` score `6.1181` n `31` status `ready` deltaP `45.4861` edge `0.2066` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.0869` n `31` status `ready` deltaP `43.1004` edge `0.1494` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.898` n `31` status `ready` deltaP `21.4844` edge `0.2003` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.5817` n `31` status `ready` deltaP `38.4442` edge `0.0682` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.8148` n `31` status `ready` deltaP `33.1901` edge `0.0218` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.5179` n `31` status `ready` deltaP `10.1603` edge `0.3012` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.2993` n `31` status `ready` deltaP `13.304` edge `0.2418` maxDD `-1.5232`
- `market_context_high->fx_4h` score `2.013` n `31` status `ready` deltaP `25.7426` edge `0.0246` maxDD `-0.2774`
- `news_risk_high->metal_1h` score `1.5142` n `31` status `ready` deltaP `29.5827` edge `0.0248` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.0652` n `31` status `ready` deltaP `16.1683` edge `0.0845` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
