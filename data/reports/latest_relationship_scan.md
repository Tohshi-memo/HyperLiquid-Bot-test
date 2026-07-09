# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-09T14:37:30.074100+00:00`
- Price records: `672`
- Market context records: `6190`
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

- `news_risk_high->crypto_alt_24h` score `12.6806` n `32` status `ready` deltaP `42.2194` edge `0.79` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.9331` n `32` status `ready` deltaP `60.7143` edge `0.173` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.0703` n `32` status `ready` deltaP `42.4487` edge `0.0608` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3212` n `32` status `ready` deltaP `27.994` edge `0.0207` maxDD `-0.1113`
- `news_risk_high->crypto_major_24h` score `2.0733` n `32` status `ready` deltaP `15.625` edge `0.2396` maxDD `-4.2368`
- `market_context_high->unknown_1h` score `1.8141` n `192` status `ready` deltaP `0.9138` edge `0.2459` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.3797` n `32` status `ready` deltaP `14.2777` edge `0.1284` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.7141` n `32` status `ready` deltaP `9.0756` edge `0.0772` maxDD `-1.6923`
- `market_context_high->unknown_4h` score `0.3612` n `192` status `ready` deltaP `-1.8253` edge `0.2955` maxDD `-11.925`
- `market_context_high->metal_24h` score `0.0684` n `192` status `ready` deltaP `19.8023` edge `0.1336` maxDD `-11.8809`
- `news_risk_high->commodity_24h` score `-0.0011` n `32` status `ready` deltaP `16.1777` edge `-0.0874` maxDD `-0.3101`
- `news_risk_high->index_24h` score `-0.1548` n `32` status `ready` deltaP `9.4813` edge `0.0041` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.2348` n `192` status `ready` deltaP `1.9282` edge `0.0593` maxDD `-2.671`
- `market_context_high->fx_1h` score `-0.3081` n `192` status `ready` deltaP `0.9107` edge `-0.001` maxDD `-0.5659`
- `market_context_high->metal_4h` score `-0.6496` n `192` status `ready` deltaP `3.5351` edge `0.0119` maxDD `-3.4996`
- `market_context_high->commodity_1h` score `-0.786` n `192` status `ready` deltaP `-2.6946` edge `-0.0029` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.8384` n `32` status `ready` deltaP `-4.0419` edge `-0.0308` maxDD `-1.6464`
- `market_context_high->crypto_major_1h` score `-0.9199` n `192` status `ready` deltaP `4.3819` edge `0.0296` maxDD `-9.807`
- `market_context_high->metal_1h` score `-0.9491` n `192` status `ready` deltaP `1.1664` edge `-0.007` maxDD `-2.0564`
- `market_context_high->crypto_alt_1h` score `-0.9496` n `192` status `ready` deltaP `3.3464` edge `0.0312` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
