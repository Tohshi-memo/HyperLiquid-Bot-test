# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T10:37:33.686836+00:00`
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

- `news_risk_high->unknown_24h` score `43.6374` n `51` status `ready` deltaP `2.2569` edge `3.6214` maxDD `0.0`
- `news_risk_high->unknown_4h` score `13.0126` n `51` status `ready` deltaP `25.7831` edge `0.9171` maxDD `-0.0348`
- `news_risk_high->equity_24h` score `9.894` n `51` status `ready` deltaP `36.4175` edge `0.6748` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.6475` n `51` status `ready` deltaP `45.4759` edge `0.0993` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.1511` n `52` status `ready` deltaP `15.9488` edge `0.1918` maxDD `-0.8426`
- `news_risk_high->fx_4h` score `3.0887` n `51` status `ready` deltaP `36.5585` edge `0.0271` maxDD `-0.0746`
- `news_risk_high->equity_4h` score `2.4906` n `51` status `ready` deltaP `22.9645` edge `0.1315` maxDD `-2.164`
- `market_context_high->unknown_4h` score `2.0185` n `133` status `ready` deltaP `20.2251` edge `0.0742` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.188` n `52` status `ready` deltaP `16.3634` edge `0.0069` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.7361` n `52` status `ready` deltaP `16.5131` edge `0.0207` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.4402` n `51` status `ready` deltaP `9.7381` edge `0.0115` maxDD `-0.1788`
- `news_risk_high->commodity_1h` score `0.2356` n `52` status `ready` deltaP `8.8669` edge `-0.0082` maxDD `-0.5024`
- `market_context_high->unknown_1h` score `0.0762` n `133` status `ready` deltaP `11.8713` edge `-0.0279` maxDD `-1.5916`
- `news_risk_high->index_1h` score `0.0354` n `52` status `ready` deltaP `5.7232` edge `0.0017` maxDD `-0.1583`
- `news_risk_high->metal_4h` score `-0.2739` n `51` status `ready` deltaP `6.1484` edge `-0.0107` maxDD `-0.249`
- `news_risk_high->metal_1h` score `-0.3906` n `52` status `ready` deltaP `-0.1727` edge `-0.0088` maxDD `-0.1413`
- `market_context_high->fx_1h` score `-0.4903` n `133` status `ready` deltaP `1.6006` edge `-0.0003` maxDD `-0.8587`
- `market_context_high->metal_4h` score `-0.6617` n `133` status `ready` deltaP `6.399` edge `-0.0341` maxDD `-2.4293`
- `news_risk_high->metal_24h` score `-0.6756` n `51` status `ready` deltaP `21.6503` edge `-0.1964` maxDD `-0.0053`
- `market_context_high->index_1h` score `-1.182` n `133` status `ready` deltaP `-5.7719` edge `-0.0062` maxDD `-1.3054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
