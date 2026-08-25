# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T12:22:31.832731+00:00`
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

- `news_risk_high->unknown_24h` score `43.6199` n `51` status `ready` deltaP `2.0833` edge `3.6211` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.5086` n `52` status `ready` deltaP `23.8977` edge `0.8881` maxDD `-0.0695`
- `news_risk_high->equity_24h` score `9.4104` n `51` status `ready` deltaP `35.2022` edge `0.6426` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.4974` n `51` status `ready` deltaP `44.2606` edge `0.0949` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.083` n `53` status `ready` deltaP `16.162` edge `0.1847` maxDD `-0.8426`
- `news_risk_high->fx_4h` score `3.0311` n `52` status `ready` deltaP `35.9287` edge `0.0265` maxDD `-0.0746`
- `news_risk_high->equity_4h` score `2.277` n `52` status `ready` deltaP `22.3499` edge `0.1178` maxDD `-2.164`
- `market_context_high->unknown_4h` score `2.0161` n `133` status `ready` deltaP `20.2251` edge `0.074` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.1513` n `53` status `ready` deltaP `15.9191` edge `0.0068` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.6398` n `53` status `ready` deltaP `15.1706` edge `0.0173` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.4038` n `52` status `ready` deltaP `9.463` edge `0.0103` maxDD `-0.1788`
- `news_risk_high->commodity_1h` score `0.3517` n `53` status `ready` deltaP `10.078` edge `-0.0066` maxDD `-0.5024`
- `market_context_high->unknown_1h` score `0.0654` n `133` status `ready` deltaP `11.7216` edge `-0.0278` maxDD `-1.5916`
- `news_risk_high->index_1h` score `-0.0262` n `53` status `ready` deltaP `4.5984` edge `0.0013` maxDD `-0.1583`
- `news_risk_high->metal_4h` score `-0.3` n `52` status `ready` deltaP `6.3321` edge `-0.0141` maxDD `-0.249`
- `news_risk_high->metal_1h` score `-0.3204` n `53` status `ready` deltaP `0.5847` edge `-0.008` maxDD `-0.1413`
- `market_context_high->fx_1h` score `-0.4428` n `133` status `ready` deltaP `2.4988` edge `-0.0002` maxDD `-0.8587`
- `news_risk_high->metal_24h` score `-0.7008` n `51` status `ready` deltaP `21.6503` edge `-0.1985` maxDD `-0.0053`
- `market_context_high->metal_4h` score `-0.7403` n `133` status `ready` deltaP `5.9417` edge `-0.0376` maxDD `-2.4293`
- `market_context_high->index_1h` score `-1.1832` n `133` status `ready` deltaP `-5.7719` edge `-0.0063` maxDD `-1.3054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
