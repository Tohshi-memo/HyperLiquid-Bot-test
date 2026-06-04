# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T04:52:23.621108+00:00`
- Price records: `672`
- Market context records: `2833`
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

- `market_context_high->unknown_24h` score `2.3219` n `142` status `ready` deltaP `2.9489` edge `0.2203` maxDD `-1.7175`
- `market_context_high->unknown_4h` score `0.9064` n `142` status `ready` deltaP `6.4904` edge `0.1376` maxDD `-3.7602`
- `market_context_high->commodity_24h` score `0.7581` n `142` status `ready` deltaP `11.5586` edge `0.2955` maxDD `-12.4171`
- `market_context_high->crypto_alt_24h` score `0.5198` n `142` status `ready` deltaP `-0.0758` edge `0.4355` maxDD `-22.6673`
- `market_context_high->index_4h` score `0.3026` n `142` status `ready` deltaP `12.996` edge `0.0363` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.0241` n `142` status `ready` deltaP `4.0314` edge `0.0442` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.142` n `142` status `ready` deltaP `3.4495` edge `0.0082` maxDD `-1.2855`
- `market_context_high->index_24h` score `-0.5383` n `142` status `ready` deltaP `3.4673` edge `0.0301` maxDD `-2.5127`
- `market_context_high->commodity_1h` score `-0.5836` n `142` status `ready` deltaP `0.0169` edge `0.0004` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.6029` n `142` status `ready` deltaP `-1.2861` edge `0.0027` maxDD `-0.2164`
- `market_context_high->metal_1h` score `-0.7814` n `142` status `ready` deltaP `-0.6157` edge `-0.0115` maxDD `-3.0996`
- `market_context_high->crypto_alt_1h` score `-0.8316` n `142` status `ready` deltaP `4.3477` edge `0.0404` maxDD `-10.747`
- `market_context_high->crypto_major_1h` score `-1.0496` n `142` status `ready` deltaP `3.3272` edge `0.0302` maxDD `-9.622`
- `market_context_high->equity_4h` score `-1.069` n `142` status `ready` deltaP `1.9624` edge `0.0358` maxDD `-5.7037`
- `market_context_high->equity_1h` score `-1.0717` n `142` status `ready` deltaP `-3.4979` edge `0.0173` maxDD `-2.6634`
- `market_context_high->fx_4h` score `-1.1689` n `142` status `ready` deltaP `-3.9054` edge `0.0065` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.3035` n `142` status `ready` deltaP `2.2951` edge `0.0096` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.5722` n `142` status `ready` deltaP `-3.2741` edge `-0.022` maxDD `-0.6418`
- `market_context_high->crypto_alt_4h` score `-1.6187` n `142` status `ready` deltaP `13.4232` edge `0.2097` maxDD `-28.7261`
- `market_context_high->equity_24h` score `-2.3521` n `142` status `ready` deltaP `1.269` edge `-0.0041` maxDD `-12.6963`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
