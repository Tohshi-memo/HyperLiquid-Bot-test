# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T20:22:28.025727+00:00`
- Price records: `672`
- Market context records: `6638`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11766`

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

- `market_context_high->unknown_1h` score `2.3567` n `203` status `ready` deltaP `-5.3413` edge `0.3221` maxDD `-3.2083`
- `market_context_high->unknown_24h` score `1.4925` n `189` status `ready` deltaP `-1.3228` edge `0.4495` maxDD `-12.3047`
- `market_context_high->commodity_24h` score `0.5691` n `189` status `ready` deltaP `10.1326` edge `0.1667` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `0.0994` n `203` status `ready` deltaP `8.6642` edge `0.0493` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.1349` n `203` status `ready` deltaP `5.9017` edge `0.0425` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.222` n `203` status `ready` deltaP `3.2351` edge `0.0007` maxDD `-0.7249`
- `market_context_high->index_1h` score `-0.4766` n `203` status `ready` deltaP `0.8208` edge `0.0052` maxDD `-0.7417`
- `market_context_high->commodity_1h` score `-0.6825` n `203` status `ready` deltaP `-1.5884` edge `-0.0086` maxDD `-2.1314`
- `market_context_high->unknown_4h` score `-0.7237` n `203` status `ready` deltaP `-15.5766` edge `0.2841` maxDD `-10.5788`
- `market_context_high->index_4h` score `-0.8043` n `203` status `ready` deltaP `10.7788` edge `0.013` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-0.8382` n `203` status `ready` deltaP `3.202` edge `0.0115` maxDD `-3.8827`
- `market_context_high->crypto_major_4h` score `-1.0474` n `203` status `ready` deltaP `10.7196` edge `0.1257` maxDD `-16.8495`
- `market_context_high->metal_1h` score `-1.1089` n `203` status `ready` deltaP `-2.9077` edge `0.0011` maxDD `-1.5966`
- `market_context_high->commodity_4h` score `-1.4096` n `203` status `ready` deltaP `-1.3119` edge `-0.0225` maxDD `-5.6246`
- `market_context_high->crypto_alt_4h` score `-1.4396` n `203` status `ready` deltaP `7.4124` edge `0.1062` maxDD `-19.2145`
- `market_context_high->fx_4h` score `-1.4808` n `203` status `ready` deltaP `4.6895` edge `0.0001` maxDD `-3.3635`
- `market_context_high->metal_4h` score `-1.8905` n `203` status `ready` deltaP `1.827` edge `0.0315` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-4.3395` n `203` status `ready` deltaP `8.9834` edge `0.0054` maxDD `-27.1529`
- `market_context_high->metal_24h` score `-5.5147` n `189` status `ready` deltaP `-2.5101` edge `0.0279` maxDD `-22.4543`
- `market_context_high->fx_24h` score `-6.1594` n `189` status `ready` deltaP `-10.1124` edge `-0.0066` maxDD `-10.475`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
