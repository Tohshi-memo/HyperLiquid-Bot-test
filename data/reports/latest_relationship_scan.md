# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T06:52:31.393232+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3564`

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

- `news_risk_high->unknown_1h` score `3225.1633` n `31` status `ready` deltaP `1.6322` edge `268.7703` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3182.8306` n `31` status `ready` deltaP `3.7864` edge `265.2163` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `21.8267` n `31` status `ready` deltaP `31.4236` edge `1.6094` maxDD `0.0`
- `news_risk_high->equity_24h` score `19.5878` n `31` status `ready` deltaP `30.9028` edge `1.4263` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.5216` n `31` status `ready` deltaP `30.5556` edge `1.1731` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.0714` n `31` status `ready` deltaP `22.797` edge `0.691` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `6.974` n `31` status `ready` deltaP `32.1942` edge `0.4146` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `5.7979` n `31` status `ready` deltaP `15.711` edge `0.7803` maxDD `-7.6714`
- `news_risk_high->metal_24h` score `5.525` n `31` status `ready` deltaP `18.8396` edge `0.3623` maxDD `-0.1986`
- `news_risk_high->fx_24h` score `4.643` n `31` status `ready` deltaP `38.5865` edge `0.1425` maxDD `-0.0262`
- `news_risk_high->index_24h` score `3.4972` n `31` status `ready` deltaP `32.4653` edge `0.075` maxDD `0.0`
- `news_risk_high->index_4h` score `2.6722` n `31` status `ready` deltaP `30.9747` edge `0.0422` maxDD `-0.4146`
- `news_risk_high->equity_1h` score `2.6017` n `31` status `ready` deltaP `16.0952` edge `0.1282` maxDD `-0.1621`
- `news_risk_high->index_1h` score `2.3847` n `31` status `ready` deltaP `28.8488` edge `0.0149` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.0792` n `31` status `ready` deltaP `6.8669` edge `0.2669` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.8458` n `31` status `ready` deltaP `9.5615` edge `0.2086` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1551` n `31` status `ready` deltaP `25.0917` edge `0.0087` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.4482` n `31` status `ready` deltaP `12.5098` edge `0.0298` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `-0.0878` n `31` status `ready` deltaP `5.7779` edge `-0.01` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.6551` n `31` status `ready` deltaP `-4.9063` edge `0.0043` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
