# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T19:52:39.277033+00:00`
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

- `news_risk_high->unknown_24h` score `44.694` n `51` status `ready` deltaP `6.9444` edge `3.6782` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.574` n `53` status `ready` deltaP `24.3701` edge `0.8953` maxDD `-0.1281`
- `news_risk_high->equity_24h` score `7.5861` n `51` status `ready` deltaP `29.9939` edge `0.5253` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.0352` n `51` status `ready` deltaP `40.2676` edge `0.083` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.1694` n `53` status `ready` deltaP `16.0123` edge `0.1929` maxDD `-0.8426`
- `news_risk_high->fx_4h` score `3.0514` n `53` status `ready` deltaP `36.1827` edge `0.0265` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `2.6154` n `133` status `ready` deltaP `22.5117` edge `0.1087` maxDD `-0.5994`
- `news_risk_high->equity_4h` score `1.5655` n `53` status `ready` deltaP `19.1268` edge `0.08` maxDD `-2.164`
- `news_risk_high->fx_1h` score `1.1644` n `53` status `ready` deltaP `16.0688` edge `0.0069` maxDD `-0.0257`
- `news_risk_high->crypto_alt_24h` score `0.4794` n `51` status `ready` deltaP `23.4375` edge `-0.1163` maxDD `0.0`
- `news_risk_high->equity_1h` score `0.4598` n `53` status `ready` deltaP `13.6736` edge `0.0042` maxDD `-0.9128`
- `news_risk_high->commodity_1h` score `0.4092` n `53` status `ready` deltaP `10.6768` edge `-0.0058` maxDD `-0.5024`
- `news_risk_high->index_4h` score `0.1745` n `53` status `ready` deltaP `7.2711` edge `0.0058` maxDD `-0.1788`
- `market_context_high->unknown_1h` score `0.1518` n `133` status `ready` deltaP `11.5719` edge `-0.0196` maxDD `-1.5916`
- `news_risk_high->metal_24h` score `0.1256` n `51` status `ready` deltaP `25.4698` edge `-0.1551` maxDD `-0.0053`
- `news_risk_high->index_1h` score `-0.0737` n `53` status `ready` deltaP `3.8499` edge `0.0002` maxDD `-0.1583`
- `market_context_high->fx_1h` score `-0.4343` n `133` status `ready` deltaP `2.6485` edge `-0.0001` maxDD `-0.8587`
- `news_risk_high->metal_1h` score `-0.5421` n `53` status `ready` deltaP `-1.5111` edge `-0.0125` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.6725` n `53` status `ready` deltaP `3.5952` edge `-0.0269` maxDD `-0.249`
- `market_context_high->unknown_24h` score `-0.9132` n `125` status `ready` deltaP `6.9444` edge `-0.1224` maxDD `0.0`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
