# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T04:37:16.676469+00:00`
- Price records: `672`
- Market context records: `1186`
- Flow alert records: `5319`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8768`

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

- `market_context_high->crypto_major_24h` score `18.6717` n `143` status `ready` deltaP `44.4105` edge `1.3731` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `8.2094` n `143` status `ready` deltaP `22.2077` edge `0.7377` maxDD `-15.1306`
- `market_context_high->metal_24h` score `4.3587` n `143` status `ready` deltaP `-2.9332` edge `0.5495` maxDD `-6.3373`
- `market_context_high->unknown_4h` score `2.7708` n `143` status `ready` deltaP `5.0924` edge `0.3186` maxDD `-6.7322`
- `market_context_high->equity_4h` score `2.7605` n `143` status `ready` deltaP `14.8154` edge `0.1976` maxDD `-3.6396`
- `market_context_high->index_24h` score `2.5568` n `143` status `ready` deltaP `15.2098` edge `0.2203` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.4872` n `143` status `ready` deltaP `15.5473` edge `0.3363` maxDD `-14.2815`
- `market_context_high->index_4h` score `1.121` n `143` status `ready` deltaP `10.5929` edge `0.0911` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.6944` n `143` status `ready` deltaP `9.8038` edge `0.0242` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.2942` n `143` status `ready` deltaP `2.8621` edge `0.0432` maxDD `-1.3546`
- `market_context_high->fx_1h` score `-0.0483` n `143` status `ready` deltaP `5.9975` edge `-0.0006` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `-0.1424` n `143` status `ready` deltaP `7.0741` edge `0.1267` maxDD `-8.3693`
- `market_context_high->crypto_major_1h` score `-0.2831` n `143` status `ready` deltaP `4.0472` edge `0.0133` maxDD `-4.1256`
- `market_context_high->metal_1h` score `-0.2981` n `143` status `ready` deltaP `7.349` edge `-0.0128` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.4704` n `143` status `ready` deltaP `-0.3946` edge `0.0266` maxDD `-3.4088`
- `market_context_high->fx_24h` score `-0.7224` n `143` status `ready` deltaP `6.0752` edge `0.0282` maxDD `-7.9051`
- `market_context_high->fx_4h` score `-1.0169` n `143` status `ready` deltaP `-4.7437` edge `-0.0058` maxDD `-1.1026`
- `market_context_high->commodity_1h` score `-1.0239` n `143` status `ready` deltaP `-3.6965` edge `0.0008` maxDD `-2.252`
- `market_context_high->crypto_alt_4h` score `-1.3609` n `143` status `ready` deltaP `3.0019` edge `0.102` maxDD `-16.7194`
- `market_context_high->commodity_24h` score `-1.5087` n `143` status `ready` deltaP `-5.1379` edge `0.4269` maxDD `-41.8856`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
