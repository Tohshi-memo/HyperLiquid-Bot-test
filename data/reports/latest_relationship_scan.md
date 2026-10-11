# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T03:37:32.060589+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `5751`

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

- `market_context_high->unknown_4h` score `42.3355` n `87` status `ready` deltaP `-6.4428` edge `3.6248` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.983` n `87` status `ready` deltaP `38.2663` edge `0.6197` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `9.1824` n `87` status `ready` deltaP `19.2528` edge `1.3637` maxDD `-17.8526`
- `market_context_high->crypto_major_4h` score `1.5786` n `87` status `ready` deltaP `18.2734` edge `0.2136` maxDD `-6.9761`
- `market_context_high->crypto_alt_24h` score `0.4754` n `87` status `ready` deltaP `8.0819` edge `0.6183` maxDD `-35.5652`
- `market_context_high->fx_1h` score `0.3845` n `97` status `ready` deltaP `8.2289` edge `0.0014` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.2391` n `97` status `ready` deltaP `10.192` edge `0.0516` maxDD `-3.7778`
- `market_context_high->fx_4h` score `0.0246` n `87` status `ready` deltaP `10.2519` edge `0.0083` maxDD `-0.3008`
- `market_context_high->commodity_1h` score `-0.2248` n `97` status `ready` deltaP `0.747` edge `0.0038` maxDD `-0.3417`
- `market_context_high->index_24h` score `-0.3401` n `87` status `ready` deltaP `8.3633` edge `0.0916` maxDD `-1.9432`
- `market_context_high->metal_24h` score `-0.3953` n `87` status `ready` deltaP `6.5134` edge `0.0544` maxDD `-3.5466`
- `market_context_high->metal_1h` score `-0.4181` n `97` status `ready` deltaP `2.244` edge `0.0014` maxDD `-0.7626`
- `market_context_high->commodity_4h` score `-0.5247` n `87` status `ready` deltaP `-0.9953` edge `-0.0073` maxDD `-1.6002`
- `market_context_high->crypto_alt_1h` score `-0.5954` n `97` status `ready` deltaP `0.0154` edge `0.0374` maxDD `-4.7735`
- `market_context_high->equity_1h` score `-0.7738` n `97` status `ready` deltaP `-1.8149` edge `-0.0031` maxDD `-2.0542`
- `market_context_high->crypto_alt_4h` score `-1.0933` n `87` status `ready` deltaP `-7.4468` edge `0.1028` maxDD `-8.7986`
- `market_context_high->metal_4h` score `-1.1142` n `87` status `ready` deltaP `-8.3981` edge `0.0139` maxDD `-1.0609`
- `market_context_high->equity_4h` score `-1.2628` n `87` status `ready` deltaP `-3.2941` edge `0.007` maxDD `-5.4217`
- `market_context_high->index_1h` score `-1.6376` n `97` status `ready` deltaP `-7.1501` edge `-0.0026` maxDD `-0.5627`
- `market_context_high->index_4h` score `-1.7617` n `87` status `ready` deltaP `-8.2335` edge `0.0013` maxDD `-1.1242`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
