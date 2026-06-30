# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T23:22:26.837035+00:00`
- Price records: `672`
- Market context records: `5296`
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

- `market_context_high->unknown_24h` score `22.2181` n `153` status `ready` deltaP `25.9497` edge `1.6875` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `7.604` n `153` status `ready` deltaP `25.7353` edge `0.8771` maxDD `-26.5332`
- `market_context_high->equity_24h` score `4.6526` n `153` status `ready` deltaP `19.9653` edge `0.8175` maxDD `-40.0306`
- `market_context_high->crypto_alt_4h` score `3.9453` n `183` status `ready` deltaP `15.114` edge `0.3921` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.85` n `183` status `ready` deltaP `15.9278` edge `0.4439` maxDD `-14.0065`
- `market_context_high->equity_4h` score `1.5783` n `183` status `ready` deltaP `11.383` edge `0.2195` maxDD `-7.4425`
- `market_context_high->unknown_4h` score `0.9635` n `183` status `ready` deltaP `14.7766` edge `0.084` maxDD `-5.5109`
- `market_context_high->fx_24h` score `0.5481` n `153` status `ready` deltaP `13.3068` edge `0.0465` maxDD `-0.8294`
- `market_context_high->index_24h` score `0.2966` n `153` status `ready` deltaP `20.8231` edge `0.0627` maxDD `-7.413`
- `market_context_high->crypto_alt_1h` score `0.2903` n `194` status `ready` deltaP `3.7425` edge `0.0954` maxDD `-5.0257`
- `market_context_high->equity_1h` score `0.1703` n `194` status `ready` deltaP `8.3123` edge `0.0553` maxDD `-5.0555`
- `market_context_high->crypto_major_1h` score `0.1366` n `194` status `ready` deltaP `5.2395` edge `0.101` maxDD `-6.9639`
- `market_context_high->index_1h` score `-0.0289` n `194` status `ready` deltaP `5.6192` edge `0.0105` maxDD `-1.0296`
- `market_context_high->index_4h` score `-0.3314` n `183` status `ready` deltaP `6.4882` edge `0.026` maxDD `-2.9391`
- `market_context_high->metal_1h` score `-0.3592` n `194` status `ready` deltaP `2.0958` edge `0.0075` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.3929` n `194` status `ready` deltaP `-0.1836` edge `-0.0002` maxDD `-0.5823`
- `market_context_high->fx_4h` score `-0.7479` n `183` status `ready` deltaP `0.7847` edge `0.0018` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.4575` n `194` status `ready` deltaP `-3.4755` edge `-0.0065` maxDD `-3.3428`
- `market_context_high->metal_4h` score `-1.8861` n `183` status `ready` deltaP `-5.053` edge `-0.0014` maxDD `-9.8709`
- `market_context_high->crypto_alt_24h` score `-2.9078` n `153` status `ready` deltaP `13.3476` edge `0.3792` maxDD `-53.6115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
