# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T00:37:25.300503+00:00`
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

- `news_risk_high->unknown_24h` score `45.6946` n `51` status `ready` deltaP `10.2431` edge `3.7396` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.748` n `53` status `ready` deltaP `25.2847` edge `0.9037` maxDD `-0.1281`
- `news_risk_high->equity_24h` score `7.1013` n `51` status `ready` deltaP `29.9939` edge `0.4849` maxDD `-4.7801`
- `news_risk_high->index_24h` score `3.98` n `51` status `ready` deltaP `40.2676` edge `0.0784` maxDD `-0.2147`
- `news_risk_high->crypto_alt_24h` score `3.6413` n `51` status `ready` deltaP `26.7361` edge `0.1252` maxDD `0.0`
- `news_risk_high->unknown_1h` score `3.4201` n `53` status `ready` deltaP `16.7608` edge `0.2088` maxDD `-0.8426`
- `news_risk_high->fx_4h` score `2.9191` n `53` status `ready` deltaP `34.9632` edge `0.0236` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `2.7894` n `133` status `ready` deltaP `23.4263` edge `0.1171` maxDD `-0.5994`
- `news_risk_high->equity_4h` score `1.5894` n `53` status `ready` deltaP `18.9744` edge `0.083` maxDD `-2.164`
- `news_risk_high->fx_1h` score `1.0986` n `53` status `ready` deltaP `15.3203` edge `0.0064` maxDD `-0.0257`
- `news_risk_high->metal_24h` score `0.8746` n `51` status `ready` deltaP `28.2475` edge `-0.1112` maxDD `-0.0053`
- `news_risk_high->commodity_1h` score `0.4895` n `53` status `ready` deltaP `11.4253` edge `-0.0041` maxDD `-0.5024`
- `news_risk_high->equity_1h` score `0.4466` n `53` status `ready` deltaP `13.2245` edge `0.0055` maxDD `-0.9128`
- `market_context_high->unknown_1h` score `0.4025` n `133` status `ready` deltaP `12.3204` edge `-0.0037` maxDD `-1.5916`
- `news_risk_high->index_4h` score `0.0077` n `53` status `ready` deltaP `5.4418` edge `0.0041` maxDD `-0.1788`
- `news_risk_high->index_1h` score `-0.0558` n `53` status `ready` deltaP `4.1493` edge `0.0005` maxDD `-0.1583`
- `market_context_high->unknown_24h` score `-0.3795` n `126` status `ready` deltaP `9.4494` edge `-0.0844` maxDD `-0.4842`
- `market_context_high->fx_1h` score `-0.4771` n `133` status `ready` deltaP `1.9` edge `-0.0006` maxDD `-0.8587`
- `news_risk_high->metal_1h` score `-0.5517` n `53` status `ready` deltaP `-1.6608` edge `-0.0123` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.6737` n `53` status `ready` deltaP `3.5952` edge `-0.027` maxDD `-0.249`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
