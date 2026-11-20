# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-20T16:37:43.299373+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2726`

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

- `market_context_high->unknown_1h` score `10173.7612` n `126` status `ready` deltaP `1.9129` edge `847.8205` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6612.8137` n `120` status `ready` deltaP `0.6504` edge `551.0919` maxDD `-0.6076`
- `market_context_high->crypto_major_24h` score `4.809` n `107` status `ready` deltaP `27.4257` edge `1.1467` maxDD `-50.7065`
- `market_context_high->crypto_alt_24h` score `1.6067` n `107` status `ready` deltaP `14.3156` edge `0.9505` maxDD `-66.63`
- `market_context_high->metal_4h` score `-0.0577` n `120` status `ready` deltaP `14.4817` edge `0.0478` maxDD `-7.8056`
- `market_context_high->metal_1h` score `-0.1813` n `126` status `ready` deltaP `4.251` edge `0.0149` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.3217` n `126` status `ready` deltaP `2.7088` edge `0.0019` maxDD `-1.2295`
- `market_context_high->crypto_major_4h` score `-0.9878` n `120` status `ready` deltaP `2.0223` edge `0.2609` maxDD `-25.7488`
- `market_context_high->fx_1h` score `-1.3579` n `126` status `ready` deltaP `-8.3571` edge `-0.0015` maxDD `-0.4757`
- `market_context_high->crypto_alt_4h` score `-1.7412` n `120` status `ready` deltaP `3.0894` edge `0.1788` maxDD `-27.8101`
- `market_context_high->index_4h` score `-1.9439` n `120` status `ready` deltaP `-2.3069` edge `-0.0093` maxDD `-4.9851`
- `market_context_high->equity_1h` score `-1.9955` n `126` status `ready` deltaP `5.5389` edge `0.0027` maxDD `-13.1399`
- `market_context_high->fx_4h` score `-2.0469` n `120` status `ready` deltaP `-9.0345` edge `-0.0006` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.1157` n `126` status `ready` deltaP `-6.7247` edge `-0.0183` maxDD `-4.3877`
- `market_context_high->crypto_major_1h` score `-2.5422` n `126` status `ready` deltaP `2.11` edge `0.0059` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-3.1188` n `126` status `ready` deltaP `-3.4455` edge `-0.0092` maxDD `-13.8848`
- `market_context_high->metal_24h` score `-5.7946` n `107` status `ready` deltaP `13.2139` edge `0.102` maxDD `-43.8379`
- `market_context_high->fx_24h` score `-6.6679` n `107` status `ready` deltaP `-17.7521` edge `-0.01` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-7.0219` n `120` status `ready` deltaP `-21.311` edge `-0.0738` maxDD `-15.5426`
- `market_context_high->equity_4h` score `-11.2007` n `120` status `ready` deltaP `-5.3862` edge `-0.0965` maxDD `-53.7455`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
