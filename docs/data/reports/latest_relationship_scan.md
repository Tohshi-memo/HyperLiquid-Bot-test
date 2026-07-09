# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-09T17:38:14.920541+00:00`
- Price records: `672`
- Market context records: `6202`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11110`

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

- `news_risk_high->crypto_alt_24h` score `12.8102` n `32` status `ready` deltaP `42.2194` edge `0.8008` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.7351` n `32` status `ready` deltaP `58.6735` edge `0.1701` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.0478` n `32` status `ready` deltaP `42.3018` edge `0.0599` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.2985` n `32` status `ready` deltaP `27.6946` edge `0.0208` maxDD `-0.1113`
- `news_risk_high->crypto_major_24h` score `2.2106` n `32` status `ready` deltaP `15.625` edge `0.2572` maxDD `-4.2368`
- `market_context_high->unknown_1h` score `1.8908` n `192` status `ready` deltaP `1.6623` edge `0.2473` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.3977` n `32` status `ready` deltaP `14.2777` edge `0.1307` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.7374` n `32` status `ready` deltaP `9.5247` edge `0.0772` maxDD `-1.6923`
- `news_risk_high->commodity_24h` score `0.5762` n `32` status `ready` deltaP `18.2185` edge `-0.0529` maxDD `-0.3101`
- `market_context_high->unknown_4h` score `0.2013` n `192` status `ready` deltaP `-2.9091` edge `0.2894` maxDD `-11.925`
- `market_context_high->metal_24h` score `-0.026` n `192` status `ready` deltaP `19.8023` edge `0.1215` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.2596` n `32` status `ready` deltaP `8.801` edge `-0.0048` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.3229` n `192` status `ready` deltaP `0.6113` edge `-0.0009` maxDD `-0.5659`
- `market_context_high->commodity_1h` score `-0.6614` n `192` status `ready` deltaP `-1.6467` edge `0.0005` maxDD `-0.5708`
- `market_context_high->metal_4h` score `-0.7567` n `192` status `ready` deltaP `2.2993` edge `0.0064` maxDD `-3.4996`
- `news_risk_high->metal_1h` score `-0.7979` n `32` status `ready` deltaP `-3.5928` edge `-0.0286` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.8868` n `192` status `ready` deltaP `1.6155` edge `-0.0048` maxDD `-2.0564`
- `market_context_high->crypto_major_1h` score `-0.902` n `192` status `ready` deltaP `4.3819` edge `0.0319` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-0.9263` n `192` status `ready` deltaP `3.7955` edge `0.0312` maxDD `-9.3536`
- `market_context_high->equity_1h` score `-1.0689` n `192` status `ready` deltaP `-2.7133` edge `-0.0074` maxDD `-4.2573`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
