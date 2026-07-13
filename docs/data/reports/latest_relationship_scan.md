# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T05:37:31.111320+00:00`
- Price records: `672`
- Market context records: `6574`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9904`

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

- `market_context_high->unknown_24h` score `6.2066` n `144` status `ready` deltaP `11.032` edge `0.7737` maxDD `-15.0689`
- `market_context_high->unknown_1h` score `1.746` n `210` status `ready` deltaP `-5.4291` edge `0.2718` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `1.4181` n `144` status `ready` deltaP `13.3492` edge `0.216` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.3293` n `210` status `ready` deltaP `1.3074` edge `-0.0002` maxDD `-0.7249`
- `market_context_high->crypto_major_1h` score `-0.3752` n `210` status `ready` deltaP `7.3467` edge `0.0295` maxDD `-6.7936`
- `market_context_high->crypto_alt_1h` score `-0.4854` n `210` status `ready` deltaP `6.3402` edge `0.0268` maxDD `-5.8368`
- `market_context_high->index_1h` score `-0.5631` n `210` status `ready` deltaP `-0.5304` edge `0.0033` maxDD `-0.7564`
- `market_context_high->commodity_1h` score `-0.6048` n `210` status `ready` deltaP `-0.7086` edge `-0.0045` maxDD `-2.1314`
- `market_context_high->index_4h` score `-0.9944` n `210` status `ready` deltaP `7.9332` edge `0.0076` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-1.2064` n `210` status `ready` deltaP `1.7822` edge `-0.0014` maxDD `-4.2147`
- `market_context_high->metal_1h` score `-1.2716` n `210` status `ready` deltaP `-3.5771` edge `-0.0014` maxDD `-2.1239`
- `market_context_high->commodity_4h` score `-1.3518` n `210` status `ready` deltaP `-1.8642` edge `-0.0114` maxDD `-5.6246`
- `market_context_high->unknown_4h` score `-1.5343` n `210` status `ready` deltaP `-15.7041` edge `0.2174` maxDD `-10.5788`
- `market_context_high->crypto_major_4h` score `-1.7168` n `210` status `ready` deltaP `7.8825` edge `0.0588` maxDD `-16.8495`
- `market_context_high->fx_4h` score `-1.7546` n `210` status `ready` deltaP `-0.0811` edge `-0.0032` maxDD `-3.3635`
- `market_context_high->crypto_alt_4h` score `-1.9029` n `210` status `ready` deltaP `5.2381` edge `0.0613` maxDD `-19.2145`
- `market_context_high->metal_24h` score `-1.9369` n `144` status `ready` deltaP `6.0917` edge `0.091` maxDD `-5.7746`
- `market_context_high->metal_4h` score `-2.1429` n `210` status `ready` deltaP `-1.3779` edge `0.0205` maxDD `-5.2172`
- `market_context_high->index_24h` score `-3.7113` n `144` status `ready` deltaP `1.4429` edge `0.0032` maxDD `-10.7676`
- `market_context_high->fx_24h` score `-3.8289` n `144` status `ready` deltaP `-4.8143` edge `-0.0053` maxDD `-9.2795`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
