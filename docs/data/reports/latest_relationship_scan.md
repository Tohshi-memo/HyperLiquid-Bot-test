# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T06:13:15.209107+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9632`

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

- `market_context_high->unknown_4h` score `69.7932` n `143` status `ready` deltaP `3.2034` edge `5.8283` maxDD `-1.0178`
- `market_context_high->unknown_1h` score `19.699` n `143` status `ready` deltaP `0.781` edge `1.6853` maxDD `-1.5807`
- `market_context_high->index_24h` score `0.5491` n `120` status `ready` deltaP `21.7938` edge `0.0259` maxDD `-2.7307`
- `market_context_high->fx_4h` score `0.4361` n `143` status `ready` deltaP `12.9733` edge `0.0097` maxDD `-0.4545`
- `market_context_high->fx_1h` score `0.3957` n `143` status `ready` deltaP `9.8384` edge `0.0032` maxDD `-0.1986`
- `market_context_high->metal_24h` score `0.0786` n `120` status `ready` deltaP `20.6442` edge `0.125` maxDD `-6.204`
- `market_context_high->metal_1h` score `0.0586` n `143` status `ready` deltaP `10.7837` edge `0.0103` maxDD `-1.3073`
- `market_context_high->commodity_1h` score `-0.0198` n `143` status `ready` deltaP `4.5476` edge `0.0181` maxDD `-1.0053`
- `market_context_high->fx_24h` score `-0.2674` n `120` status `ready` deltaP `14.8729` edge `0.0238` maxDD `-1.2451`
- `market_context_high->commodity_4h` score `-0.52` n `143` status `ready` deltaP `5.845` edge `0.0406` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.6702` n `143` status `ready` deltaP `-1.3505` edge `-0.0032` maxDD `-1.8971`
- `market_context_high->crypto_major_1h` score `-0.6765` n `143` status `ready` deltaP `4.7423` edge `0.0215` maxDD `-7.8544`
- `market_context_high->metal_4h` score `-0.7791` n `143` status `ready` deltaP `9.5588` edge `0.0006` maxDD `-4.8031`
- `market_context_high->equity_1h` score `-1.75` n `143` status `ready` deltaP `1.6435` edge `-0.0077` maxDD `-12.2088`
- `market_context_high->crypto_alt_1h` score `-2.0213` n `143` status `ready` deltaP `-1.1558` edge `-0.007` maxDD `-12.8878`
- `market_context_high->equity_24h` score `-3.0736` n `120` status `ready` deltaP `-0.286` edge `-0.0507` maxDD `-19.3152`
- `market_context_high->index_4h` score `-3.2219` n `143` status `ready` deltaP `-5.603` edge `-0.0262` maxDD `-6.3949`
- `market_context_high->crypto_major_4h` score `-4.0184` n `143` status `ready` deltaP `1.5692` edge `-0.0703` maxDD `-29.0939`
- `market_context_high->crypto_major_24h` score `-4.1812` n `120` status `ready` deltaP `1.4804` edge `-0.0602` maxDD `-29.1905`
- `market_context_high->equity_4h` score `-5.9706` n `143` status `ready` deltaP `1.1843` edge `-0.1447` maxDD `-40.9588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
