# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T20:38:05.480132+00:00`
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

- `news_risk_high->unknown_24h` score `44.8292` n `51` status `ready` deltaP `7.4653` edge `3.686` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.5776` n `53` status `ready` deltaP `24.3701` edge `0.8956` maxDD `-0.1281`
- `news_risk_high->equity_24h` score `7.4589` n `51` status `ready` deltaP `29.9939` edge `0.5147` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.0184` n `51` status `ready` deltaP `40.2676` edge `0.0816` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.2245` n `53` status `ready` deltaP `16.4614` edge `0.1945` maxDD `-0.8426`
- `news_risk_high->fx_4h` score `3.0258` n `53` status `ready` deltaP `35.8779` edge `0.0264` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `2.619` n `133` status `ready` deltaP `22.5117` edge `0.109` maxDD `-0.5994`
- `news_risk_high->equity_4h` score `1.4918` n `53` status `ready` deltaP `18.6695` edge `0.0769` maxDD `-2.164`
- `news_risk_high->fx_1h` score `1.1884` n `53` status `ready` deltaP `16.3682` edge `0.0069` maxDD `-0.0257`
- `news_risk_high->crypto_alt_24h` score `0.8403` n `51` status `ready` deltaP `23.9583` edge `-0.0897` maxDD `0.0`
- `news_risk_high->commodity_1h` score `0.4511` n `53` status `ready` deltaP `10.9762` edge `-0.0043` maxDD `-0.5024`
- `news_risk_high->equity_1h` score `0.4255` n `53` status `ready` deltaP `13.2245` edge `0.0028` maxDD `-0.9128`
- `market_context_high->unknown_1h` score `0.2069` n `133` status `ready` deltaP `12.021` edge `-0.018` maxDD `-1.5916`
- `news_risk_high->metal_24h` score `0.194` n `51` status `ready` deltaP `25.4698` edge `-0.1494` maxDD `-0.0053`
- `news_risk_high->index_4h` score `0.1295` n `53` status `ready` deltaP `6.8138` edge `0.0051` maxDD `-0.1788`
- `news_risk_high->index_1h` score `-0.0838` n `53` status `ready` deltaP `3.7002` edge `-0.0001` maxDD `-0.1583`
- `market_context_high->fx_1h` score `-0.4187` n `133` status `ready` deltaP `2.9479` edge `-0.0001` maxDD `-0.8587`
- `news_risk_high->metal_1h` score `-0.5672` n `53` status `ready` deltaP `-1.8105` edge `-0.0126` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.7175` n `53` status `ready` deltaP `3.1379` edge `-0.0276` maxDD `-0.249`
- `market_context_high->unknown_24h` score `-0.778` n `125` status `ready` deltaP `7.4653` edge `-0.1146` maxDD `0.0`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
