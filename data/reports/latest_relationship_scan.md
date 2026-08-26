# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T02:37:32.897695+00:00`
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

- `news_risk_high->unknown_24h` score `46.1262` n `51` status `ready` deltaP `11.6319` edge `3.7663` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.6292` n `53` status `ready` deltaP `24.3701` edge `0.8999` maxDD `-0.1281`
- `news_risk_high->equity_24h` score `7.0209` n `51` status `ready` deltaP `29.9939` edge `0.4782` maxDD `-4.7801`
- `news_risk_high->crypto_alt_24h` score `5.0592` n `51` status `ready` deltaP `28.125` edge `0.2341` maxDD `0.0`
- `news_risk_high->index_24h` score `3.9932` n `51` status `ready` deltaP `40.2676` edge `0.0795` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.3266` n `53` status `ready` deltaP `16.0123` edge `0.206` maxDD `-0.8426`
- `news_risk_high->fx_4h` score `2.8571` n `53` status `ready` deltaP `34.3535` edge `0.0225` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `2.6706` n `133` status `ready` deltaP `22.5117` edge `0.1133` maxDD `-0.5994`
- `news_risk_high->equity_4h` score `1.557` n `53` status `ready` deltaP `18.9744` edge `0.0803` maxDD `-2.164`
- `news_risk_high->metal_24h` score `1.1229` n `51` status `ready` deltaP `29.1156` edge `-0.0963` maxDD `-0.0053`
- `news_risk_high->fx_1h` score `1.071` n `53` status `ready` deltaP `15.0209` edge `0.0061` maxDD `-0.0257`
- `news_risk_high->commodity_1h` score `0.4943` n `53` status `ready` deltaP `11.4253` edge `-0.0037` maxDD `-0.5024`
- `news_risk_high->equity_1h` score `0.459` n `53` status `ready` deltaP `13.3742` edge `0.0061` maxDD `-0.9128`
- `market_context_high->unknown_1h` score `0.309` n `133` status `ready` deltaP `11.5719` edge `-0.0065` maxDD `-1.5916`
- `news_risk_high->index_4h` score `0.0077` n `53` status `ready` deltaP `5.4418` edge `0.0041` maxDD `-0.1788`
- `news_risk_high->index_1h` score `-0.0752` n `53` status `ready` deltaP `3.8499` edge `0.0` maxDD `-0.1583`
- `market_context_high->fx_1h` score `-0.495` n `133` status `ready` deltaP `1.6006` edge `-0.0009` maxDD `-0.8587`
- `news_risk_high->metal_1h` score `-0.5708` n `53` status `ready` deltaP `-1.8105` edge `-0.0129` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.7503` n `53` status `ready` deltaP `2.833` edge `-0.0283` maxDD `-0.249`
- `news_risk_high->commodity_4h` score `-1.0632` n `53` status `ready` deltaP `-2.278` edge `0.0022` maxDD `-1.1986`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
