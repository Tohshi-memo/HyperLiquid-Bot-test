# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T12:52:24.093457+00:00`
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

- `news_risk_high->unknown_24h` score `43.6331` n `51` status `ready` deltaP `2.0833` edge `3.6222` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.522` n `52` status `ready` deltaP `24.0501` edge `0.8882` maxDD `-0.0695`
- `news_risk_high->equity_24h` score `9.3238` n `51` status `ready` deltaP `34.855` edge `0.6377` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.4613` n `51` status `ready` deltaP `43.9134` edge `0.0942` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.0818` n `53` status `ready` deltaP `16.162` edge `0.1846` maxDD `-0.8426`
- `news_risk_high->fx_4h` score `3.0579` n `52` status `ready` deltaP `36.2336` edge `0.0267` maxDD `-0.0746`
- `news_risk_high->equity_4h` score `2.1998` n `52` status `ready` deltaP `22.0451` edge `0.1134` maxDD `-2.164`
- `market_context_high->unknown_4h` score `2.0295` n `133` status `ready` deltaP `20.3775` edge `0.0741` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.1644` n `53` status `ready` deltaP `16.0688` edge `0.0069` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.6359` n `53` status `ready` deltaP `15.1706` edge `0.0168` maxDD `-0.9128`
- `news_risk_high->commodity_1h` score `0.3828` n `53` status `ready` deltaP `10.3774` edge `-0.006` maxDD `-0.5024`
- `news_risk_high->index_4h` score `0.371` n `52` status `ready` deltaP `9.1581` edge `0.0096` maxDD `-0.1788`
- `market_context_high->unknown_1h` score `0.0642` n `133` status `ready` deltaP `11.7216` edge `-0.0279` maxDD `-1.5916`
- `news_risk_high->index_1h` score `-0.0184` n `53` status `ready` deltaP `4.7481` edge `0.0013` maxDD `-0.1583`
- `news_risk_high->metal_1h` score `-0.3216` n `53` status `ready` deltaP `0.5847` edge `-0.0081` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.3266` n `52` status `ready` deltaP `6.1797` edge `-0.0153` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.4343` n `133` status `ready` deltaP `2.6485` edge `-0.0001` maxDD `-0.8587`
- `news_risk_high->metal_24h` score `-0.6924` n `51` status `ready` deltaP `21.6503` edge `-0.1978` maxDD `-0.0053`
- `market_context_high->metal_4h` score `-0.7669` n `133` status `ready` deltaP `5.7893` edge `-0.0388` maxDD `-2.4293`
- `market_context_high->index_1h` score `-1.1712` n `133` status `ready` deltaP `-5.6222` edge `-0.0063` maxDD `-1.3054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
