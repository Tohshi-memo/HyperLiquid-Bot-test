# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T23:37:37.112333+00:00`
- Price records: `672`
- Market context records: `6030`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11125`

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

- `news_risk_high->fx_24h` score `7.8904` n `30` status `ready` deltaP `71.1806` edge `0.183` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.3075` n `30` status `ready` deltaP `44.5732` edge `0.0664` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `2.928` n `30` status `ready` deltaP `27.2917` edge `0.0826` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.2574` n `30` status `ready` deltaP `27.0758` edge `0.0215` maxDD `-0.1113`
- `market_context_high->equity_24h` score `1.688` n `180` status `ready` deltaP `29.7223` edge `0.5634` maxDD `-31.6107`
- `market_context_high->equity_4h` score `1.6687` n `206` status `ready` deltaP `9.2514` edge `0.1691` maxDD `-2.671`
- `news_risk_high->crypto_major_1h` score `0.8286` n `30` status `ready` deltaP `10.1896` edge `0.085` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.2403` n `30` status `ready` deltaP `5.6188` edge `0.0395` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.1522` n `30` status `ready` deltaP `9.2361` edge `0.0451` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.394` n `206` status `ready` deltaP `3.5797` edge `0.0055` maxDD `-2.0564`
- `news_risk_high->crypto_alt_24h` score `-0.4214` n `30` status `ready` deltaP `23.1944` edge `-0.175` maxDD `-0.5131`
- `market_context_high->index_24h` score `-0.4273` n `180` status `ready` deltaP `5.3472` edge `0.0796` maxDD `-5.6021`
- `news_risk_high->metal_1h` score `-0.4304` n `30` status `ready` deltaP `1.0878` edge `-0.0258` maxDD `-1.2643`
- `market_context_high->fx_1h` score `-0.575` n `206` status `ready` deltaP `-0.141` edge `-0.0013` maxDD `-0.6538`
- `market_context_high->commodity_1h` score `-0.6511` n `206` status `ready` deltaP `-1.3836` edge `-0.0004` maxDD `-0.5708`
- `market_context_high->index_4h` score `-0.9221` n `206` status `ready` deltaP `2.5678` edge `0.018` maxDD `-1.9335`
- `market_context_high->metal_4h` score `-0.9237` n `206` status `ready` deltaP `5.0956` edge `0.0078` maxDD `-3.4996`
- `market_context_high->equity_1h` score `-0.9354` n `206` status `ready` deltaP `1.2296` edge `0.0267` maxDD `-4.3608`
- `market_context_high->crypto_alt_1h` score `-0.9662` n `206` status `ready` deltaP `3.8065` edge `0.026` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.9891` n `206` status `ready` deltaP `3.6524` edge `0.0256` maxDD `-9.807`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
