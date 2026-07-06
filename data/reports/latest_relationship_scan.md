# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T21:37:38.144419+00:00`
- Price records: `672`
- Market context records: `5917`
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

- `news_risk_high->fx_4h` score `3.6765` n `30` status `ready` deltaP `38.1707` edge `0.0565` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.0741` n `30` status `ready` deltaP `25.1297` edge `0.0192` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `0.9081` n `30` status `ready` deltaP `11.0878` edge `0.0892` maxDD `-2.0691`
- `market_context_high->equity_4h` score `0.8893` n `220` status `ready` deltaP `7.9878` edge `0.1303` maxDD `-4.0887`
- `news_risk_high->crypto_alt_1h` score `0.185` n `30` status `ready` deltaP `4.8703` edge `0.0374` maxDD `-1.6923`
- `market_context_high->equity_1h` score `-0.1876` n `221` status `ready` deltaP `5.2443` edge `0.033` maxDD `-4.3608`
- `market_context_high->metal_1h` score `-0.3109` n `221` status `ready` deltaP `3.5603` edge `0.0035` maxDD `-2.0339`
- `news_risk_high->metal_1h` score `-0.4468` n `30` status `ready` deltaP `1.2375` edge `-0.0289` maxDD `-1.2643`
- `market_context_high->commodity_1h` score `-0.5164` n `221` status `ready` deltaP `-1.8967` edge `-0.002` maxDD `-1.4578`
- `market_context_high->crypto_major_1h` score `-0.5511` n `221` status `ready` deltaP `3.8631` edge `0.0357` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-0.6838` n `221` status `ready` deltaP `2.5022` edge `0.0291` maxDD `-6.6758`
- `market_context_high->fx_1h` score `-0.726` n `221` status `ready` deltaP `-1.5973` edge `-0.001` maxDD `-0.5751`
- `market_context_high->index_1h` score `-0.9813` n `221` status `ready` deltaP `-0.0596` edge `0.0034` maxDD `-0.7819`
- `news_risk_high->index_1h` score `-1.2159` n `30` status `ready` deltaP `-12.0958` edge `-0.0238` maxDD `-1.1161`
- `market_context_high->commodity_4h` score `-1.6897` n `220` status `ready` deltaP `-3.8996` edge `-0.0193` maxDD `-6.3734`
- `market_context_high->metal_4h` score `-1.8211` n `220` status `ready` deltaP `-4.7477` edge `-0.0386` maxDD `-5.725`
- `market_context_high->equity_24h` score `-1.8904` n `213` status `ready` deltaP `14.0185` edge `0.1718` maxDD `-31.2762`
- `news_risk_high->commodity_4h` score `-2.0078` n `30` status `ready` deltaP `-16.7784` edge `-0.058` maxDD `-2.3372`
- `market_context_high->index_4h` score `-2.0237` n `220` status `ready` deltaP `-1.2472` edge `0.0084` maxDD `-3.165`
- `market_context_high->fx_24h` score `-2.1413` n `213` status `ready` deltaP `0.8949` edge `0.0013` maxDD `-5.5435`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
