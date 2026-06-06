# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T16:52:24.747172+00:00`
- Price records: `672`
- Market context records: `3092`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6911`

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

- `market_context_high->crypto_alt_24h` score `16.9844` n `84` status `ready` deltaP `13.5416` edge `2.5538` maxDD `-28.6603`
- `market_context_high->commodity_24h` score `15.1403` n `84` status `ready` deltaP `45.3621` edge `1.0021` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `14.6799` n `84` status `ready` deltaP `22.9911` edge `1.1176` maxDD `-1.8041`
- `market_context_high->index_24h` score `11.6435` n `84` status `ready` deltaP `34.5982` edge `0.9406` maxDD `-12.7439`
- `market_context_high->equity_24h` score `8.6702` n `84` status `ready` deltaP `21.0069` edge `1.4351` maxDD `-32.0862`
- `market_context_high->commodity_4h` score `3.0293` n `118` status `ready` deltaP `18.4115` edge `0.1755` maxDD `-1.9973`
- `market_context_high->unknown_4h` score `0.5686` n `118` status `ready` deltaP `4.5964` edge `0.099` maxDD `-2.914`
- `market_context_high->commodity_1h` score `-0.0712` n `124` status `ready` deltaP `1.5791` edge `0.0258` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.5052` n `124` status `ready` deltaP `3.7667` edge `0.0164` maxDD `-4.5023`
- `market_context_high->fx_1h` score `-0.6828` n `124` status `ready` deltaP `-7.316` edge `-0.0015` maxDD `-0.3147`
- `market_context_high->crypto_alt_1h` score `-0.7546` n `124` status `ready` deltaP `3.9164` edge `0.0901` maxDD `-14.7034`
- `market_context_high->fx_24h` score `-0.7965` n `84` status `ready` deltaP `3.4226` edge `-0.004` maxDD `-0.4822`
- `market_context_high->equity_1h` score `-1.263` n `124` status `ready` deltaP `-1.9123` edge `-0.0006` maxDD `-8.8863`
- `market_context_high->fx_4h` score `-1.3399` n `118` status `ready` deltaP `-12.2727` edge `-0.0056` maxDD `-1.0829`
- `market_context_high->index_4h` score `-1.4421` n `118` status `ready` deltaP `9.3039` edge `0.044` maxDD `-17.6057`
- `market_context_high->crypto_major_1h` score `-2.1094` n `124` status `ready` deltaP `-0.3139` edge `0.0526` maxDD `-15.1032`
- `market_context_high->metal_1h` score `-2.322` n `124` status `ready` deltaP `-6.4999` edge `-0.0108` maxDD `-7.4828`
- `market_context_high->unknown_1h` score `-2.9275` n `124` status `ready` deltaP `1.753` edge `-0.0712` maxDD `-12.7554`
- `market_context_high->crypto_alt_4h` score `-3.4377` n `118` status `ready` deltaP `15.262` edge `0.262` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-3.9191` n `118` status `ready` deltaP `7.3222` edge `-0.0274` maxDD `-36.242`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
