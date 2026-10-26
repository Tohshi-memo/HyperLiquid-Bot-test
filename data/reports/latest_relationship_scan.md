# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T23:52:31.801932+00:00`
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

- `market_context_high->unknown_4h` score `90.2763` n `153` status `ready` deltaP `1.0172` edge `7.5498` maxDD `-1.0178`
- `market_context_high->unknown_1h` score `20.8932` n `153` status `ready` deltaP `1.6242` edge `1.7792` maxDD `-1.5807`
- `market_context_high->fx_1h` score `0.2782` n `153` status `ready` deltaP `8.4145` edge `0.0029` maxDD `-0.1986`
- `market_context_high->metal_24h` score `0.2279` n `112` status `ready` deltaP `23.5887` edge `0.1346` maxDD `-7.0108`
- `market_context_high->fx_4h` score `0.1932` n `153` status `ready` deltaP `10.0869` edge `0.0087` maxDD `-0.4545`
- `market_context_high->index_24h` score `-0.0476` n `112` status `ready` deltaP `16.1318` edge `0.0102` maxDD `-4.5747`
- `market_context_high->metal_1h` score `-0.1338` n `153` status `ready` deltaP `8.3304` edge `0.0065` maxDD `-1.6682`
- `market_context_high->fx_24h` score `-0.1379` n `112` status `ready` deltaP `16.972` edge `0.0264` maxDD `-1.2451`
- `market_context_high->commodity_1h` score `-0.2354` n `153` status `ready` deltaP `2.452` edge `0.0141` maxDD `-1.0053`
- `market_context_high->commodity_4h` score `-0.3899` n `153` status `ready` deltaP `6.2111` edge `0.049` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.6078` n `153` status `ready` deltaP `-0.4364` edge `-0.0013` maxDD `-1.8971`
- `market_context_high->crypto_major_1h` score `-0.8389` n `153` status `ready` deltaP `4.8325` edge `0.0183` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-0.9131` n `153` status `ready` deltaP `8.1221` edge `-0.0002` maxDD `-5.3474`
- `market_context_high->equity_1h` score `-1.833` n `153` status `ready` deltaP `0.8561` edge `-0.0131` maxDD `-12.2088`
- `market_context_high->crypto_alt_1h` score `-1.9562` n `153` status `ready` deltaP `-0.1262` edge `-0.0015` maxDD `-13.2099`
- `market_context_high->index_4h` score `-3.3813` n `153` status `ready` deltaP `-6.0796` edge `-0.0236` maxDD `-6.7447`
- `market_context_high->crypto_major_4h` score `-4.5197` n `153` status `ready` deltaP `0.3039` edge `-0.0775` maxDD `-32.9851`
- `market_context_high->crypto_major_24h` score `-4.5605` n `112` status `ready` deltaP `-2.9648` edge `-0.0792` maxDD `-29.1905`
- `market_context_high->commodity_24h` score `-5.9631` n `112` status `ready` deltaP `-13.0911` edge `-0.1183` maxDD `-24.0477`
- `market_context_high->equity_24h` score `-6.8669` n `112` status `ready` deltaP `-7.3765` edge `-0.2879` maxDD `-35.4638`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
