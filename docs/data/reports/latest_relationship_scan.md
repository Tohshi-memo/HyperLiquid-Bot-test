# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T15:22:14.550901+00:00`
- Price records: `672`
- Market context records: `1750`
- Flow alert records: `6938`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8862`

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

- `market_context_high->metal_24h` score `7.1663` n `162` status `ready` deltaP `26.8342` edge `0.6609` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `5.8899` n `196` status `ready` deltaP `20.3615` edge `0.5317` maxDD `-9.1295`
- `market_context_high->index_24h` score `4.2939` n `162` status `ready` deltaP `19.0898` edge `0.3534` maxDD `-4.1604`
- `market_context_high->crypto_major_4h` score `4.2624` n `196` status `ready` deltaP `21.805` edge `0.4504` maxDD `-10.9117`
- `market_context_high->unknown_24h` score `4.1739` n `162` status `ready` deltaP `15.1893` edge `0.7786` maxDD `-35.8966`
- `market_context_high->equity_4h` score `2.9524` n `196` status `ready` deltaP `15.807` edge `0.2501` maxDD `-5.0894`
- `market_context_high->equity_24h` score `2.8882` n `162` status `ready` deltaP `17.3139` edge `0.6151` maxDD `-33.1875`
- `market_context_high->unknown_4h` score `2.8395` n `196` status `ready` deltaP `12.7271` edge `0.3789` maxDD `-11.1695`
- `market_context_high->crypto_alt_1h` score `0.8041` n `196` status `ready` deltaP `7.5706` edge `0.1189` maxDD `-4.1892`
- `market_context_high->index_4h` score `0.8019` n `196` status `ready` deltaP `11.1032` edge `0.1017` maxDD `-3.7119`
- `market_context_high->crypto_major_24h` score `0.6563` n `162` status `ready` deltaP `19.6311` edge `0.7824` maxDD `-62.3533`
- `market_context_high->crypto_major_1h` score `0.2568` n `196` status `ready` deltaP `5.0471` edge `0.0951` maxDD `-3.9211`
- `market_context_high->equity_1h` score `0.0658` n `196` status `ready` deltaP `4.9707` edge `0.0532` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.2083` n `196` status `ready` deltaP `3.767` edge `0.0207` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.2599` n `196` status `ready` deltaP `12.444` edge `0.1529` maxDD `-12.5349`
- `market_context_high->crypto_alt_24h` score `-0.4679` n `162` status `ready` deltaP `20.5073` edge `1.0052` maxDD `-88.8062`
- `market_context_high->metal_1h` score `-0.4793` n `196` status `ready` deltaP `6.3944` edge `0.0295` maxDD `-6.3532`
- `market_context_high->fx_24h` score `-0.6426` n `162` status `ready` deltaP `6.773` edge `0.0062` maxDD `-1.3925`
- `market_context_high->fx_1h` score `-0.6723` n `196` status `ready` deltaP `-3.2659` edge `-0.0012` maxDD `-0.3914`
- `market_context_high->unknown_1h` score `-1.7206` n `196` status `ready` deltaP `0.0397` edge `0.0033` maxDD `-7.7558`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
