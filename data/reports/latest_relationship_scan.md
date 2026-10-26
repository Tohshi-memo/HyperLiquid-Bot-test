# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T18:37:28.737199+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8092`

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

- `market_context_high->unknown_4h` score `93.3767` n `153` status `ready` deltaP `0.7124` edge `7.8102` maxDD `-1.0178`
- `market_context_high->unknown_1h` score `28.3405` n `153` status `ready` deltaP `1.4745` edge `2.4008` maxDD `-1.5807`
- `market_context_high->metal_24h` score `0.3918` n `112` status `ready` deltaP `25.4951` edge `0.1429` maxDD `-7.0108`
- `market_context_high->fx_1h` score `0.2422` n `153` status `ready` deltaP `7.9654` edge `0.0029` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.1018` n `153` status `ready` deltaP `9.0198` edge `0.0082` maxDD `-0.4545`
- `market_context_high->index_24h` score `-0.0051` n `112` status `ready` deltaP `16.3051` edge `0.0145` maxDD `-4.5747`
- `market_context_high->metal_1h` score `-0.1322` n `153` status `ready` deltaP `8.3304` edge `0.0067` maxDD `-1.6682`
- `market_context_high->fx_24h` score `-0.1454` n `112` status `ready` deltaP `16.7987` edge `0.0266` maxDD `-1.2451`
- `market_context_high->commodity_1h` score `-0.275` n `153` status `ready` deltaP `2.1526` edge `0.0128` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.5681` n `153` status `ready` deltaP `0.3121` edge `-0.0012` maxDD `-1.8971`
- `market_context_high->commodity_4h` score `-0.685` n `153` status `ready` deltaP `4.3819` edge `0.0366` maxDD `-1.165`
- `market_context_high->crypto_major_1h` score `-0.9293` n `153` status `ready` deltaP `3.7846` edge `0.0137` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-0.9479` n `153` status `ready` deltaP `7.5123` edge `-0.0006` maxDD `-5.3474`
- `market_context_high->equity_1h` score `-1.7933` n `153` status `ready` deltaP `1.7543` edge `-0.014` maxDD `-12.2088`
- `market_context_high->crypto_alt_1h` score `-2.0232` n `153` status `ready` deltaP `-0.8747` edge `-0.0051` maxDD `-13.2099`
- `market_context_high->index_4h` score `-3.3813` n `153` status `ready` deltaP `-6.0796` edge `-0.0236` maxDD `-6.7447`
- `market_context_high->crypto_major_24h` score `-4.4247` n `112` status `ready` deltaP `-2.6182` edge `-0.0641` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-4.6557` n `153` status `ready` deltaP `-0.9156` edge `-0.0868` maxDD `-32.9851`
- `market_context_high->equity_24h` score `-6.1192` n `112` status `ready` deltaP `-3.737` edge `-0.2163` maxDD `-35.4638`
- `market_context_high->commodity_24h` score `-6.3037` n `112` status `ready` deltaP `-16.7306` edge `-0.1377` maxDD `-24.0477`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
