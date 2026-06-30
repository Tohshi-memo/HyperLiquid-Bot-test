# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T20:37:27.604855+00:00`
- Price records: `672`
- Market context records: `5283`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9650`

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

- `market_context_high->unknown_24h` score `24.6334` n `153` status `ready` deltaP `27.6859` edge `1.8772` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `7.4996` n `153` status `ready` deltaP `25.7353` edge `0.8684` maxDD `-26.5332`
- `market_context_high->crypto_alt_4h` score `4.2656` n `177` status `ready` deltaP `16.6571` edge `0.4085` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.0004` n `177` status `ready` deltaP `16.2628` edge `0.4542` maxDD `-14.0065`
- `market_context_high->equity_24h` score `3.9038` n `153` status `ready` deltaP `19.9653` edge `0.7551` maxDD `-40.0306`
- `market_context_high->equity_4h` score `1.0342` n `177` status `ready` deltaP `10.3271` edge `0.1812` maxDD `-7.4425`
- `market_context_high->unknown_4h` score `0.7735` n `177` status `ready` deltaP `14.8021` edge `0.068` maxDD `-5.5109`
- `market_context_high->fx_24h` score `0.5649` n `153` status `ready` deltaP `13.3068` edge `0.0479` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.4772` n `184` status `ready` deltaP `4.9238` edge `0.1031` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.2971` n `184` status `ready` deltaP `6.1214` edge `0.1085` maxDD `-6.9639`
- `market_context_high->index_24h` score `0.2389` n `153` status `ready` deltaP `20.8231` edge `0.0553` maxDD `-7.413`
- `market_context_high->equity_1h` score `0.1313` n `184` status `ready` deltaP `7.4655` edge `0.0577` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.0187` n `184` status `ready` deltaP `5.7017` edge `0.0108` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.2402` n `184` status `ready` deltaP `2.789` edge `0.0098` maxDD `-2.0682`
- `market_context_high->index_4h` score `-0.2863` n `177` status `ready` deltaP `7.2508` edge `0.0267` maxDD `-2.9391`
- `market_context_high->fx_1h` score `-0.3352` n `184` status `ready` deltaP `0.8657` edge `0.0002` maxDD `-0.5823`
- `market_context_high->fx_4h` score `-0.7327` n `177` status `ready` deltaP `1.1084` edge `0.0016` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.3737` n `184` status `ready` deltaP `-2.4733` edge `-0.0062` maxDD `-3.3428`
- `market_context_high->metal_4h` score `-1.7142` n `177` status `ready` deltaP `-3.6637` edge `0.005` maxDD `-9.3609`
- `market_context_high->unknown_1h` score `-2.6301` n `184` status `ready` deltaP `7.0164` edge `-0.2018` maxDD `-2.7986`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
