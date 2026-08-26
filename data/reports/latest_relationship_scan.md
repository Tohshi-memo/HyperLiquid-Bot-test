# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T00:07:43.479673+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14792`

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

- `news_risk_high->unknown_24h` score `45.5865` n `51` status `ready` deltaP `9.8958` edge `3.7329` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.7008` n `53` status `ready` deltaP `24.9798` edge `0.9018` maxDD `-0.1281`
- `news_risk_high->equity_24h` score `7.1253` n `51` status `ready` deltaP `29.9939` edge `0.4869` maxDD `-4.7801`
- `news_risk_high->index_24h` score `3.98` n `51` status `ready` deltaP `40.2676` edge `0.0784` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.3661` n `53` status `ready` deltaP `16.4614` edge `0.2063` maxDD `-0.8426`
- `news_risk_high->crypto_alt_24h` score `3.2691` n `51` status `ready` deltaP `26.3889` edge `0.0965` maxDD `0.0`
- `news_risk_high->fx_4h` score `2.9483` n `53` status `ready` deltaP `35.2681` edge `0.024` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `2.7422` n `133` status `ready` deltaP `23.1214` edge `0.1152` maxDD `-0.5994`
- `news_risk_high->equity_4h` score `1.5422` n `53` status `ready` deltaP `18.6695` edge `0.0811` maxDD `-2.164`
- `news_risk_high->fx_1h` score `1.1237` n `53` status `ready` deltaP `15.6197` edge `0.0065` maxDD `-0.0257`
- `news_risk_high->metal_24h` score `0.7856` n `51` status `ready` deltaP `27.9003` edge `-0.1163` maxDD `-0.0053`
- `news_risk_high->commodity_1h` score `0.4763` n `53` status `ready` deltaP `11.2756` edge `-0.0042` maxDD `-0.5024`
- `news_risk_high->equity_1h` score `0.406` n `53` status `ready` deltaP `12.9251` edge `0.0023` maxDD `-0.9128`
- `market_context_high->unknown_1h` score `0.3485` n `133` status `ready` deltaP `12.021` edge `-0.0062` maxDD `-1.5916`
- `news_risk_high->index_4h` score `-0.0093` n `53` status `ready` deltaP `5.2894` edge `0.0037` maxDD `-0.1788`
- `market_context_high->unknown_24h` score `-0.0207` n `125` status `ready` deltaP `9.8958` edge `-0.0677` maxDD `0.0`
- `news_risk_high->index_1h` score `-0.076` n `53` status `ready` deltaP `3.8499` edge `-0.0001` maxDD `-0.1583`
- `market_context_high->fx_1h` score `-0.4608` n `133` status `ready` deltaP `2.1994` edge `-0.0005` maxDD `-0.8587`
- `news_risk_high->metal_1h` score `-0.5648` n `53` status `ready` deltaP `-1.8105` edge `-0.0124` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.6883` n `53` status `ready` deltaP `3.4428` edge `-0.0272` maxDD `-0.249`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
