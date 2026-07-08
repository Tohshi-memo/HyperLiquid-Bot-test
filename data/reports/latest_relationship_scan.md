# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T16:37:31.143229+00:00`
- Price records: `672`
- Market context records: `6104`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11115`

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

- `news_risk_high->fx_24h` score `8.113` n `30` status `ready` deltaP `72.2222` edge `0.1946` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `8.077` n `30` status `ready` deltaP `35.0` edge `0.4545` maxDD `-0.5131`
- `news_risk_high->fx_4h` score `4.1885` n `32` status `ready` deltaP `43.5213` edge `0.0635` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3164` n `32` status `ready` deltaP `27.8443` edge `0.0213` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.3095` n `32` status `ready` deltaP `14.128` edge `0.1204` maxDD `-2.0691`
- `market_context_high->equity_4h` score `1.217` n `195` status `ready` deltaP `7.8659` edge `0.1407` maxDD `-2.671`
- `news_risk_high->crypto_alt_1h` score `0.7148` n `32` status `ready` deltaP `9.375` edge `0.0753` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.082` n `30` status `ready` deltaP `9.2361` edge `0.0361` maxDD `-2.3058`
- `news_risk_high->commodity_24h` score `-0.2172` n `30` status `ready` deltaP `15.4861` edge `-0.1008` maxDD `-0.3101`
- `market_context_high->fx_1h` score `-0.3245` n `195` status `ready` deltaP `0.5366` edge `-0.0006` maxDD `-0.5659`
- `market_context_high->equity_1h` score `-0.5881` n `195` status `ready` deltaP `1.5369` edge `0.0259` maxDD `-4.2573`
- `market_context_high->metal_4h` score `-0.599` n `195` status `ready` deltaP `3.847` edge `0.0163` maxDD `-3.4996`
- `market_context_high->metal_1h` score `-0.6774` n `195` status `ready` deltaP `3.7379` edge `-0.0015` maxDD `-2.0564`
- `news_risk_high->metal_1h` score `-0.678` n `32` status `ready` deltaP `-1.6467` edge `-0.0262` maxDD `-1.6464`
- `market_context_high->commodity_1h` score `-0.7368` n `195` status `ready` deltaP `-1.6897` edge `-0.0055` maxDD `-0.5708`
- `market_context_high->index_4h` score `-0.8096` n `195` status `ready` deltaP `2.7658` edge `0.0242` maxDD `-1.381`
- `market_context_high->crypto_alt_1h` score `-0.8611` n `195` status `ready` deltaP `4.359` edge `0.0358` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.8884` n `195` status `ready` deltaP `4.9133` edge `0.0301` maxDD `-9.807`
- `news_risk_high->index_1h` score `-1.0688` n `32` status `ready` deltaP `-9.2253` edge `-0.0192` maxDD `-1.1725`
- `market_context_high->index_1h` score `-1.1712` n `195` status `ready` deltaP `-2.158` edge `0.0037` maxDD `-0.9531`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
