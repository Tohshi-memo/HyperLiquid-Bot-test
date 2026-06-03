# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T23:52:24.525465+00:00`
- Price records: `672`
- Market context records: `2812`
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

- `market_context_high->unknown_24h` score `2.505` n `142` status `ready` deltaP `3.1225` edge `0.2344` maxDD `-1.7175`
- `market_context_high->unknown_4h` score `0.9798` n `142` status `ready` deltaP `6.6429` edge `0.1427` maxDD `-3.7602`
- `market_context_high->commodity_24h` score `0.6883` n `142` status `ready` deltaP `11.2114` edge `0.292` maxDD `-12.4171`
- `market_context_high->crypto_alt_24h` score `0.4113` n `142` status `ready` deltaP `0.0979` edge `0.4253` maxDD `-22.6673`
- `market_context_high->index_4h` score `0.3434` n `142` status `ready` deltaP `13.3009` edge `0.0395` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `0.0946` n `142` status `ready` deltaP `4.9296` edge `0.0481` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.0571` n `142` status `ready` deltaP `4.4974` edge `0.0121` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.5251` n `142` status `ready` deltaP `-0.3879` edge `0.0032` maxDD `-0.2164`
- `market_context_high->metal_1h` score `-0.6061` n `142` status `ready` deltaP `0.8813` edge `0.001` maxDD `-3.0996`
- `market_context_high->commodity_1h` score `-0.6172` n `142` status `ready` deltaP `0.0169` edge `-0.0039` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.7599` n `142` status `ready` deltaP `4.9465` edge `0.0456` maxDD `-10.747`
- `market_context_high->equity_1h` score `-0.8343` n `142` status `ready` deltaP `-2.3003` edge `0.0291` maxDD `-2.6634`
- `market_context_high->crypto_major_1h` score `-0.9428` n `142` status `ready` deltaP `3.926` edge `0.0399` maxDD `-9.622`
- `market_context_high->equity_4h` score `-0.981` n `142` status `ready` deltaP `2.2673` edge `0.0411` maxDD `-5.7037`
- `market_context_high->fx_4h` score `-1.1703` n `142` status `ready` deltaP `-4.0579` edge `0.0074` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.5233` n `142` status `ready` deltaP `0.6183` edge `-0.0074` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.7526` n `142` status `ready` deltaP `-5.1838` edge `-0.0243` maxDD `-0.6418`
- `market_context_high->index_24h` score `-1.7545` n `142` status `ready` deltaP `-0.0049` edge `-0.0481` maxDD `-2.5127`
- `market_context_high->crypto_alt_4h` score `-1.8119` n `142` status `ready` deltaP `13.4232` edge `0.1936` maxDD `-28.7261`
- `market_context_high->metal_4h` score `-2.1575` n `142` status `ready` deltaP `-0.0086` edge `-0.0215` maxDD `-11.4038`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
