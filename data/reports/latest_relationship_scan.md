# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T23:22:48.428950+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7985`

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

- `market_context_high->unknown_4h` score `91.2039` n `153` status `ready` deltaP `1.0172` edge `7.6271` maxDD `-1.0178`
- `market_context_high->unknown_1h` score `21.708` n `153` status `ready` deltaP `1.6242` edge `1.8471` maxDD `-1.5807`
- `market_context_high->fx_1h` score `0.265` n `153` status `ready` deltaP `8.2648` edge `0.0028` maxDD `-0.1986`
- `market_context_high->metal_24h` score `0.2334` n `112` status `ready` deltaP `23.5887` edge `0.1353` maxDD `-7.0108`
- `market_context_high->fx_4h` score `0.1652` n `153` status `ready` deltaP `9.782` edge `0.0084` maxDD `-0.4545`
- `market_context_high->index_24h` score `-0.0324` n `112` status `ready` deltaP `16.3051` edge `0.011` maxDD `-4.5747`
- `market_context_high->metal_1h` score `-0.1423` n `153` status `ready` deltaP `8.1807` edge `0.0064` maxDD `-1.6682`
- `market_context_high->fx_24h` score `-0.1575` n `112` status `ready` deltaP `16.6254` edge `0.0262` maxDD `-1.2451`
- `market_context_high->commodity_1h` score `-0.2426` n `153` status `ready` deltaP `2.452` edge `0.0135` maxDD `-1.0053`
- `market_context_high->commodity_4h` score `-0.431` n `153` status `ready` deltaP `5.9063` edge `0.0476` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.5907` n `153` status `ready` deltaP `-0.137` edge `-0.0011` maxDD `-1.8971`
- `market_context_high->crypto_major_1h` score `-0.8327` n `153` status `ready` deltaP `4.8325` edge `0.0191` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-0.9289` n `153` status `ready` deltaP `7.8172` edge `-0.0002` maxDD `-5.3474`
- `market_context_high->equity_1h` score `-1.8213` n `153` status `ready` deltaP `1.0058` edge `-0.0126` maxDD `-12.2088`
- `market_context_high->crypto_alt_1h` score `-1.9274` n `153` status `ready` deltaP `0.1732` edge `0.0002` maxDD `-13.2099`
- `market_context_high->index_4h` score `-3.3655` n `153` status `ready` deltaP `-5.9272` edge `-0.0233` maxDD `-6.7447`
- `market_context_high->crypto_major_4h` score `-4.4953` n `153` status `ready` deltaP `0.6087` edge `-0.0764` maxDD `-32.9851`
- `market_context_high->crypto_major_24h` score `-4.5011` n `112` status `ready` deltaP `-2.6182` edge `-0.0739` maxDD `-29.1905`
- `market_context_high->commodity_24h` score `-5.996` n `112` status `ready` deltaP `-13.4377` edge `-0.1202` maxDD `-24.0477`
- `market_context_high->equity_24h` score `-6.7779` n `112` status `ready` deltaP `-7.0299` edge `-0.2788` maxDD `-35.4638`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
