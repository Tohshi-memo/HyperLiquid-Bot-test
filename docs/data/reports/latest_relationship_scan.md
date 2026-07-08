# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T14:37:32.690765+00:00`
- Price records: `672`
- Market context records: `6096`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11111`

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

- `news_risk_high->fx_24h` score `8.163` n `30` status `ready` deltaP `72.7431` edge `0.1953` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `7.1271` n `30` status `ready` deltaP `33.6111` edge `0.3846` maxDD `-0.5131`
- `news_risk_high->fx_4h` score `4.2335` n `32` status `ready` deltaP `43.9787` edge `0.0642` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3668` n `32` status `ready` deltaP `28.4431` edge `0.0215` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.5462` n `195` status `ready` deltaP `9.0854` edge `0.16` maxDD `-2.671`
- `news_risk_high->crypto_major_1h` score `1.2729` n `32` status `ready` deltaP `13.8286` edge `0.1177` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.7047` n `32` status `ready` deltaP `9.375` edge `0.074` maxDD `-1.6923`
- `news_risk_high->commodity_24h` score `0.1219` n `30` status `ready` deltaP `16.875` edge `-0.0818` maxDD `-0.3101`
- `news_risk_high->index_24h` score `0.1156` n `30` status `ready` deltaP `9.2361` edge `0.0404` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.2918` n `195` status `ready` deltaP `1.1354` edge `-0.0004` maxDD `-0.5659`
- `market_context_high->metal_4h` score `-0.5928` n `195` status `ready` deltaP `3.847` edge `0.0171` maxDD `-3.4996`
- `market_context_high->equity_1h` score `-0.6178` n `195` status `ready` deltaP `1.5369` edge `0.0221` maxDD `-4.2573`
- `news_risk_high->metal_1h` score `-0.6967` n `32` status `ready` deltaP `-1.7964` edge `-0.0276` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.7062` n `195` status `ready` deltaP `3.5882` edge `-0.0029` maxDD `-2.0564`
- `market_context_high->index_4h` score `-0.7181` n `195` status `ready` deltaP `3.9853` edge `0.0278` maxDD `-1.381`
- `market_context_high->commodity_1h` score `-0.7272` n `195` status `ready` deltaP `-1.6897` edge `-0.0047` maxDD `-0.5708`
- `market_context_high->crypto_alt_1h` score `-0.8712` n `195` status `ready` deltaP `4.359` edge `0.0345` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.925` n `195` status `ready` deltaP `4.6139` edge `0.0274` maxDD `-9.807`
- `news_risk_high->index_1h` score `-1.0688` n `32` status `ready` deltaP `-9.2253` edge `-0.0192` maxDD `-1.1725`
- `market_context_high->index_1h` score `-1.1712` n `195` status `ready` deltaP `-2.158` edge `0.0037` maxDD `-0.9531`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
