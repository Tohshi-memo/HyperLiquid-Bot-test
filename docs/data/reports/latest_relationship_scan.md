# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T01:22:28.773215+00:00`
- Price records: `672`
- Market context records: `5933`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11237`

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

- `news_risk_high->fx_4h` score `3.5997` n `30` status `ready` deltaP `37.2561` edge `0.0562` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.1004` n `30` status `ready` deltaP `25.4291` edge `0.0194` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.1686` n `221` status `ready` deltaP `9.2133` edge `0.1454` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.8294` n `30` status `ready` deltaP `10.489` edge `0.0831` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.153` n `30` status `ready` deltaP `4.8703` edge `0.0333` maxDD `-1.6923`
- `market_context_high->equity_1h` score `-0.1221` n `221` status `ready` deltaP `5.8431` edge `0.0374` maxDD `-4.3608`
- `market_context_high->metal_1h` score `-0.3054` n `221` status `ready` deltaP `3.8597` edge `0.0022` maxDD `-2.0339`
- `news_risk_high->metal_1h` score `-0.4414` n `30` status `ready` deltaP `1.5369` edge `-0.0302` maxDD `-1.2643`
- `market_context_high->commodity_1h` score `-0.5662` n `221` status `ready` deltaP `-2.7949` edge `-0.0024` maxDD `-1.4578`
- `market_context_high->crypto_major_1h` score `-0.6298` n `221` status `ready` deltaP `3.2643` edge `0.0296` maxDD `-6.2348`
- `market_context_high->fx_1h` score `-0.6997` n `221` status `ready` deltaP `-1.2979` edge `-0.0008` maxDD `-0.5751`
- `market_context_high->crypto_alt_1h` score `-0.7158` n `221` status `ready` deltaP `2.5022` edge `0.025` maxDD `-6.6758`
- `market_context_high->index_1h` score `-0.8938` n `221` status `ready` deltaP `0.8386` edge `0.0047` maxDD `-0.7819`
- `news_risk_high->index_1h` score `-1.1591` n `30` status `ready` deltaP `-11.1976` edge `-0.0225` maxDD `-1.1161`
- `market_context_high->equity_24h` score `-1.2862` n `213` status `ready` deltaP `16.6227` edge `0.2319` maxDD `-31.2762`
- `market_context_high->commodity_4h` score `-1.7277` n `221` status `ready` deltaP `-4.5408` edge `-0.0199` maxDD `-6.3734`
- `market_context_high->metal_4h` score `-1.8287` n `221` status `ready` deltaP `-4.2331` edge `-0.043` maxDD `-5.725`
- `market_context_high->index_4h` score `-1.8727` n `221` status `ready` deltaP `0.0255` edge `0.0125` maxDD `-3.165`
- `news_risk_high->commodity_4h` score `-2.0631` n `30` status `ready` deltaP `-17.6931` edge `-0.059` maxDD `-2.3372`
- `market_context_high->fx_24h` score `-2.1437` n `213` status `ready` deltaP `0.8949` edge `0.001` maxDD `-5.5435`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
