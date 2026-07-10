# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T08:07:32.172043+00:00`
- Price records: `672`
- Market context records: `6264`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11096`

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

- `news_risk_high->crypto_alt_24h` score `14.8434` n `32` status `ready` deltaP `42.7191` edge `0.9669` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `5.9606` n `32` status `ready` deltaP `50.6873` edge `0.1588` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1793` n `32` status `ready` deltaP `43.8262` edge `0.0607` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `3.7818` n `32` status `ready` deltaP `16.1405` edge `0.4552` maxDD `-4.2368`
- `news_risk_high->commodity_24h` score `2.4743` n `32` status `ready` deltaP `25.9558` edge `0.0537` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.344` n `32` status `ready` deltaP `28.1437` edge `0.0216` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `2.1645` n `195` status `ready` deltaP `2.5787` edge `0.264` maxDD `-3.7317`
- `market_context_high->unknown_4h` score `1.3855` n `192` status `ready` deltaP `-1.2322` edge `0.3769` maxDD `-11.925`
- `news_risk_high->crypto_major_1h` score `1.3712` n `32` status `ready` deltaP `14.128` edge `0.1283` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.7951` n `32` status `ready` deltaP `10.5726` edge `0.0776` maxDD `-1.6923`
- `news_risk_high->index_24h` score `-0.1534` n `32` status `ready` deltaP `9.3428` edge `0.0052` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.1829` n `192` status `ready` deltaP `4.497` edge `0.0465` maxDD `-2.671`
- `market_context_high->fx_1h` score `-0.2775` n `195` status `ready` deltaP `1.3488` edge `0.0` maxDD `-0.5659`
- `market_context_high->metal_24h` score `-0.3204` n `192` status `ready` deltaP `17.6493` edge `0.0981` maxDD `-11.8809`
- `market_context_high->commodity_1h` score `-0.3842` n `195` status `ready` deltaP `-0.7692` edge `0.0016` maxDD `-0.6583`
- `market_context_high->metal_4h` score `-0.5048` n `192` status `ready` deltaP `4.1286` edge `0.0265` maxDD `-3.4996`
- `news_risk_high->metal_1h` score `-0.7029` n `32` status `ready` deltaP `-2.3952` edge `-0.0244` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.817` n `195` status `ready` deltaP `1.9638` edge `-0.0013` maxDD `-2.0564`
- `market_context_high->crypto_alt_1h` score `-0.8277` n `195` status `ready` deltaP `5.5566` edge `0.0321` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.9488` n `195` status `ready` deltaP `3.8876` edge `0.0292` maxDD `-9.807`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
