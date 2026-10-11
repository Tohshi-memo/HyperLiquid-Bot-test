# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T03:07:24.826091+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `5719`

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

- `market_context_high->unknown_4h` score `40.7993` n `89` status `ready` deltaP `-7.0756` edge `3.501` maxDD `-2.3109`
- `market_context_high->equity_24h` score `10.055` n `89` status `ready` deltaP `38.3251` edge `0.6253` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `9.4059` n `89` status `ready` deltaP `20.1311` edge `1.3865` maxDD `-17.8526`
- `market_context_high->crypto_major_4h` score `1.6012` n `89` status `ready` deltaP `18.6917` edge `0.2137` maxDD `-6.9761`
- `market_context_high->crypto_alt_24h` score `0.7395` n `89` status `ready` deltaP `9.1409` edge `0.6451` maxDD `-35.5652`
- `market_context_high->crypto_major_1h` score `0.5869` n `97` status `ready` deltaP `11.9545` edge `0.0581` maxDD `-3.7778`
- `market_context_high->fx_1h` score `0.2423` n `97` status `ready` deltaP `6.4665` edge `0.0013` maxDD `-0.271`
- `market_context_high->fx_4h` score `-0.0037` n `89` status `ready` deltaP `9.929` edge `0.0081` maxDD `-0.3013`
- `market_context_high->metal_1h` score `-0.1793` n `97` status `ready` deltaP `4.0064` edge `0.0015` maxDD `-0.7626`
- `market_context_high->index_24h` score `-0.3083` n `89` status `ready` deltaP `9.0493` edge `0.0911` maxDD `-1.9432`
- `market_context_high->metal_24h` score `-0.3503` n `89` status `ready` deltaP `7.0185` edge `0.0568` maxDD `-3.5466`
- `market_context_high->commodity_1h` score `-0.3615` n `97` status `ready` deltaP `0.747` edge `0.0025` maxDD `-0.3417`
- `market_context_high->commodity_4h` score `-0.6405` n `89` status `ready` deltaP `-1.956` edge `-0.0074` maxDD `-1.6002`
- `market_context_high->crypto_alt_1h` score `-0.7312` n `97` status `ready` deltaP `0.0154` edge `0.0528` maxDD `-4.7735`
- `market_context_high->equity_1h` score `-0.7645` n `97` status `ready` deltaP `-1.8149` edge `-0.0019` maxDD `-2.0542`
- `market_context_high->crypto_alt_4h` score `-0.9958` n `89` status `ready` deltaP `-6.5634` edge `0.1094` maxDD `-8.7986`
- `market_context_high->metal_4h` score `-1.0459` n `89` status `ready` deltaP `-7.055` edge `0.0137` maxDD `-1.0609`
- `market_context_high->index_4h` score `-1.1948` n `89` status `ready` deltaP `-9.1892` edge `0.0013` maxDD `-1.1242`
- `market_context_high->equity_4h` score `-1.2101` n `89` status `ready` deltaP `-2.5658` edge `0.0089` maxDD `-5.4217`
- `market_context_high->index_1h` score `-1.6364` n `97` status `ready` deltaP `-7.1501` edge `-0.0025` maxDD `-0.5627`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
