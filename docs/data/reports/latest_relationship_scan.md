# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T20:16:37.408062+00:00`
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

- `news_risk_high->unknown_24h` score `44.7841` n `51` status `ready` deltaP `7.2917` edge `3.6834` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.5752` n `53` status `ready` deltaP `24.3701` edge `0.8954` maxDD `-0.1281`
- `news_risk_high->equity_24h` score `7.5021` n `51` status `ready` deltaP `29.9939` edge `0.5183` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.0244` n `51` status `ready` deltaP `40.2676` edge `0.0821` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.2065` n `53` status `ready` deltaP `16.3117` edge `0.194` maxDD `-0.8426`
- `news_risk_high->fx_4h` score `3.038` n `53` status `ready` deltaP `36.0303` edge `0.0264` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `2.6166` n `133` status `ready` deltaP `22.5117` edge `0.1088` maxDD `-0.5994`
- `news_risk_high->equity_4h` score `1.5136` n `53` status `ready` deltaP `18.8219` edge `0.0777` maxDD `-2.164`
- `news_risk_high->fx_1h` score `1.1884` n `53` status `ready` deltaP `16.3682` edge `0.0069` maxDD `-0.0257`
- `news_risk_high->crypto_alt_24h` score `0.7112` n `51` status `ready` deltaP `23.7847` edge `-0.0993` maxDD `0.0`
- `news_risk_high->commodity_1h` score `0.4463` n `53` status `ready` deltaP `10.9762` edge `-0.0047` maxDD `-0.5024`
- `news_risk_high->equity_1h` score `0.4388` n `53` status `ready` deltaP `13.3742` edge `0.0035` maxDD `-0.9128`
- `market_context_high->unknown_1h` score `0.189` n `133` status `ready` deltaP `11.8713` edge `-0.0185` maxDD `-1.5916`
- `news_risk_high->metal_24h` score `0.1712` n `51` status `ready` deltaP `25.4698` edge `-0.1513` maxDD `-0.0053`
- `news_risk_high->index_4h` score `0.1441` n `53` status `ready` deltaP `6.9662` edge `0.0053` maxDD `-0.1788`
- `news_risk_high->index_1h` score `-0.0745` n `53` status `ready` deltaP `3.8499` edge `0.0001` maxDD `-0.1583`
- `market_context_high->fx_1h` score `-0.4187` n `133` status `ready` deltaP `2.9479` edge `-0.0001` maxDD `-0.8587`
- `news_risk_high->metal_1h` score `-0.5553` n `53` status `ready` deltaP `-1.6608` edge `-0.0126` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.7029` n `53` status `ready` deltaP `3.2904` edge `-0.0274` maxDD `-0.249`
- `market_context_high->unknown_24h` score `-0.8231` n `125` status `ready` deltaP `7.2917` edge `-0.1172` maxDD `0.0`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
