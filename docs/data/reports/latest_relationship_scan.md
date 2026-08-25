# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T20:08:18.807676+00:00`
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

- `news_risk_high->unknown_24h` score `44.7414` n `51` status `ready` deltaP `7.1181` edge `3.681` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.574` n `53` status `ready` deltaP `24.3701` edge `0.8953` maxDD `-0.1281`
- `news_risk_high->equity_24h` score `7.5453` n `51` status `ready` deltaP `29.9939` edge `0.5219` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.0292` n `51` status `ready` deltaP `40.2676` edge `0.0825` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.1886` n `53` status `ready` deltaP `16.162` edge `0.1935` maxDD `-0.8426`
- `news_risk_high->fx_4h` score `3.0514` n `53` status `ready` deltaP `36.1827` edge `0.0265` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `2.6154` n `133` status `ready` deltaP `22.5117` edge `0.1087` maxDD `-0.5994`
- `news_risk_high->equity_4h` score `1.5402` n `53` status `ready` deltaP `18.9744` edge `0.0789` maxDD `-2.164`
- `news_risk_high->fx_1h` score `1.1764` n `53` status `ready` deltaP `16.2185` edge `0.0069` maxDD `-0.0257`
- `news_risk_high->crypto_alt_24h` score `0.5953` n `51` status `ready` deltaP `23.6111` edge `-0.1078` maxDD `0.0`
- `news_risk_high->equity_1h` score `0.4497` n `53` status `ready` deltaP `13.5239` edge `0.0039` maxDD `-0.9128`
- `news_risk_high->commodity_1h` score `0.4272` n `53` status `ready` deltaP `10.8265` edge `-0.0053` maxDD `-0.5024`
- `market_context_high->unknown_1h` score `0.171` n `133` status `ready` deltaP `11.7216` edge `-0.019` maxDD `-1.5916`
- `news_risk_high->index_4h` score `0.1599` n `53` status `ready` deltaP `7.1186` edge `0.0056` maxDD `-0.1788`
- `news_risk_high->metal_24h` score `0.1484` n `51` status `ready` deltaP `25.4698` edge `-0.1532` maxDD `-0.0053`
- `news_risk_high->index_1h` score `-0.0745` n `53` status `ready` deltaP `3.8499` edge `0.0001` maxDD `-0.1583`
- `market_context_high->fx_1h` score `-0.4265` n `133` status `ready` deltaP `2.7982` edge `-0.0001` maxDD `-0.8587`
- `news_risk_high->metal_1h` score `-0.5553` n `53` status `ready` deltaP `-1.6608` edge `-0.0126` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.6883` n `53` status `ready` deltaP `3.4428` edge `-0.0272` maxDD `-0.249`
- `market_context_high->unknown_24h` score `-0.8658` n `125` status `ready` deltaP `7.1181` edge `-0.1196` maxDD `0.0`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
