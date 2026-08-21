# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T06:52:28.920153+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13758`

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

- `market_context_high->equity_1h` score `0.3089` n `105` status `ready` deltaP `8.4203` edge `0.0511` maxDD `-3.1861`
- `market_context_high->index_1h` score `0.2963` n `105` status `ready` deltaP `10.1084` edge `0.006` maxDD `-0.5622`
- `market_context_high->equity_4h` score `0.1015` n `105` status `ready` deltaP `4.7402` edge `0.1398` maxDD `-8.3685`
- `market_context_high->fx_4h` score `0.0652` n `105` status `ready` deltaP `7.6379` edge `0.0077` maxDD `-0.3539`
- `market_context_high->fx_1h` score `-0.2146` n `105` status `ready` deltaP `0.6259` edge `0.0042` maxDD `-0.2043`
- `market_context_high->commodity_24h` score `-0.2223` n `98` status `ready` deltaP `5.3253` edge `0.1293` maxDD `-4.666`
- `market_context_high->metal_4h` score `-0.2437` n `105` status `ready` deltaP `6.5302` edge `-0.0172` maxDD `-1.273`
- `market_context_high->index_4h` score `-0.3027` n `105` status `ready` deltaP `5.4283` edge `0.0174` maxDD `-1.7252`
- `market_context_high->metal_1h` score `-0.3156` n `105` status `ready` deltaP `2.1899` edge `-0.0022` maxDD `-0.4291`
- `market_context_high->unknown_1h` score `-0.411` n `105` status `ready` deltaP `7.6305` edge `-0.0624` maxDD `-0.4843`
- `market_context_high->commodity_4h` score `-0.6401` n `105` status `ready` deltaP `-1.2805` edge `0.0115` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.7455` n `105` status `ready` deltaP `-5.7285` edge `-0.0008` maxDD `-1.1941`
- `market_context_high->crypto_alt_1h` score `-0.8127` n `105` status `ready` deltaP `-1.7436` edge `-0.0124` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.9563` n `105` status `ready` deltaP `-1.008` edge `-0.0314` maxDD `-2.7581`
- `market_context_high->crypto_alt_4h` score `-2.6287` n `105` status `ready` deltaP `0.4704` edge `-0.0952` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-2.9924` n `105` status `ready` deltaP `2.7192` edge `-0.1654` maxDD `-3.1677`
- `market_context_high->fx_24h` score `-3.3868` n `98` status `ready` deltaP `-16.3088` edge `-0.0152` maxDD `-1.9981`
- `market_context_high->index_24h` score `-3.7134` n `98` status `ready` deltaP `-0.0213` edge `-0.0486` maxDD `-18.5202`
- `market_context_high->metal_24h` score `-4.8129` n `98` status `ready` deltaP `-19.9865` edge `-0.153` maxDD `-11.4635`
- `market_context_high->unknown_24h` score `-5.1656` n `98` status `ready` deltaP `11.515` edge `-0.4566` maxDD `-1.0505`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
