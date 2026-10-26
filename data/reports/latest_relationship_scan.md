# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T19:37:29.582430+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8128`

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

- `market_context_high->unknown_4h` score `93.4671` n `153` status `ready` deltaP `1.0172` edge `7.8157` maxDD `-1.0178`
- `market_context_high->unknown_1h` score `28.494` n `153` status `ready` deltaP `1.6242` edge `2.4126` maxDD `-1.5807`
- `market_context_high->metal_24h` score `0.3523` n `112` status `ready` deltaP `24.9752` edge `0.1413` maxDD `-7.0108`
- `market_context_high->fx_1h` score `0.2662` n `153` status `ready` deltaP `8.2648` edge `0.0029` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.0994` n `153` status `ready` deltaP `9.0198` edge `0.008` maxDD `-0.4545`
- `market_context_high->index_24h` score `-0.0082` n `112` status `ready` deltaP `16.3051` edge `0.0141` maxDD `-4.5747`
- `market_context_high->metal_1h` score `-0.1213` n `153` status `ready` deltaP `8.4801` edge `0.0071` maxDD `-1.6682`
- `market_context_high->fx_24h` score `-0.1846` n `112` status `ready` deltaP `16.1055` edge `0.0262` maxDD `-1.2451`
- `market_context_high->commodity_1h` score `-0.2762` n `153` status `ready` deltaP `2.1526` edge `0.0127` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.5595` n `153` status `ready` deltaP `0.4618` edge `-0.0011` maxDD `-1.8971`
- `market_context_high->commodity_4h` score `-0.7276` n `153` status `ready` deltaP `3.9245` edge `0.0361` maxDD `-1.165`
- `market_context_high->crypto_major_1h` score `-0.8943` n `153` status `ready` deltaP `4.084` edge `0.0162` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-0.9361` n `153` status `ready` deltaP `7.6648` edge `-0.0001` maxDD `-5.3474`
- `market_context_high->equity_1h` score `-1.7879` n `153` status `ready` deltaP `1.7543` edge `-0.0133` maxDD `-12.2088`
- `market_context_high->crypto_alt_1h` score `-2.003` n `153` status `ready` deltaP `-0.725` edge `-0.0035` maxDD `-13.2099`
- `market_context_high->index_4h` score `-3.3533` n `153` status `ready` deltaP `-5.7747` edge `-0.0233` maxDD `-6.7447`
- `market_context_high->crypto_major_24h` score `-4.427` n `112` status `ready` deltaP `-2.6182` edge `-0.0644` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-4.5881` n `153` status `ready` deltaP `-0.3059` edge `-0.0822` maxDD `-32.9851`
- `market_context_high->equity_24h` score `-6.2379` n `112` status `ready` deltaP `-4.4302` edge `-0.2269` maxDD `-35.4638`
- `market_context_high->commodity_24h` score `-6.2435` n `112` status `ready` deltaP `-16.0373` edge `-0.1346` maxDD `-24.0477`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
