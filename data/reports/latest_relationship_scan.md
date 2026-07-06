# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T19:52:25.965957+00:00`
- Price records: `672`
- Market context records: `5910`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11166`

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

- `news_risk_high->fx_4h` score `3.6047` n `30` status `ready` deltaP `37.4085` edge `0.0556` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.013` n `30` status `ready` deltaP `24.3812` edge `0.0191` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `0.9128` n `30` status `ready` deltaP `10.9381` edge `0.0908` maxDD `-2.0691`
- `market_context_high->equity_4h` score `0.8591` n `220` status `ready` deltaP `7.8354` edge `0.1288` maxDD `-4.0887`
- `news_risk_high->crypto_alt_1h` score `0.2037` n `30` status `ready` deltaP `4.8703` edge `0.0398` maxDD `-1.6923`
- `market_context_high->equity_1h` score `-0.2156` n `221` status `ready` deltaP `4.7952` edge `0.0324` maxDD `-4.3608`
- `market_context_high->metal_1h` score `-0.3358` n `221` status `ready` deltaP `3.1112` edge `0.0033` maxDD `-2.0339`
- `news_risk_high->metal_1h` score `-0.4718` n `30` status `ready` deltaP `0.7884` edge `-0.0291` maxDD `-1.2643`
- `market_context_high->commodity_1h` score `-0.4922` n `221` status `ready` deltaP `-1.4476` edge `-0.0019` maxDD `-1.4578`
- `market_context_high->crypto_major_1h` score `-0.5464` n `221` status `ready` deltaP `3.7134` edge `0.0373` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-0.6651` n `221` status `ready` deltaP `2.5022` edge `0.0315` maxDD `-6.6758`
- `market_context_high->fx_1h` score `-0.7871` n `221` status `ready` deltaP `-2.3458` edge `-0.0011` maxDD `-0.5751`
- `market_context_high->index_1h` score `-0.9813` n `221` status `ready` deltaP `-0.0596` edge `0.0034` maxDD `-0.7819`
- `news_risk_high->index_1h` score `-1.2159` n `30` status `ready` deltaP `-12.0958` edge `-0.0238` maxDD `-1.1161`
- `market_context_high->commodity_4h` score `-1.6218` n `220` status `ready` deltaP `-2.8325` edge `-0.0177` maxDD `-6.3734`
- `market_context_high->metal_4h` score `-1.7306` n `220` status `ready` deltaP `-3.6807` edge `-0.0341` maxDD `-5.725`
- `news_risk_high->commodity_4h` score `-1.9398` n `30` status `ready` deltaP `-15.7113` edge `-0.0564` maxDD `-2.3372`
- `market_context_high->index_4h` score `-2.0031` n `220` status `ready` deltaP `-1.0947` edge `0.0091` maxDD `-3.165`
- `market_context_high->equity_24h` score `-2.1276` n `213` status `ready` deltaP `12.8032` edge `0.1495` maxDD `-31.2762`
- `market_context_high->fx_24h` score `-2.1351` n `213` status `ready` deltaP `0.8949` edge `0.0021` maxDD `-5.5435`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
