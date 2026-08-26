# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T01:22:25.909949+00:00`
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

- `news_risk_high->unknown_24h` score `45.8551` n `51` status `ready` deltaP `10.7639` edge `3.7495` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.7032` n `53` status `ready` deltaP `24.9798` edge `0.902` maxDD `-0.1281`
- `news_risk_high->equity_24h` score `7.0737` n `51` status `ready` deltaP `29.9939` edge `0.4826` maxDD `-4.7801`
- `news_risk_high->crypto_alt_24h` score `4.1738` n `51` status `ready` deltaP `27.2569` edge `0.1661` maxDD `0.0`
- `news_risk_high->index_24h` score `3.9824` n `51` status `ready` deltaP `40.2676` edge `0.0786` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.4009` n `53` status `ready` deltaP `16.6111` edge `0.2082` maxDD `-0.8426`
- `news_risk_high->fx_4h` score `2.8753` n `53` status `ready` deltaP `34.5059` edge `0.023` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `2.7446` n `133` status `ready` deltaP `23.1214` edge `0.1154` maxDD `-0.5994`
- `news_risk_high->equity_4h` score `1.5894` n `53` status `ready` deltaP `18.9744` edge `0.083` maxDD `-2.164`
- `news_risk_high->fx_1h` score `1.0722` n `53` status `ready` deltaP `15.0209` edge `0.0062` maxDD `-0.0257`
- `news_risk_high->metal_24h` score `1.0003` n `51` status `ready` deltaP `28.7684` edge `-0.1042` maxDD `-0.0053`
- `news_risk_high->commodity_1h` score `0.5182` n `53` status `ready` deltaP `11.7247` edge `-0.0037` maxDD `-0.5024`
- `news_risk_high->equity_1h` score `0.484` n `53` status `ready` deltaP `13.5239` edge `0.0083` maxDD `-0.9128`
- `market_context_high->unknown_1h` score `0.3833` n `133` status `ready` deltaP `12.1707` edge `-0.0043` maxDD `-1.5916`
- `news_risk_high->index_4h` score `0.0077` n `53` status `ready` deltaP `5.4418` edge `0.0041` maxDD `-0.1788`
- `news_risk_high->index_1h` score `-0.048` n `53` status `ready` deltaP `4.299` edge `0.0005` maxDD `-0.1583`
- `market_context_high->fx_1h` score `-0.4942` n `133` status `ready` deltaP `1.6006` edge `-0.0008` maxDD `-0.8587`
- `news_risk_high->metal_1h` score `-0.5229` n `53` status `ready` deltaP `-1.3614` edge `-0.0119` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.6737` n `53` status `ready` deltaP `3.5952` edge `-0.027` maxDD `-0.249`
- `news_risk_high->commodity_4h` score `-1.0742` n `53` status `ready` deltaP `-2.4304` edge `0.0018` maxDD `-1.1986`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
