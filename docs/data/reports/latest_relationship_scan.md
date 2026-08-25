# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T10:52:27.227088+00:00`
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

- `news_risk_high->unknown_24h` score `43.6314` n `51` status `ready` deltaP `2.2569` edge `3.6209` maxDD `0.0`
- `news_risk_high->unknown_4h` score `13.0126` n `51` status `ready` deltaP `25.7831` edge `0.9171` maxDD `-0.0348`
- `news_risk_high->equity_24h` score `9.8261` n `51` status `ready` deltaP `36.2439` edge `0.6703` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.6264` n `51` status `ready` deltaP `45.3023` edge `0.0987` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.1499` n `52` status `ready` deltaP `15.9488` edge `0.1917` maxDD `-0.8426`
- `news_risk_high->fx_4h` score `3.1021` n `51` status `ready` deltaP `36.7109` edge `0.0272` maxDD `-0.0746`
- `news_risk_high->equity_4h` score `2.4412` n `51` status `ready` deltaP `22.8121` edge `0.1284` maxDD `-2.164`
- `market_context_high->unknown_4h` score `2.0185` n `133` status `ready` deltaP `20.2251` edge `0.0742` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.188` n `52` status `ready` deltaP `16.3634` edge `0.0069` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.7478` n `52` status `ready` deltaP `16.6628` edge `0.0212` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.4232` n `51` status `ready` deltaP `9.5857` edge `0.0111` maxDD `-0.1788`
- `news_risk_high->commodity_1h` score `0.2356` n `52` status `ready` deltaP `8.8669` edge `-0.0082` maxDD `-0.5024`
- `market_context_high->unknown_1h` score `0.075` n `133` status `ready` deltaP `11.8713` edge `-0.028` maxDD `-1.5916`
- `news_risk_high->index_1h` score `0.044` n `52` status `ready` deltaP `5.8729` edge `0.0018` maxDD `-0.1583`
- `news_risk_high->metal_4h` score `-0.2775` n `51` status `ready` deltaP `6.1484` edge `-0.011` maxDD `-0.249`
- `news_risk_high->metal_1h` score `-0.3906` n `52` status `ready` deltaP `-0.1727` edge `-0.0088` maxDD `-0.1413`
- `market_context_high->fx_1h` score `-0.4903` n `133` status `ready` deltaP `1.6006` edge `-0.0003` maxDD `-0.8587`
- `market_context_high->metal_4h` score `-0.6653` n `133` status `ready` deltaP `6.399` edge `-0.0344` maxDD `-2.4293`
- `news_risk_high->metal_24h` score `-0.6804` n `51` status `ready` deltaP `21.6503` edge `-0.1968` maxDD `-0.0053`
- `market_context_high->index_1h` score `-1.1688` n `133` status `ready` deltaP `-5.6222` edge `-0.0061` maxDD `-1.3054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
