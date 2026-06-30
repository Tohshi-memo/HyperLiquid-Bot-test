# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T14:07:30.950912+00:00`
- Price records: `672`
- Market context records: `5254`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9544`

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

- `market_context_high->unknown_24h` score `25.376` n `143` status `ready` deltaP `29.8417` edge `1.9347` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `10.9401` n `143` status `ready` deltaP `29.8259` edge `1.079` maxDD `-22.6266`
- `market_context_high->crypto_alt_4h` score `4.1432` n `158` status `ready` deltaP `14.0669` edge `0.4114` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.8359` n `158` status `ready` deltaP `14.2656` edge `0.4538` maxDD `-14.0065`
- `market_context_high->equity_24h` score `2.9237` n `143` status `ready` deltaP `19.1883` edge `0.6786` maxDD `-40.0306`
- `market_context_high->crypto_alt_24h` score `1.9486` n `143` status `ready` deltaP `16.867` edge `0.5753` maxDD `-32.3622`
- `market_context_high->unknown_4h` score `1.8862` n `158` status `ready` deltaP `16.6506` edge `0.1484` maxDD `-5.5109`
- `market_context_high->crypto_alt_1h` score `0.5562` n `165` status `ready` deltaP `4.9655` edge `0.1094` maxDD `-5.0257`
- `market_context_high->fx_24h` score `0.514` n `143` status `ready` deltaP `12.7307` edge `0.0475` maxDD `-0.8294`
- `market_context_high->equity_4h` score `0.5056` n `158` status `ready` deltaP `8.085` edge `0.1521` maxDD `-7.4425`
- `market_context_high->crypto_major_1h` score `0.4241` n `165` status `ready` deltaP `6.2983` edge `0.1179` maxDD `-6.9639`
- `market_context_high->index_24h` score `0.117` n `143` status `ready` deltaP `20.4752` edge `0.042` maxDD `-7.413`
- `market_context_high->unknown_1h` score `0.0976` n `165` status `ready` deltaP `8.0829` edge `0.0184` maxDD `-2.7986`
- `market_context_high->equity_1h` score `0.0532` n `165` status `ready` deltaP `6.5496` edge `0.0573` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.1005` n `165` status `ready` deltaP `4.7242` edge `0.0105` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.1184` n `165` status `ready` deltaP `4.5164` edge `0.0139` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.3263` n `165` status `ready` deltaP `0.6315` edge `-0.0008` maxDD `-0.6194`
- `market_context_high->index_4h` score `-0.7571` n `158` status `ready` deltaP `4.4767` edge `0.0188` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.8171` n `158` status `ready` deltaP `-0.3088` edge `0.0007` maxDD `-1.6047`
- `market_context_high->commodity_1h` score `-1.291` n `165` status `ready` deltaP `-2.5631` edge `-0.0065` maxDD `-2.7194`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
