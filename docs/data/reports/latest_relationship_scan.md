# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T13:07:25.203186+00:00`
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

- `news_risk_high->unknown_24h` score `43.6674` n `51` status `ready` deltaP `2.2569` edge `3.6239` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.5366` n `52` status `ready` deltaP `24.2026` edge `0.8884` maxDD `-0.0695`
- `news_risk_high->equity_24h` score `9.2859` n `51` status `ready` deltaP `34.6814` edge `0.6357` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.4438` n `51` status `ready` deltaP `43.7398` edge `0.0939` maxDD `-0.2147`
- `news_risk_high->fx_4h` score `3.0713` n `52` status `ready` deltaP `36.3861` edge `0.0268` maxDD `-0.0746`
- `news_risk_high->unknown_1h` score `3.0674` n `53` status `ready` deltaP `16.0123` edge `0.1844` maxDD `-0.8426`
- `news_risk_high->equity_4h` score `2.1782` n `52` status `ready` deltaP `22.0451` edge `0.1116` maxDD `-2.164`
- `market_context_high->unknown_4h` score `2.0441` n `133` status `ready` deltaP `20.53` edge `0.0743` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.1644` n `53` status `ready` deltaP `16.0688` edge `0.0069` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.632` n `53` status `ready` deltaP `15.1706` edge `0.0163` maxDD `-0.9128`
- `news_risk_high->commodity_1h` score `0.3828` n `53` status `ready` deltaP `10.3774` edge `-0.006` maxDD `-0.5024`
- `news_risk_high->index_4h` score `0.3674` n `52` status `ready` deltaP `9.1581` edge `0.0093` maxDD `-0.1788`
- `market_context_high->unknown_1h` score `0.0498` n `133` status `ready` deltaP `11.5719` edge `-0.0281` maxDD `-1.5916`
- `news_risk_high->index_1h` score `-0.0184` n `53` status `ready` deltaP `4.7481` edge `0.0013` maxDD `-0.1583`
- `news_risk_high->metal_1h` score `-0.3204` n `53` status `ready` deltaP `0.5847` edge `-0.008` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.3326` n `52` status `ready` deltaP `6.1797` edge `-0.0158` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.4343` n `133` status `ready` deltaP `2.6485` edge `-0.0001` maxDD `-0.8587`
- `news_risk_high->metal_24h` score `-0.6677` n `51` status `ready` deltaP `21.8239` edge `-0.1969` maxDD `-0.0053`
- `market_context_high->metal_4h` score `-0.7729` n `133` status `ready` deltaP `5.7893` edge `-0.0393` maxDD `-2.4293`
- `market_context_high->index_1h` score `-1.1712` n `133` status `ready` deltaP `-5.6222` edge `-0.0063` maxDD `-1.3054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
