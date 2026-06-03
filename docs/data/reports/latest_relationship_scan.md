# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T08:37:22.930951+00:00`
- Price records: `672`
- Market context records: `2747`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9237`

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

- `market_context_high->unknown_24h` score `7.3845` n `117` status `ready` deltaP `15.2244` edge `0.5467` maxDD `-1.6255`
- `market_context_high->crypto_alt_24h` score `5.8629` n `117` status `ready` deltaP `12.8873` edge `1.0151` maxDD `-19.9486`
- `market_context_high->unknown_4h` score `0.9593` n `143` status `ready` deltaP `6.4014` edge `0.1426` maxDD `-3.7602`
- `market_context_high->index_4h` score `0.1594` n `143` status `ready` deltaP `11.0087` edge `0.0312` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.1076` n `143` status `ready` deltaP `3.4976` edge `0.0408` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.155` n `143` status `ready` deltaP `3.2003` edge `0.0082` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.5219` n `143` status `ready` deltaP `-0.3475` edge `0.0032` maxDD `-0.2164`
- `market_context_high->crypto_alt_1h` score `-0.6336` n `143` status `ready` deltaP `5.9954` edge `0.0548` maxDD `-10.747`
- `market_context_high->commodity_1h` score `-0.6909` n `143` status `ready` deltaP `-0.6961` edge `-0.0086` maxDD `-4.3601`
- `market_context_high->metal_1h` score `-0.7154` n `143` status `ready` deltaP `-0.6512` edge `-0.0028` maxDD `-3.0996`
- `market_context_high->crypto_major_1h` score `-0.951` n `143` status `ready` deltaP `3.6473` edge `0.0407` maxDD `-9.622`
- `market_context_high->crypto_alt_4h` score `-1.0232` n `143` status `ready` deltaP `15.6011` edge `0.2448` maxDD `-28.7261`
- `market_context_high->fx_4h` score `-1.1747` n `143` status `ready` deltaP `-4.0978` edge `0.0073` maxDD `-0.5631`
- `market_context_high->commodity_24h` score `-1.2365` n `117` status `ready` deltaP `4.5673` edge `0.1204` maxDD `-12.4171`
- `market_context_high->fx_24h` score `-1.24` n `117` status `ready` deltaP `0.0534` edge `-0.0165` maxDD `-0.6418`
- `market_context_high->equity_1h` score `-1.2471` n `143` status `ready` deltaP `-4.5349` edge `0.0096` maxDD `-2.6634`
- `market_context_high->commodity_4h` score `-1.6108` n `143` status `ready` deltaP `-0.3155` edge `-0.0124` maxDD `-10.0279`
- `market_context_high->equity_4h` score `-2.0099` n `143` status `ready` deltaP `-1.2493` edge `-0.0212` maxDD `-5.7037`
- `market_context_high->metal_4h` score `-2.38` n `143` status `ready` deltaP `-2.1864` edge `-0.0355` maxDD `-11.4038`
- `market_context_high->crypto_major_4h` score `-2.4375` n `143` status `ready` deltaP `6.4473` edge `0.1351` maxDD `-32.2466`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
