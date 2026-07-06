# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T19:37:33.147715+00:00`
- Price records: `672`
- Market context records: `5909`
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
- `news_risk_high->fx_1h` score `1.9998` n `30` status `ready` deltaP `24.2315` edge `0.019` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `0.926` n `30` status `ready` deltaP `11.0878` edge `0.0915` maxDD `-2.0691`
- `market_context_high->equity_4h` score `0.8349` n `220` status `ready` deltaP `7.6829` edge `0.1278` maxDD `-4.0887`
- `news_risk_high->crypto_alt_1h` score `0.206` n `30` status `ready` deltaP `4.8703` edge `0.0401` maxDD `-1.6923`
- `market_context_high->equity_1h` score `-0.2156` n `221` status `ready` deltaP `4.7952` edge `0.0324` maxDD `-4.3608`
- `market_context_high->metal_1h` score `-0.3366` n `221` status `ready` deltaP `3.1112` edge `0.0032` maxDD `-2.0339`
- `news_risk_high->metal_1h` score `-0.4725` n `30` status `ready` deltaP `0.7884` edge `-0.0292` maxDD `-1.2643`
- `market_context_high->commodity_1h` score `-0.4837` n `221` status `ready` deltaP `-1.2979` edge `-0.0018` maxDD `-1.4578`
- `market_context_high->crypto_major_1h` score `-0.5331` n `221` status `ready` deltaP `3.8631` edge `0.038` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-0.6627` n `221` status `ready` deltaP `2.5022` edge `0.0318` maxDD `-6.6758`
- `market_context_high->fx_1h` score `-0.8003` n `221` status `ready` deltaP `-2.4955` edge `-0.0012` maxDD `-0.5751`
- `market_context_high->index_1h` score `-0.9813` n `221` status `ready` deltaP `-0.0596` edge `0.0034` maxDD `-0.7819`
- `news_risk_high->index_1h` score `-1.2159` n `30` status `ready` deltaP `-12.0958` edge `-0.0238` maxDD `-1.1161`
- `market_context_high->commodity_4h` score `-1.6131` n `220` status `ready` deltaP `-2.6801` edge `-0.0176` maxDD `-6.3734`
- `market_context_high->metal_4h` score `-1.7298` n `220` status `ready` deltaP `-3.6807` edge `-0.034` maxDD `-5.725`
- `news_risk_high->commodity_4h` score `-1.9311` n `30` status `ready` deltaP `-15.5589` edge `-0.0563` maxDD `-2.3372`
- `market_context_high->index_4h` score `-2.0165` n `220` status `ready` deltaP `-1.2472` edge `0.009` maxDD `-3.165`
- `market_context_high->crypto_major_4h` score `-2.1125` n `220` status `ready` deltaP `7.7106` edge `0.115` maxDD `-25.6458`
- `market_context_high->fx_24h` score `-2.1343` n `213` status `ready` deltaP `0.8949` edge `0.0022` maxDD `-5.5435`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
