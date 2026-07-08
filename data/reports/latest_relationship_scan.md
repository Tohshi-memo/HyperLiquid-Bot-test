# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T14:22:31.320996+00:00`
- Price records: `672`
- Market context records: `6095`
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
- `news_risk_high->crypto_alt_24h` score `7.022` n `30` status `ready` deltaP `33.4375` edge `0.377` maxDD `-0.5131`
- `news_risk_high->fx_4h` score `4.2469` n `32` status `ready` deltaP `44.1311` edge `0.0643` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3799` n `32` status `ready` deltaP `28.5928` edge `0.0216` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.5944` n `195` status `ready` deltaP `9.2378` edge `0.163` maxDD `-2.671`
- `news_risk_high->crypto_major_1h` score `1.2503` n `32` status `ready` deltaP `13.6789` edge `0.1158` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.6985` n `32` status `ready` deltaP `9.375` edge `0.0732` maxDD `-1.6923`
- `news_risk_high->commodity_24h` score `0.1694` n `30` status `ready` deltaP `17.0486` edge `-0.079` maxDD `-0.3101`
- `news_risk_high->index_24h` score `0.1187` n `30` status `ready` deltaP `9.2361` edge `0.0408` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.2832` n `195` status `ready` deltaP `1.2851` edge `-0.0003` maxDD `-0.5659`
- `market_context_high->metal_4h` score `-0.5873` n `195` status `ready` deltaP `3.847` edge `0.0178` maxDD `-3.4996`
- `market_context_high->equity_1h` score `-0.6201` n `195` status `ready` deltaP `1.5369` edge `0.0218` maxDD `-4.2573`
- `news_risk_high->metal_1h` score `-0.6959` n `32` status `ready` deltaP `-1.7964` edge `-0.0275` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.705` n `195` status `ready` deltaP `3.5882` edge `-0.0028` maxDD `-2.0564`
- `market_context_high->index_4h` score `-0.7055` n `195` status `ready` deltaP `4.1377` edge `0.0284` maxDD `-1.381`
- `market_context_high->commodity_1h` score `-0.7068` n `195` status `ready` deltaP `-1.54` edge `-0.004` maxDD `-0.5708`
- `market_context_high->crypto_alt_1h` score `-0.8774` n `195` status `ready` deltaP `4.359` edge `0.0337` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.9476` n `195` status `ready` deltaP `4.4642` edge `0.0255` maxDD `-9.807`
- `news_risk_high->index_1h` score `-1.0688` n `32` status `ready` deltaP `-9.2253` edge `-0.0192` maxDD `-1.1725`
- `market_context_high->index_1h` score `-1.1712` n `195` status `ready` deltaP `-2.158` edge `0.0037` maxDD `-0.9531`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
