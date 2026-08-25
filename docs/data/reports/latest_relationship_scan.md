# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T10:07:30.933606+00:00`
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

- `news_risk_high->unknown_24h` score `43.6644` n `51` status `ready` deltaP `2.4306` edge `3.6225` maxDD `0.0`
- `news_risk_high->unknown_4h` score `13.0066` n `51` status `ready` deltaP `25.7831` edge `0.9166` maxDD `-0.0348`
- `news_risk_high->equity_24h` score `10.0178` n `51` status `ready` deltaP `36.7647` edge `0.6828` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.6884` n `51` status `ready` deltaP `45.8231` edge `0.1004` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.1176` n `52` status `ready` deltaP `15.6494` edge `0.191` maxDD `-0.8426`
- `news_risk_high->fx_4h` score `3.0753` n `51` status `ready` deltaP `36.406` edge `0.027` maxDD `-0.0746`
- `news_risk_high->equity_4h` score `2.5546` n `51` status `ready` deltaP `23.2694` edge `0.1348` maxDD `-2.164`
- `market_context_high->unknown_4h` score `2.0125` n `133` status `ready` deltaP `20.2251` edge `0.0737` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.1748` n `52` status `ready` deltaP `16.2137` edge `0.0068` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.7307` n `52` status `ready` deltaP `16.5131` edge `0.02` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.4694` n `51` status `ready` deltaP `10.043` edge `0.0119` maxDD `-0.1788`
- `news_risk_high->commodity_1h` score `0.2344` n `52` status `ready` deltaP `8.8669` edge `-0.0083` maxDD `-0.5024`
- `market_context_high->unknown_1h` score `0.0426` n `133` status `ready` deltaP `11.5719` edge `-0.0287` maxDD `-1.5916`
- `news_risk_high->index_1h` score `0.0347` n `52` status `ready` deltaP `5.7232` edge `0.0016` maxDD `-0.1583`
- `news_risk_high->metal_4h` score `-0.2739` n `51` status `ready` deltaP `6.1484` edge `-0.0107` maxDD `-0.249`
- `news_risk_high->metal_1h` score `-0.3906` n `52` status `ready` deltaP `-0.1727` edge `-0.0088` maxDD `-0.1413`
- `market_context_high->fx_1h` score `-0.4989` n `133` status `ready` deltaP `1.4509` edge `-0.0004` maxDD `-0.8587`
- `market_context_high->metal_4h` score `-0.6617` n `133` status `ready` deltaP `6.399` edge `-0.0341` maxDD `-2.4293`
- `news_risk_high->metal_24h` score `-0.6684` n `51` status `ready` deltaP `21.6503` edge `-0.1958` maxDD `-0.0053`
- `market_context_high->index_1h` score `-1.1832` n `133` status `ready` deltaP `-5.7719` edge `-0.0063` maxDD `-1.3054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
