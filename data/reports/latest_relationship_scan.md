# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T14:07:21.021287+00:00`
- Price records: `672`
- Market context records: `2464`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9224`

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

- `news_risk_high->crypto_alt_24h` score `21.825` n `33` status `ready` deltaP `45.4072` edge `1.5749` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `21.5731` n `33` status `ready` deltaP `55.9975` edge `1.4684` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `19.0472` n `33` status `ready` deltaP `29.0878` edge `1.4248` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `12.9722` n `33` status `ready` deltaP `24.4476` edge `0.9761` maxDD `-3.3119`
- `news_risk_high->index_24h` score `9.0407` n `33` status `ready` deltaP `27.3516` edge `0.5921` maxDD `-1.3507`
- `news_risk_high->unknown_24h` score `7.0886` n `33` status `ready` deltaP `24.2266` edge `0.4518` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `5.8031` n `113` status `ready` deltaP `21.9472` edge `0.3701` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `3.9499` n `136` status `ready` deltaP `20.5882` edge `0.4598` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.8971` n `136` status `ready` deltaP `18.0236` edge `0.3856` maxDD `-10.1468`
- `news_risk_high->fx_24h` score `3.6557` n `33` status `ready` deltaP `36.3321` edge `0.0809` maxDD `-0.1442`
- `news_risk_high->commodity_4h` score `3.4992` n `33` status `ready` deltaP `23.0137` edge `0.2053` maxDD `-3.0367`
- `news_risk_high->metal_4h` score `2.7486` n `33` status `ready` deltaP `12.9112` edge `0.3571` maxDD `-3.93`
- `market_context_high->crypto_major_24h` score `2.4566` n `113` status `ready` deltaP `12.0314` edge `0.624` maxDD `-25.1408`
- `news_risk_high->equity_4h` score `1.8368` n `33` status `ready` deltaP `-9.3634` edge `0.3806` maxDD `-3.2819`
- `news_risk_high->fx_4h` score `1.822` n `33` status `ready` deltaP `23.0137` edge `0.0168` maxDD `-0.1382`
- `market_context_high->unknown_4h` score `1.5273` n `136` status `ready` deltaP `9.6934` edge `0.1647` maxDD `-3.4972`
- `news_risk_high->unknown_1h` score `1.5018` n `33` status `ready` deltaP `18.9485` edge `0.042` maxDD `-1.4536`
- `news_risk_high->fx_1h` score `1.132` n `33` status `ready` deltaP `15.7685` edge `0.0148` maxDD `-0.0473`
- `market_context_high->crypto_major_1h` score `0.7914` n `136` status `ready` deltaP `8.6342` edge `0.1278` maxDD `-4.2199`
- `market_context_high->index_24h` score `0.7236` n `113` status `ready` deltaP `4.7182` edge `0.0958` maxDD `-1.3562`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
