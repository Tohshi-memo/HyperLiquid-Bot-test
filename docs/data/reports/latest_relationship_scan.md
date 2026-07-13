# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T02:07:29.095040+00:00`
- Price records: `672`
- Market context records: `6562`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9872`

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

- `market_context_high->unknown_24h` score `6.2554` n `144` status `ready` deltaP `11.0269` edge `0.7778` maxDD `-15.0689`
- `market_context_high->unknown_1h` score `1.7807` n `210` status `ready` deltaP `-4.8303` edge `0.2707` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `1.3875` n `144` status `ready` deltaP `13.4773` edge `0.2126` maxDD `-5.2791`
- `market_context_high->index_4h` score `-0.2378` n `202` status `ready` deltaP `10.0504` edge `0.0181` maxDD `-2.5801`
- `market_context_high->fx_1h` score `-0.3464` n `210` status `ready` deltaP `1.008` edge `-0.0004` maxDD `-0.7249`
- `market_context_high->crypto_major_1h` score `-0.4088` n `210` status `ready` deltaP `7.197` edge `0.0262` maxDD `-6.7936`
- `market_context_high->crypto_alt_1h` score `-0.4651` n `210` status `ready` deltaP `6.7893` edge `0.0264` maxDD `-5.8368`
- `market_context_high->crypto_alt_4h` score `-0.5488` n `202` status `ready` deltaP `7.2733` edge `0.0903` maxDD `-11.0654`
- `market_context_high->index_1h` score `-0.5771` n `210` status `ready` deltaP `-0.8298` edge `0.0035` maxDD `-0.7564`
- `market_context_high->commodity_1h` score `-0.5915` n `210` status `ready` deltaP `-0.4092` edge `-0.0048` maxDD `-2.1314`
- `market_context_high->crypto_major_4h` score `-0.7566` n `202` status `ready` deltaP `9.978` edge `0.0822` maxDD `-12.6576`
- `market_context_high->equity_1h` score `-1.1513` n `210` status `ready` deltaP `2.0816` edge `0.0012` maxDD `-4.2147`
- `market_context_high->metal_1h` score `-1.2284` n `210` status `ready` deltaP `-3.128` edge `-0.0008` maxDD `-2.1239`
- `market_context_high->unknown_4h` score `-1.2467` n `202` status `ready` deltaP `-16.7139` edge `0.2481` maxDD `-10.5788`
- `market_context_high->commodity_4h` score `-1.4216` n `202` status `ready` deltaP `-2.8617` edge `-0.0137` maxDD `-5.6246`
- `market_context_high->metal_4h` score `-1.5674` n `202` status `ready` deltaP `0.0453` edge `0.0306` maxDD `-3.5485`
- `market_context_high->equity_4h` score `-1.8361` n `202` status `ready` deltaP `8.1502` edge `0.0184` maxDD `-12.726`
- `market_context_high->metal_24h` score `-1.9745` n `144` status `ready` deltaP `5.966` edge `0.0887` maxDD `-5.7746`
- `market_context_high->fx_4h` score `-2.864` n `202` status `ready` deltaP `-1.6738` edge `-0.0063` maxDD `-3.3635`
- `market_context_high->index_24h` score `-3.8122` n `144` status `ready` deltaP `1.2914` edge `-0.0042` maxDD `-10.7676`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
