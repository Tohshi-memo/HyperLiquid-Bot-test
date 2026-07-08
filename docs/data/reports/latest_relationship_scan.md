# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T17:07:27.432624+00:00`
- Price records: `672`
- Market context records: `6106`
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

- `news_risk_high->crypto_alt_24h` score `8.3268` n `30` status `ready` deltaP `35.3472` edge `0.473` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `8.0804` n `30` status `ready` deltaP `71.875` edge `0.1942` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1861` n `32` status `ready` deltaP `43.5213` edge `0.0633` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3045` n `32` status `ready` deltaP `27.6946` edge `0.0213` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.3056` n `32` status `ready` deltaP `14.128` edge `0.1199` maxDD `-2.0691`
- `market_context_high->equity_4h` score `1.129` n `195` status `ready` deltaP `7.561` edge `0.1354` maxDD `-2.671`
- `news_risk_high->crypto_alt_1h` score `0.7047` n `32` status `ready` deltaP `9.375` edge `0.074` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.0696` n `30` status `ready` deltaP `9.2361` edge `0.0345` maxDD `-2.3058`
- `news_risk_high->commodity_24h` score `-0.2834` n `30` status `ready` deltaP `15.1389` edge `-0.104` maxDD `-0.3101`
- `market_context_high->fx_1h` score `-0.3322` n `195` status `ready` deltaP `0.3869` edge `-0.0006` maxDD `-0.5659`
- `market_context_high->metal_4h` score `-0.6037` n `195` status `ready` deltaP `3.847` edge `0.0157` maxDD `-3.4996`
- `market_context_high->equity_1h` score `-0.6248` n `195` status `ready` deltaP `1.2375` edge `0.0232` maxDD `-4.2573`
- `news_risk_high->metal_1h` score `-0.7014` n `32` status `ready` deltaP `-1.9461` edge `-0.0272` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.7134` n `195` status `ready` deltaP `3.4385` edge `-0.0025` maxDD `-2.0564`
- `market_context_high->commodity_1h` score `-0.7248` n `195` status `ready` deltaP `-1.6897` edge `-0.0045` maxDD `-0.5708`
- `market_context_high->index_4h` score `-0.8332` n `195` status `ready` deltaP `2.4609` edge `0.0232` maxDD `-1.381`
- `market_context_high->crypto_alt_1h` score `-0.8712` n `195` status `ready` deltaP `4.359` edge `0.0345` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.8923` n `195` status `ready` deltaP `4.9133` edge `0.0296` maxDD `-9.807`
- `news_risk_high->index_1h` score `-1.0898` n `32` status `ready` deltaP `-9.5247` edge `-0.0199` maxDD `-1.1725`
- `market_context_high->index_1h` score `-1.2036` n `195` status `ready` deltaP `-2.4574` edge `0.003` maxDD `-0.9531`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
