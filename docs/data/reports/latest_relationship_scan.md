# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T19:52:30.573380+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8162`

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

- `market_context_high->unknown_4h` score `93.3399` n `153` status `ready` deltaP `1.0172` edge `7.8051` maxDD `-1.0178`
- `market_context_high->unknown_1h` score `27.0636` n `153` status `ready` deltaP `1.6242` edge `2.2934` maxDD `-1.5807`
- `market_context_high->metal_24h` score `0.3409` n `112` status `ready` deltaP `24.8019` edge `0.141` maxDD `-7.0108`
- `market_context_high->fx_1h` score `0.2662` n `153` status `ready` deltaP `8.2648` edge `0.0029` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.0982` n `153` status `ready` deltaP `9.0198` edge `0.0079` maxDD `-0.4545`
- `market_context_high->index_24h` score `-0.009` n `112` status `ready` deltaP `16.3051` edge `0.014` maxDD `-4.5747`
- `market_context_high->metal_1h` score `-0.1213` n `153` status `ready` deltaP `8.4801` edge `0.0071` maxDD `-1.6682`
- `market_context_high->fx_24h` score `-0.1943` n `112` status `ready` deltaP `15.9321` edge `0.0261` maxDD `-1.2451`
- `market_context_high->commodity_1h` score `-0.2762` n `153` status `ready` deltaP `2.1526` edge `0.0127` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.5588` n `153` status `ready` deltaP `0.4618` edge `-0.001` maxDD `-1.8971`
- `market_context_high->commodity_4h` score `-0.724` n `153` status `ready` deltaP `3.9245` edge `0.0364` maxDD `-1.165`
- `market_context_high->crypto_major_1h` score `-0.8935` n `153` status `ready` deltaP `4.084` edge `0.0163` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-0.9361` n `153` status `ready` deltaP `7.6648` edge `-0.0001` maxDD `-5.3474`
- `market_context_high->equity_1h` score `-1.784` n `153` status `ready` deltaP `1.7543` edge `-0.0128` maxDD `-12.2088`
- `market_context_high->crypto_alt_1h` score `-2.003` n `153` status `ready` deltaP `-0.725` edge `-0.0035` maxDD `-13.2099`
- `market_context_high->index_4h` score `-3.3521` n `153` status `ready` deltaP `-5.7747` edge `-0.0232` maxDD `-6.7447`
- `market_context_high->crypto_major_24h` score `-4.4133` n `112` status `ready` deltaP `-2.4449` edge `-0.0638` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-4.5716` n `153` status `ready` deltaP `-0.1535` edge `-0.0811` maxDD `-32.9851`
- `market_context_high->commodity_24h` score `-6.2274` n `112` status `ready` deltaP `-15.864` edge `-0.1337` maxDD `-24.0477`
- `market_context_high->equity_24h` score `-6.2649` n `112` status `ready` deltaP `-4.6036` edge `-0.2292` maxDD `-35.4638`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
