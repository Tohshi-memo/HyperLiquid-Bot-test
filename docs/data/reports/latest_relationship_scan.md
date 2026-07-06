# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T19:07:41.832665+00:00`
- Price records: `672`
- Market context records: `5907`
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
- `news_risk_high->fx_1h` score `1.9878` n `30` status `ready` deltaP `24.0818` edge `0.019` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `0.9463` n `30` status `ready` deltaP `11.3872` edge `0.0921` maxDD `-2.0691`
- `market_context_high->equity_4h` score `0.7949` n `220` status `ready` deltaP `7.378` edge `0.1265` maxDD `-4.0887`
- `news_risk_high->crypto_alt_1h` score `0.2255` n `30` status `ready` deltaP `5.1697` edge `0.0406` maxDD `-1.6923`
- `market_context_high->equity_1h` score `-0.2164` n `221` status `ready` deltaP `4.7952` edge `0.0323` maxDD `-4.3608`
- `market_context_high->metal_1h` score `-0.3451` n `221` status `ready` deltaP `2.9615` edge `0.0031` maxDD `-2.0339`
- `news_risk_high->metal_1h` score `-0.4811` n `30` status `ready` deltaP `0.6387` edge `-0.0293` maxDD `-1.2643`
- `market_context_high->commodity_1h` score `-0.4829` n `221` status `ready` deltaP `-1.2979` edge `-0.0017` maxDD `-1.4578`
- `market_context_high->crypto_major_1h` score `-0.5129` n `221` status `ready` deltaP `4.1625` edge `0.0386` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-0.6433` n `221` status `ready` deltaP `2.8016` edge `0.0323` maxDD `-6.6758`
- `market_context_high->fx_1h` score `-0.8123` n `221` status `ready` deltaP `-2.6452` edge `-0.0012` maxDD `-0.5751`
- `market_context_high->index_1h` score `-0.9681` n `221` status `ready` deltaP `0.0901` edge `0.0035` maxDD `-0.7819`
- `news_risk_high->index_1h` score `-1.2074` n `30` status `ready` deltaP `-11.9461` edge `-0.0237` maxDD `-1.1161`
- `market_context_high->commodity_4h` score `-1.6036` n `220` status `ready` deltaP `-2.5277` edge `-0.0174` maxDD `-6.3734`
- `market_context_high->metal_4h` score `-1.7282` n `220` status `ready` deltaP `-3.6807` edge `-0.0338` maxDD `-5.725`
- `news_risk_high->commodity_4h` score `-1.9216` n `30` status `ready` deltaP `-15.4065` edge `-0.0561` maxDD `-2.3372`
- `market_context_high->index_4h` score `-2.0287` n `220` status `ready` deltaP `-1.3996` edge `0.009` maxDD `-3.165`
- `market_context_high->crypto_major_4h` score `-2.0491` n `220` status `ready` deltaP `8.0155` edge `0.1211` maxDD `-25.6458`
- `market_context_high->fx_24h` score `-2.1327` n `213` status `ready` deltaP `0.8949` edge `0.0024` maxDD `-5.5435`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
