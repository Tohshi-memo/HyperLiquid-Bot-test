# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T06:52:32.605732+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7458`

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

- `news_risk_high->unknown_24h` score `1153.0864` n `135` status `ready` deltaP `1.9097` edge `96.0778` maxDD `0.0`
- `market_context_high->unknown_1h` score `738.38` n `33` status `ready` deltaP `9.7305` edge `61.4668` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `18.3673` n `135` status `ready` deltaP `28.5532` edge `1.3612` maxDD `-1.0093`
- `news_risk_high->equity_24h` score `8.2957` n `135` status `ready` deltaP `28.3796` edge `0.737` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `7.8081` n `135` status `ready` deltaP `23.9931` edge `0.8061` maxDD `-15.8971`
- `news_risk_high->index_24h` score `3.8696` n `135` status `ready` deltaP `34.5718` edge `0.1398` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `3.5222` n `135` status `ready` deltaP `26.7477` edge `0.2426` maxDD `-2.192`
- `news_risk_high->equity_4h` score `2.9932` n `135` status `ready` deltaP `29.9333` edge `0.21` maxDD `-9.143`
- `news_risk_high->crypto_alt_4h` score `1.9398` n `135` status `ready` deltaP `11.4171` edge `0.3515` maxDD `-15.9436`
- `market_context_high->crypto_alt_1h` score `1.6892` n `33` status `ready` deltaP `10.157` edge `0.1345` maxDD `-3.5821`
- `market_context_high->fx_1h` score `1.5313` n `33` status `ready` deltaP `21.1577` edge `0.0088` maxDD `-0.113`
- `market_context_high->crypto_major_1h` score `1.3422` n `33` status `ready` deltaP `5.8565` edge `0.1338` maxDD `-3.546`
- `news_risk_high->crypto_alt_1h` score `1.1401` n `135` status `ready` deltaP `9.5509` edge `0.1224` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.9463` n `135` status `ready` deltaP `9.7006` edge `0.0765` maxDD `-1.6514`
- `market_context_high->equity_1h` score `0.6254` n `33` status `ready` deltaP `10.3067` edge `0.054` maxDD `-2.4027`
- `news_risk_high->index_1h` score `0.5448` n `135` status `ready` deltaP `9.4167` edge `0.0114` maxDD `-0.302`
- `market_context_high->metal_1h` score `0.3427` n `33` status `ready` deltaP `5.4074` edge `0.0146` maxDD `-0.4338`
- `market_context_high->index_1h` score `-0.0383` n `33` status `ready` deltaP `2.4134` edge `0.0127` maxDD `-0.3627`
- `news_risk_high->index_4h` score `-0.1004` n `135` status `ready` deltaP `7.2538` edge `0.0286` maxDD `-1.493`
- `market_context_high->commodity_1h` score `-0.4662` n `33` status `ready` deltaP `4.6952` edge `-0.0405` maxDD `-2.0455`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
