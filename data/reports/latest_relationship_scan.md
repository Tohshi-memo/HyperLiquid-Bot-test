# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T02:52:25.216296+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `5679`

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

- `market_context_high->unknown_4h` score `39.9914` n `90` status `ready` deltaP `-7.7845` edge `3.4384` maxDD `-2.3109`
- `market_context_high->equity_24h` score `10.0855` n `90` status `ready` deltaP `38.4375` edge `0.6271` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `9.4818` n `90` status `ready` deltaP `20.5555` edge `1.3934` maxDD `-17.8526`
- `market_context_high->crypto_major_4h` score `1.606` n `90` status `ready` deltaP `18.8889` edge `0.213` maxDD `-6.9761`
- `market_context_high->crypto_alt_24h` score `0.8418` n `90` status `ready` deltaP `9.6527` edge `0.6548` maxDD `-35.5652`
- `market_context_high->crypto_major_1h` score `0.5809` n `97` status `ready` deltaP `11.9545` edge `0.0576` maxDD `-3.7778`
- `market_context_high->fx_1h` score `0.2423` n `97` status `ready` deltaP `6.4665` edge `0.0013` maxDD `-0.271`
- `market_context_high->fx_4h` score `-0.0487` n `90` status `ready` deltaP `9.3699` edge `0.0081` maxDD `-0.3034`
- `market_context_high->metal_1h` score `-0.2759` n `97` status `ready` deltaP `4.0064` edge `0.0015` maxDD `-0.7626`
- `market_context_high->index_24h` score `-0.2945` n `90` status `ready` deltaP `9.375` edge `0.0907` maxDD `-1.9432`
- `market_context_high->metal_24h` score `-0.3324` n `90` status `ready` deltaP `7.2569` edge `0.0575` maxDD `-3.5466`
- `market_context_high->commodity_1h` score `-0.4368` n `97` status `ready` deltaP `-0.1343` edge `0.0021` maxDD `-0.3417`
- `market_context_high->commodity_4h` score `-0.7023` n `90` status `ready` deltaP `-2.4154` edge `-0.0081` maxDD `-1.6002`
- `market_context_high->crypto_alt_1h` score `-0.73` n `97` status `ready` deltaP `0.0154` edge `0.0529` maxDD `-4.7735`
- `market_context_high->equity_1h` score `-0.7645` n `97` status `ready` deltaP `-1.8149` edge `-0.0019` maxDD `-2.0542`
- `market_context_high->crypto_alt_4h` score `-0.9591` n `90` status `ready` deltaP `-6.1416` edge `0.1113` maxDD `-8.7986`
- `market_context_high->metal_4h` score `-1.013` n `90` status `ready` deltaP `-6.4058` edge `0.0136` maxDD `-1.0609`
- `market_context_high->equity_4h` score `-1.1866` n `90` status `ready` deltaP `-2.2188` edge `0.0096` maxDD `-5.4217`
- `market_context_high->index_1h` score `-1.6364` n `97` status `ready` deltaP `-7.1501` edge `-0.0025` maxDD `-0.5627`
- `market_context_high->index_4h` score `-1.8629` n `90` status `ready` deltaP `-9.4987` edge `0.0013` maxDD `-1.1242`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
