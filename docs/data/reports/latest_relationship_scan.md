# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T12:37:27.666978+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14760`

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

- `news_risk_high->unknown_24h` score `43.6259` n `51` status `ready` deltaP `2.0833` edge `3.6216` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.5098` n `52` status `ready` deltaP `23.8977` edge `0.8882` maxDD `-0.0695`
- `news_risk_high->equity_24h` score `9.3617` n `51` status `ready` deltaP `35.0286` edge `0.6397` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.4788` n `51` status `ready` deltaP `44.087` edge `0.0945` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.0842` n `53` status `ready` deltaP `16.162` edge `0.1848` maxDD `-0.8426`
- `news_risk_high->fx_4h` score `3.0445` n `52` status `ready` deltaP `36.0812` edge `0.0266` maxDD `-0.0746`
- `news_risk_high->equity_4h` score `2.2384` n `52` status `ready` deltaP `22.1975` edge `0.1156` maxDD `-2.164`
- `market_context_high->unknown_4h` score `2.0173` n `133` status `ready` deltaP `20.2251` edge `0.0741` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.1644` n `53` status `ready` deltaP `16.0688` edge `0.0069` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.6414` n `53` status `ready` deltaP `15.1706` edge `0.0175` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.3868` n `52` status `ready` deltaP `9.3105` edge `0.0099` maxDD `-0.1788`
- `news_risk_high->commodity_1h` score `0.3673` n `53` status `ready` deltaP `10.2277` edge `-0.0063` maxDD `-0.5024`
- `market_context_high->unknown_1h` score `0.0666` n `133` status `ready` deltaP `11.7216` edge `-0.0277` maxDD `-1.5916`
- `news_risk_high->index_1h` score `-0.0184` n `53` status `ready` deltaP `4.7481` edge `0.0013` maxDD `-0.1583`
- `news_risk_high->metal_4h` score `-0.306` n `52` status `ready` deltaP `6.3321` edge `-0.0146` maxDD `-0.249`
- `news_risk_high->metal_1h` score `-0.3192` n `53` status `ready` deltaP `0.5847` edge `-0.0079` maxDD `-0.1413`
- `market_context_high->fx_1h` score `-0.4343` n `133` status `ready` deltaP `2.6485` edge `-0.0001` maxDD `-0.8587`
- `news_risk_high->metal_24h` score `-0.6972` n `51` status `ready` deltaP `21.6503` edge `-0.1982` maxDD `-0.0053`
- `market_context_high->metal_4h` score `-0.7463` n `133` status `ready` deltaP `5.9417` edge `-0.0381` maxDD `-2.4293`
- `market_context_high->index_1h` score `-1.1712` n `133` status `ready` deltaP `-5.6222` edge `-0.0063` maxDD `-1.3054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
