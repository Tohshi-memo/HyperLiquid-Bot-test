# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T00:22:27.560134+00:00`
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

- `news_risk_high->unknown_24h` score `45.64` n `51` status `ready` deltaP `10.0694` edge `3.7362` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.7238` n `53` status `ready` deltaP `25.1323` edge `0.9027` maxDD `-0.1281`
- `news_risk_high->equity_24h` score `7.1097` n `51` status `ready` deltaP `29.9939` edge `0.4856` maxDD `-4.7801`
- `news_risk_high->index_24h` score `3.98` n `51` status `ready` deltaP `40.2676` edge `0.0784` maxDD `-0.2147`
- `news_risk_high->crypto_alt_24h` score `3.4534` n `51` status `ready` deltaP `26.5625` edge `0.1107` maxDD `0.0`
- `news_risk_high->unknown_1h` score `3.3937` n `53` status `ready` deltaP `16.6111` edge `0.2076` maxDD `-0.8426`
- `news_risk_high->fx_4h` score `2.9337` n `53` status `ready` deltaP `35.1157` edge `0.0238` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `2.7652` n `133` status `ready` deltaP `23.2739` edge `0.1161` maxDD `-0.5994`
- `news_risk_high->equity_4h` score `1.5664` n `53` status `ready` deltaP `18.8219` edge `0.0821` maxDD `-2.164`
- `news_risk_high->fx_1h` score `1.1117` n `53` status `ready` deltaP `15.47` edge `0.0065` maxDD `-0.0257`
- `news_risk_high->metal_24h` score `0.8283` n `51` status `ready` deltaP `28.0739` edge `-0.1139` maxDD `-0.0053`
- `news_risk_high->commodity_1h` score `0.4895` n `53` status `ready` deltaP `11.4253` edge `-0.0041` maxDD `-0.5024`
- `news_risk_high->equity_1h` score `0.4263` n `53` status `ready` deltaP `13.0748` edge `0.0039` maxDD `-0.9128`
- `market_context_high->unknown_1h` score `0.3761` n `133` status `ready` deltaP `12.1707` edge `-0.0049` maxDD `-1.5916`
- `market_context_high->unknown_24h` score `0.0328` n `125` status `ready` deltaP `10.0694` edge `-0.0644` maxDD `0.0`
- `news_risk_high->index_4h` score `0.0053` n `53` status `ready` deltaP `5.4418` edge `0.0039` maxDD `-0.1788`
- `news_risk_high->index_1h` score `-0.0659` n `53` status `ready` deltaP `3.9996` edge `0.0002` maxDD `-0.1583`
- `market_context_high->fx_1h` score `-0.4685` n `133` status `ready` deltaP `2.0497` edge `-0.0005` maxDD `-0.8587`
- `news_risk_high->metal_1h` score `-0.566` n `53` status `ready` deltaP `-1.8105` edge `-0.0125` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.6749` n `53` status `ready` deltaP `3.5952` edge `-0.0271` maxDD `-0.249`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
