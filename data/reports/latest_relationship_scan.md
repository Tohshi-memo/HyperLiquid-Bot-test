# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T13:52:28.671435+00:00`
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

- `news_risk_high->unknown_24h` score `43.7678` n `51` status `ready` deltaP `2.7778` edge `3.6288` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.6476` n `52` status `ready` deltaP `24.6599` edge `0.8946` maxDD `-0.0695`
- `news_risk_high->equity_24h` score `9.0486` n `51` status `ready` deltaP `34.1606` edge `0.6194` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.3793` n `51` status `ready` deltaP `43.2189` edge `0.092` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.0878` n `53` status `ready` deltaP `16.162` edge `0.1851` maxDD `-0.8426`
- `news_risk_high->fx_4h` score `3.0457` n `52` status `ready` deltaP `36.0812` edge `0.0267` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `2.1551` n `133` status `ready` deltaP `20.9873` edge `0.0805` maxDD `-0.5994`
- `news_risk_high->equity_4h` score `2.0892` n `52` status `ready` deltaP `21.8926` edge `0.1052` maxDD `-2.164`
- `news_risk_high->fx_1h` score `1.1632` n `53` status `ready` deltaP `16.0688` edge `0.0068` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.5837` n `53` status `ready` deltaP `14.8712` edge `0.0121` maxDD `-0.9128`
- `news_risk_high->commodity_1h` score `0.3661` n `53` status `ready` deltaP `10.2277` edge `-0.0064` maxDD `-0.5024`
- `news_risk_high->index_4h` score `0.3578` n `52` status `ready` deltaP `9.1581` edge `0.0085` maxDD `-0.1788`
- `market_context_high->unknown_1h` score `0.0702` n `133` status `ready` deltaP `11.7216` edge `-0.0274` maxDD `-1.5916`
- `news_risk_high->index_1h` score `-0.0371` n `53` status `ready` deltaP `4.4487` edge `0.0009` maxDD `-0.1583`
- `news_risk_high->metal_1h` score `-0.3192` n `53` status `ready` deltaP `0.5847` edge `-0.0079` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.3398` n `52` status `ready` deltaP `6.1797` edge `-0.0164` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.4351` n `133` status `ready` deltaP `2.6485` edge `-0.0002` maxDD `-0.8587`
- `news_risk_high->metal_24h` score `-0.578` n `51` status `ready` deltaP `22.3448` edge `-0.1929` maxDD `-0.0053`
- `market_context_high->metal_4h` score `-0.7801` n `133` status `ready` deltaP `5.7893` edge `-0.0399` maxDD `-2.4293`
- `market_context_high->index_1h` score `-1.1999` n `133` status `ready` deltaP `-5.9216` edge `-0.0067` maxDD `-1.3054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
