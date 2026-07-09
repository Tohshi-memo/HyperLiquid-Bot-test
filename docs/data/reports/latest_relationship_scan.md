# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-09T21:07:41.723528+00:00`
- Price records: `672`
- Market context records: `6218`
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

- `news_risk_high->crypto_alt_24h` score `13.1666` n `32` status `ready` deltaP `42.2194` edge `0.8305` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.517` n `32` status `ready` deltaP `56.2925` edge `0.1678` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1257` n `32` status `ready` deltaP `43.2165` edge `0.0603` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `2.475` n `32` status `ready` deltaP `15.625` edge `0.2911` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.3332` n `32` status `ready` deltaP `28.1437` edge `0.0207` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.904` n `192` status `ready` deltaP `1.812` edge `0.2474` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.3984` n `32` status `ready` deltaP `14.2777` edge `0.1308` maxDD `-2.0691`
- `news_risk_high->commodity_24h` score `1.1674` n `32` status `ready` deltaP `20.5995` edge `-0.0195` maxDD `-0.3101`
- `news_risk_high->crypto_alt_1h` score `0.7538` n `32` status `ready` deltaP `9.9738` edge `0.0763` maxDD `-1.6923`
- `market_context_high->unknown_4h` score `0.4483` n `192` status `ready` deltaP `-2.1469` edge `0.3049` maxDD `-11.925`
- `market_context_high->metal_24h` score `-0.0447` n `192` status `ready` deltaP `19.8023` edge `0.1191` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.2331` n `32` status `ready` deltaP `8.801` edge `-0.0014` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.3003` n `192` status `ready` deltaP `1.0604` edge `-0.001` maxDD `-0.5659`
- `market_context_high->commodity_1h` score `-0.5703` n `192` status `ready` deltaP `-0.7485` edge `0.0021` maxDD `-0.5708`
- `market_context_high->metal_4h` score `-0.6836` n `192` status `ready` deltaP `3.0615` edge `0.0107` maxDD `-3.4996`
- `news_risk_high->metal_1h` score `-0.7909` n `32` status `ready` deltaP `-3.5928` edge `-0.0277` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.876` n `192` status `ready` deltaP `1.6155` edge `-0.0039` maxDD `-2.0564`
- `market_context_high->crypto_major_1h` score `-0.9012` n `192` status `ready` deltaP `4.3819` edge `0.032` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-0.9099` n `192` status `ready` deltaP `4.2446` edge `0.0303` maxDD `-9.3536`
- `market_context_high->equity_1h` score `-1.1227` n `192` status `ready` deltaP `-3.0127` edge `-0.0123` maxDD `-4.2573`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
