# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T20:22:42.729587+00:00`
- Price records: `672`
- Market context records: `5912`
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

- `news_risk_high->fx_4h` score `3.6193` n `30` status `ready` deltaP `37.561` edge `0.0558` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.025` n `30` status `ready` deltaP `24.5309` edge `0.0191` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `0.9097` n `30` status `ready` deltaP `10.9381` edge `0.0904` maxDD `-2.0691`
- `market_context_high->equity_4h` score `0.8905` n `220` status `ready` deltaP `7.9878` edge `0.1304` maxDD `-4.0887`
- `news_risk_high->crypto_alt_1h` score `0.1975` n `30` status `ready` deltaP `4.8703` edge `0.039` maxDD `-1.6923`
- `market_context_high->equity_1h` score `-0.2063` n `221` status `ready` deltaP `4.9449` edge `0.0326` maxDD `-4.3608`
- `market_context_high->metal_1h` score `-0.3187` n `221` status `ready` deltaP `3.4106` edge `0.0035` maxDD `-2.0339`
- `news_risk_high->metal_1h` score `-0.4546` n `30` status `ready` deltaP `1.0878` edge `-0.0289` maxDD `-1.2643`
- `market_context_high->commodity_1h` score `-0.5` n `221` status `ready` deltaP `-1.5973` edge `-0.0019` maxDD `-1.4578`
- `market_context_high->crypto_major_1h` score `-0.5495` n `221` status `ready` deltaP `3.7134` edge `0.0369` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-0.6713` n `221` status `ready` deltaP `2.5022` edge `0.0307` maxDD `-6.6758`
- `market_context_high->fx_1h` score `-0.7752` n `221` status `ready` deltaP `-2.1961` edge `-0.0011` maxDD `-0.5751`
- `market_context_high->index_1h` score `-0.9561` n `221` status `ready` deltaP `0.2398` edge `0.0035` maxDD `-0.7819`
- `news_risk_high->index_1h` score `-1.1996` n `30` status `ready` deltaP `-11.7964` edge `-0.0237` maxDD `-1.1161`
- `market_context_high->commodity_4h` score `-1.6392` n `220` status `ready` deltaP `-3.1374` edge `-0.0179` maxDD `-6.3734`
- `market_context_high->metal_4h` score `-1.7511` n `220` status `ready` deltaP `-3.9856` edge `-0.0347` maxDD `-5.725`
- `news_risk_high->commodity_4h` score `-1.9572` n `30` status `ready` deltaP `-16.0162` edge `-0.0566` maxDD `-2.3372`
- `market_context_high->index_4h` score `-1.9885` n `220` status `ready` deltaP `-0.9423` edge `0.0093` maxDD `-3.165`
- `market_context_high->equity_24h` score `-2.058` n `213` status `ready` deltaP `13.1504` edge `0.1561` maxDD `-31.2762`
- `market_context_high->fx_24h` score `-2.1366` n `213` status `ready` deltaP `0.8949` edge `0.0019` maxDD `-5.5435`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
