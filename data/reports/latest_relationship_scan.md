# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T22:37:33.191190+00:00`
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

- `news_risk_high->unknown_24h` score `45.2607` n `51` status `ready` deltaP `8.8542` edge `3.7127` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.6088` n `53` status `ready` deltaP `24.3701` edge `0.8982` maxDD `-0.1281`
- `news_risk_high->equity_24h` score `7.2333` n `51` status `ready` deltaP `29.9939` edge `0.4959` maxDD `-4.7801`
- `news_risk_high->index_24h` score `3.9908` n `51` status `ready` deltaP `40.2676` edge `0.0793` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.2461` n `53` status `ready` deltaP `16.3117` edge `0.1973` maxDD `-0.8426`
- `news_risk_high->fx_4h` score `3.0016` n `53` status `ready` deltaP `35.7254` edge `0.0254` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `2.6502` n `133` status `ready` deltaP `22.5117` edge `0.1116` maxDD `-0.5994`
- `news_risk_high->crypto_alt_24h` score `2.293` n `51` status `ready` deltaP `25.3472` edge `0.0221` maxDD `0.0`
- `news_risk_high->equity_4h` score `1.4782` n `53` status `ready` deltaP `18.3646` edge `0.0778` maxDD `-2.164`
- `news_risk_high->fx_1h` score `1.1644` n `53` status `ready` deltaP `16.0688` edge `0.0069` maxDD `-0.0257`
- `news_risk_high->metal_24h` score `0.5223` n `51` status `ready` deltaP `26.8586` edge `-0.1313` maxDD `-0.0053`
- `news_risk_high->commodity_1h` score `0.4619` n `53` status `ready` deltaP `11.1259` edge `-0.0044` maxDD `-0.5024`
- `news_risk_high->equity_1h` score `0.3897` n `53` status `ready` deltaP `12.7754` edge `0.0012` maxDD `-0.9128`
- `market_context_high->unknown_1h` score `0.2286` n `133` status `ready` deltaP `11.8713` edge `-0.0152` maxDD `-1.5916`
- `news_risk_high->index_4h` score `0.0443` n `53` status `ready` deltaP `5.8991` edge `0.0041` maxDD `-0.1788`
- `news_risk_high->index_1h` score `-0.0924` n `53` status `ready` deltaP `3.5505` edge `-0.0002` maxDD `-0.1583`
- `market_context_high->unknown_24h` score `-0.3465` n `125` status `ready` deltaP `8.8542` edge `-0.0879` maxDD `0.0`
- `market_context_high->fx_1h` score `-0.4343` n `133` status `ready` deltaP `2.6485` edge `-0.0001` maxDD `-0.8587`
- `news_risk_high->metal_1h` score `-0.5948` n `53` status `ready` deltaP `-2.1099` edge `-0.0129` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.7479` n `53` status `ready` deltaP `2.833` edge `-0.0281` maxDD `-0.249`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
