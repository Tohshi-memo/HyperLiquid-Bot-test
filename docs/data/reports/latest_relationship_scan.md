# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T23:34:48.765954+00:00`
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

- `news_risk_high->unknown_24h` score `45.4771` n `51` status `ready` deltaP `9.5486` edge `3.7261` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.6476` n `53` status `ready` deltaP `24.675` edge `0.8994` maxDD `-0.1281`
- `news_risk_high->equity_24h` score `7.1565` n `51` status `ready` deltaP `29.9939` edge `0.4895` maxDD `-4.7801`
- `news_risk_high->index_24h` score `3.9836` n `51` status `ready` deltaP `40.2676` edge `0.0787` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.2258` n `53` status `ready` deltaP `16.162` edge `0.1966` maxDD `-0.8426`
- `news_risk_high->fx_4h` score `2.9665` n `53` status `ready` deltaP `35.4205` edge `0.0245` maxDD `-0.0746`
- `news_risk_high->crypto_alt_24h` score `2.9221` n `51` status `ready` deltaP `26.0417` edge `0.0699` maxDD `0.0`
- `market_context_high->unknown_4h` score `2.689` n `133` status `ready` deltaP `22.8166` edge `0.1128` maxDD `-0.5994`
- `news_risk_high->equity_4h` score `1.4938` n `53` status `ready` deltaP `18.3646` edge `0.0791` maxDD `-2.164`
- `news_risk_high->fx_1h` score `1.1381` n `53` status `ready` deltaP `15.7694` edge `0.0067` maxDD `-0.0257`
- `news_risk_high->metal_24h` score `0.6955` n `51` status `ready` deltaP `27.5531` edge `-0.1215` maxDD `-0.0053`
- `news_risk_high->commodity_1h` score `0.4631` n `53` status `ready` deltaP `11.1259` edge `-0.0043` maxDD `-0.5024`
- `news_risk_high->equity_1h` score `0.3733` n `53` status `ready` deltaP `12.6257` edge `0.0001` maxDD `-0.9128`
- `market_context_high->unknown_1h` score `0.2082` n `133` status `ready` deltaP `11.7216` edge `-0.0159` maxDD `-1.5916`
- `news_risk_high->index_4h` score `-0.0105` n `53` status `ready` deltaP `5.2894` edge `0.0036` maxDD `-0.1788`
- `news_risk_high->index_1h` score `-0.0869` n `53` status `ready` deltaP `3.7002` edge `-0.0005` maxDD `-0.1583`
- `market_context_high->unknown_24h` score `-0.1301` n `125` status `ready` deltaP `9.5486` edge `-0.0745` maxDD `0.0`
- `market_context_high->fx_1h` score `-0.4514` n `133` status `ready` deltaP `2.3491` edge `-0.0003` maxDD `-0.8587`
- `news_risk_high->metal_1h` score `-0.5936` n `53` status `ready` deltaP `-2.1099` edge `-0.0128` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.7187` n `53` status `ready` deltaP `3.1379` edge `-0.0277` maxDD `-0.249`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
