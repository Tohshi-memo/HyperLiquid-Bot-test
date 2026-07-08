# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T15:07:30.005513+00:00`
- Price records: `672`
- Market context records: `6098`
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
- `news_risk_high->crypto_alt_24h` score `7.3493` n `30` status `ready` deltaP `33.9583` edge `0.4008` maxDD `-0.5131`
- `news_risk_high->fx_4h` score `4.2067` n `32` status `ready` deltaP `43.6738` edge `0.064` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3416` n `32` status `ready` deltaP `28.1437` edge `0.0214` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.4678` n `195` status `ready` deltaP `8.7805` edge `0.1555` maxDD `-2.671`
- `news_risk_high->crypto_major_1h` score `1.3088` n `32` status `ready` deltaP `14.128` edge `0.1203` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.7335` n `32` status `ready` deltaP `9.6744` edge `0.0757` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.1086` n `30` status `ready` deltaP `9.2361` edge `0.0395` maxDD `-2.3058`
- `news_risk_high->commodity_24h` score `0.0305` n `30` status `ready` deltaP `16.5278` edge `-0.0871` maxDD `-0.3101`
- `market_context_high->fx_1h` score `-0.3081` n `195` status `ready` deltaP `0.836` edge `-0.0005` maxDD `-0.5659`
- `market_context_high->equity_1h` score `-0.5804` n `195` status `ready` deltaP `1.8363` edge `0.0249` maxDD `-4.2573`
- `market_context_high->metal_4h` score `-0.5959` n `195` status `ready` deltaP `3.847` edge `0.0167` maxDD `-3.4996`
- `news_risk_high->metal_1h` score `-0.6835` n `32` status `ready` deltaP `-1.6467` edge `-0.0269` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.6858` n `195` status `ready` deltaP `3.7379` edge `-0.0022` maxDD `-2.0564`
- `market_context_high->index_4h` score `-0.7409` n `195` status `ready` deltaP `3.6804` edge `0.0269` maxDD `-1.381`
- `market_context_high->commodity_1h` score `-0.7524` n `195` status `ready` deltaP `-1.8394` edge `-0.0058` maxDD `-0.5708`
- `market_context_high->crypto_alt_1h` score `-0.8424` n `195` status `ready` deltaP `4.6584` edge `0.0362` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.8892` n `195` status `ready` deltaP `4.9133` edge `0.03` maxDD `-9.807`
- `news_risk_high->index_1h` score `-1.0509` n `32` status `ready` deltaP `-8.9259` edge `-0.0189` maxDD `-1.1725`
- `market_context_high->index_1h` score `-1.1437` n `195` status `ready` deltaP `-1.8586` edge `0.004` maxDD `-0.9531`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
