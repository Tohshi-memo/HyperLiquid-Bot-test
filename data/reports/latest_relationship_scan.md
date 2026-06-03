# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T11:37:22.682612+00:00`
- Price records: `672`
- Market context records: `2760`
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

- `market_context_high->unknown_24h` score `5.7509` n `129` status `ready` deltaP `12.6535` edge `0.4277` maxDD `-1.6255`
- `market_context_high->crypto_alt_24h` score `3.946` n `129` status `ready` deltaP `6.9242` edge `0.8091` maxDD `-19.9486`
- `market_context_high->unknown_4h` score `0.9595` n `143` status `ready` deltaP `6.5539` edge `0.1416` maxDD `-3.7602`
- `market_context_high->index_4h` score `0.0716` n `143` status `ready` deltaP `10.3989` edge `0.024` maxDD `-2.3986`
- `market_context_high->commodity_24h` score `-0.1314` n `129` status `ready` deltaP `7.9861` edge `0.2393` maxDD `-12.4171`
- `market_context_high->unknown_1h` score `-0.1448` n `143` status `ready` deltaP `3.4976` edge `0.0377` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.1534` n `143` status `ready` deltaP `3.2003` edge `0.0084` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.5734` n `143` status `ready` deltaP `-0.9463` edge `0.0029` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.6512` n `143` status `ready` deltaP `-0.247` edge `-0.0065` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.7053` n `143` status `ready` deltaP `5.5463` edge `0.0486` maxDD `-10.747`
- `market_context_high->metal_1h` score `-0.7832` n `143` status `ready` deltaP `-1.1003` edge `-0.0085` maxDD `-3.0996`
- `market_context_high->crypto_major_1h` score `-0.976` n `143` status `ready` deltaP `3.4976` edge `0.0385` maxDD `-9.622`
- `market_context_high->equity_1h` score `-1.1716` n `143` status `ready` deltaP `-3.7864` edge `0.0109` maxDD `-2.6634`
- `market_context_high->fx_4h` score `-1.2161` n `143` status `ready` deltaP `-4.5551` edge `0.0069` maxDD `-0.5631`
- `market_context_high->fx_24h` score `-1.2374` n `129` status `ready` deltaP `0.3553` edge `-0.0183` maxDD `-0.6418`
- `market_context_high->crypto_alt_4h` score `-1.2438` n `143` status `ready` deltaP `14.8389` edge `0.2315` maxDD `-28.7261`
- `market_context_high->commodity_4h` score `-1.7111` n `143` status `ready` deltaP `-0.7728` edge `-0.0222` maxDD `-10.0279`
- `market_context_high->equity_4h` score `-2.0697` n `143` status `ready` deltaP `-1.0969` edge `-0.0272` maxDD `-5.7037`
- `market_context_high->metal_4h` score `-2.4426` n `143` status `ready` deltaP `-2.4913` edge `-0.0415` maxDD `-11.4038`
- `market_context_high->crypto_major_4h` score `-2.6164` n `143` status `ready` deltaP `5.2277` edge `0.1203` maxDD `-32.2466`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
