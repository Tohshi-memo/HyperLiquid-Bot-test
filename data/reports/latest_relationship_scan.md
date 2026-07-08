# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T08:07:29.594178+00:00`
- Price records: `672`
- Market context records: `6067`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11112`

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

- `news_risk_high->fx_24h` score `8.151` n `30` status `ready` deltaP `72.7431` edge `0.1943` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.4206` n `30` status `ready` deltaP `45.7927` edge `0.0677` maxDD `-0.0345`
- `news_risk_high->crypto_alt_24h` score `3.2476` n `30` status `ready` deltaP `29.0972` edge `0.0914` maxDD `-0.5131`
- `news_risk_high->fx_1h` score `2.4219` n `32` status `ready` deltaP `29.0419` edge `0.0221` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.4967` n `206` status `ready` deltaP `8.9465` edge `0.1568` maxDD `-2.671`
- `news_risk_high->commodity_24h` score `1.4058` n `30` status `ready` deltaP `21.3889` edge `-0.0049` maxDD `-0.3101`
- `news_risk_high->crypto_major_1h` score `1.1411` n `32` status `ready` deltaP `13.5292` edge `0.1028` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.5612` n `32` status `ready` deltaP `8.7762` edge `0.0596` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.0774` n `30` status `ready` deltaP `9.2361` edge `0.0355` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.4501` n `206` status `ready` deltaP `2.9809` edge `0.0023` maxDD `-2.0564`
- `market_context_high->fx_1h` score `-0.545` n `206` status `ready` deltaP `0.1584` edge `-0.0008` maxDD `-0.6538`
- `market_context_high->commodity_1h` score `-0.7482` n `206` status `ready` deltaP `-2.2818` edge `-0.0025` maxDD `-0.5708`
- `market_context_high->crypto_major_1h` score `-0.8457` n `206` status `ready` deltaP `4.7003` edge `0.037` maxDD `-9.807`
- `news_risk_high->metal_1h` score `-0.8464` n `32` status `ready` deltaP `-2.8443` edge `-0.0398` maxDD `-1.6464`
- `market_context_high->crypto_alt_1h` score `-0.8555` n `206` status `ready` deltaP `4.2556` edge `0.0372` maxDD `-9.3536`
- `market_context_high->index_4h` score `-0.9318` n `206` status `ready` deltaP `2.1105` edge `0.0198` maxDD `-1.9335`
- `news_risk_high->index_1h` score `-1.0158` n `32` status `ready` deltaP `-8.3271` edge `-0.0184` maxDD `-1.1725`
- `market_context_high->equity_1h` score `-1.0577` n `206` status `ready` deltaP `0.7805` edge `0.0195` maxDD `-4.3608`
- `market_context_high->metal_4h` score `-1.097` n `206` status `ready` deltaP `3.7237` edge `0.0025` maxDD `-3.4996`
- `market_context_high->index_1h` score `-1.2798` n `206` status `ready` deltaP `-2.8356` edge `0.0021` maxDD `-1.1879`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
