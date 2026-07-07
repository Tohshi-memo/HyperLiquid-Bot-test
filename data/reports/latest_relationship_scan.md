# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T00:07:27.449200+00:00`
- Price records: `672`
- Market context records: `5928`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11236`

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

- `news_risk_high->fx_4h` score `3.6667` n `30` status `ready` deltaP `38.0183` edge `0.0567` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.0897` n `30` status `ready` deltaP `25.2794` edge `0.0195` maxDD `-0.1113`
- `market_context_high->equity_4h` score `0.9552` n `221` status `ready` deltaP `8.4511` edge `0.1327` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.8559` n `30` status `ready` deltaP `10.7884` edge `0.0845` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.1546` n `30` status `ready` deltaP `4.8703` edge `0.0335` maxDD `-1.6923`
- `market_context_high->equity_1h` score `-0.1845` n `221` status `ready` deltaP `5.2443` edge `0.0334` maxDD `-4.3608`
- `market_context_high->metal_1h` score `-0.3156` n `221` status `ready` deltaP `3.71` edge `0.0019` maxDD `-2.0339`
- `news_risk_high->metal_1h` score `-0.4515` n `30` status `ready` deltaP `1.3872` edge `-0.0305` maxDD `-1.2643`
- `market_context_high->commodity_1h` score `-0.5748` n `221` status `ready` deltaP `-2.9446` edge `-0.0025` maxDD `-1.4578`
- `market_context_high->crypto_major_1h` score `-0.6033` n `221` status `ready` deltaP `3.5637` edge `0.031` maxDD `-6.2348`
- `market_context_high->fx_1h` score `-0.7105` n `221` status `ready` deltaP `-1.4476` edge `-0.0007` maxDD `-0.5751`
- `market_context_high->crypto_alt_1h` score `-0.7142` n `221` status `ready` deltaP `2.5022` edge `0.0252` maxDD `-6.6758`
- `market_context_high->index_1h` score `-0.9573` n `221` status `ready` deltaP `0.2398` edge `0.0034` maxDD `-0.7819`
- `news_risk_high->index_1h` score `-1.2004` n `30` status `ready` deltaP `-11.7964` edge `-0.0238` maxDD `-1.1161`
- `market_context_high->equity_24h` score `-1.51` n `213` status `ready` deltaP `15.7546` edge `0.209` maxDD `-31.2762`
- `market_context_high->commodity_4h` score `-1.6914` n `221` status `ready` deltaP `-3.931` edge `-0.0193` maxDD `-6.3734`
- `market_context_high->metal_4h` score `-1.8784` n `221` status `ready` deltaP `-4.8428` edge `-0.0453` maxDD `-5.725`
- `market_context_high->index_4h` score `-1.9757` n `221` status `ready` deltaP `-0.7367` edge `0.009` maxDD `-3.165`
- `news_risk_high->commodity_4h` score `-2.0267` n `30` status `ready` deltaP `-17.0833` edge `-0.0584` maxDD `-2.3372`
- `market_context_high->fx_24h` score `-2.1444` n `213` status `ready` deltaP `0.8949` edge `0.0009` maxDD `-5.5435`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
