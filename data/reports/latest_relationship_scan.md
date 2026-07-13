# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T04:37:26.140792+00:00`
- Price records: `672`
- Market context records: `6570`
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

- `market_context_high->unknown_24h` score `6.2318` n `144` status `ready` deltaP `11.032` edge `0.7758` maxDD `-15.0689`
- `market_context_high->unknown_1h` score `1.7412` n `210` status `ready` deltaP `-5.4291` edge `0.2714` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `1.4061` n `144` status `ready` deltaP `13.3492` edge `0.215` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.3378` n `210` status `ready` deltaP `7.6461` edge `0.0323` maxDD `-6.7936`
- `market_context_high->fx_1h` score `-0.3549` n `210` status `ready` deltaP `0.8583` edge `-0.0005` maxDD `-0.7249`
- `market_context_high->crypto_alt_1h` score `-0.4246` n `210` status `ready` deltaP `6.939` edge `0.0306` maxDD `-5.8368`
- `market_context_high->index_1h` score `-0.5491` n `210` status `ready` deltaP `-0.3807` edge `0.0041` maxDD `-0.7564`
- `market_context_high->commodity_1h` score `-0.5985` n `210` status `ready` deltaP `-0.5589` edge `-0.0047` maxDD `-2.1314`
- `market_context_high->index_4h` score `-1.0117` n `210` status `ready` deltaP `7.7812` edge `0.0064` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-1.1417` n `210` status `ready` deltaP `2.0816` edge `0.002` maxDD `-4.2147`
- `market_context_high->metal_1h` score `-1.2068` n `210` status `ready` deltaP `-2.9783` edge `0.0` maxDD `-2.1239`
- `market_context_high->unknown_4h` score `-1.3543` n `210` status `ready` deltaP `-15.7041` edge `0.2324` maxDD `-10.5788`
- `market_context_high->commodity_4h` score `-1.3707` n `210` status `ready` deltaP `-2.1682` edge `-0.0118` maxDD `-5.6246`
- `market_context_high->crypto_major_4h` score `-1.7293` n `210` status `ready` deltaP `7.8825` edge `0.0572` maxDD `-16.8495`
- `market_context_high->fx_4h` score `-1.7459` n `210` status `ready` deltaP `0.0709` edge `-0.0031` maxDD `-3.3635`
- `market_context_high->crypto_alt_4h` score `-1.8974` n `210` status `ready` deltaP `5.2381` edge `0.062` maxDD `-19.2145`
- `market_context_high->metal_24h` score `-1.9285` n `144` status `ready` deltaP `6.0917` edge `0.0917` maxDD `-5.7746`
- `market_context_high->metal_4h` score `-2.1328` n `210` status `ready` deltaP `-1.3779` edge `0.0218` maxDD `-5.2172`
- `market_context_high->index_24h` score `-3.7353` n `144` status `ready` deltaP `1.4429` edge `0.0012` maxDD `-10.7676`
- `market_context_high->fx_24h` score `-3.8313` n `144` status `ready` deltaP `-4.8143` edge `-0.0056` maxDD `-9.2795`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
