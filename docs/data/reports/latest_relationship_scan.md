# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T01:37:24.040842+00:00`
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

- `news_risk_high->unknown_24h` score `45.9098` n `51` status `ready` deltaP `10.9375` edge `3.7529` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.685` n `53` status `ready` deltaP `24.8274` edge `0.9015` maxDD `-0.1281`
- `news_risk_high->equity_24h` score `7.0593` n `51` status `ready` deltaP `29.9939` edge `0.4814` maxDD `-4.7801`
- `news_risk_high->crypto_alt_24h` score `4.3448` n `51` status `ready` deltaP `27.4306` edge `0.1792` maxDD `0.0`
- `news_risk_high->index_24h` score `3.9836` n `51` status `ready` deltaP `40.2676` edge `0.0787` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.3817` n `53` status `ready` deltaP `16.4614` edge `0.2076` maxDD `-0.8426`
- `news_risk_high->fx_4h` score `2.8607` n `53` status `ready` deltaP `34.3535` edge `0.0228` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `2.7264` n `133` status `ready` deltaP `22.969` edge `0.1149` maxDD `-0.5994`
- `news_risk_high->equity_4h` score `1.5846` n `53` status `ready` deltaP `18.9744` edge `0.0826` maxDD `-2.164`
- `news_risk_high->fx_1h` score `1.0722` n `53` status `ready` deltaP `15.0209` edge `0.0062` maxDD `-0.0257`
- `news_risk_high->metal_24h` score `1.0382` n `51` status `ready` deltaP `28.942` edge `-0.1022` maxDD `-0.0053`
- `news_risk_high->commodity_1h` score `0.5194` n `53` status `ready` deltaP `11.7247` edge `-0.0036` maxDD `-0.5024`
- `news_risk_high->equity_1h` score `0.4809` n `53` status `ready` deltaP `13.5239` edge `0.0079` maxDD `-0.9128`
- `market_context_high->unknown_1h` score `0.3641` n `133` status `ready` deltaP `12.021` edge `-0.0049` maxDD `-1.5916`
- `news_risk_high->index_4h` score `0.0077` n `53` status `ready` deltaP `5.4418` edge `0.0041` maxDD `-0.1788`
- `news_risk_high->index_1h` score `-0.0488` n `53` status `ready` deltaP `4.299` edge `0.0004` maxDD `-0.1583`
- `market_context_high->fx_1h` score `-0.4942` n `133` status `ready` deltaP `1.6006` edge `-0.0008` maxDD `-0.8587`
- `news_risk_high->metal_1h` score `-0.5361` n `53` status `ready` deltaP `-1.5111` edge `-0.012` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.6883` n `53` status `ready` deltaP `3.4428` edge `-0.0272` maxDD `-0.249`
- `news_risk_high->commodity_4h` score `-1.0734` n `53` status `ready` deltaP `-2.4304` edge `0.0019` maxDD `-1.1986`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
