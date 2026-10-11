# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T02:37:28.699953+00:00`
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

- `market_context_high->unknown_4h` score `39.186` n `91` status `ready` deltaP `-8.627` edge `3.3769` maxDD `-2.3109`
- `market_context_high->equity_24h` score `10.1171` n `91` status `ready` deltaP `38.5474` edge `0.629` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `9.572` n `91` status `ready` deltaP `20.9707` edge `1.4022` maxDD `-17.8526`
- `market_context_high->crypto_major_4h` score `1.6096` n `91` status `ready` deltaP `19.0784` edge `0.2122` maxDD `-6.9761`
- `market_context_high->crypto_alt_24h` score `0.9435` n `91` status `ready` deltaP `10.1534` edge `0.6645` maxDD `-35.5652`
- `market_context_high->crypto_major_1h` score `0.5665` n `97` status `ready` deltaP `11.9545` edge `0.0564` maxDD `-3.7778`
- `market_context_high->fx_1h` score `0.1718` n `97` status `ready` deltaP `5.5852` edge `0.0013` maxDD `-0.271`
- `market_context_high->fx_4h` score `-0.094` n `91` status `ready` deltaP `8.8264` edge `0.008` maxDD `-0.3077`
- `market_context_high->metal_1h` score `-0.2759` n `97` status `ready` deltaP `4.0064` edge `0.0015` maxDD `-0.7626`
- `market_context_high->index_24h` score `-0.2805` n `91` status `ready` deltaP `9.6898` edge `0.0904` maxDD `-1.9432`
- `market_context_high->metal_24h` score `-0.3068` n `91` status `ready` deltaP `7.6599` edge `0.0581` maxDD `-3.5466`
- `market_context_high->commodity_1h` score `-0.4368` n `97` status `ready` deltaP `-0.1343` edge `0.0021` maxDD `-0.3417`
- `market_context_high->crypto_alt_1h` score `-0.7408` n `97` status `ready` deltaP `0.0154` edge `0.052` maxDD `-4.7735`
- `market_context_high->commodity_4h` score `-0.7603` n `91` status `ready` deltaP `-2.8611` edge `-0.0084` maxDD `-1.6002`
- `market_context_high->equity_1h` score `-0.8142` n `97` status `ready` deltaP `-2.6961` edge `-0.0024` maxDD `-2.0542`
- `market_context_high->crypto_alt_4h` score `-0.9221` n `91` status `ready` deltaP `-5.58` edge `0.1123` maxDD `-8.7986`
- `market_context_high->metal_4h` score `-0.9807` n `91` status `ready` deltaP `-5.7709` edge `0.0135` maxDD `-1.0609`
- `market_context_high->equity_4h` score `-1.2152` n `91` status `ready` deltaP `-2.8293` edge `0.01` maxDD `-5.4217`
- `market_context_high->index_4h` score `-1.2336` n `91` status `ready` deltaP `-9.9505` edge `0.0014` maxDD `-1.1242`
- `market_context_high->index_1h` score `-1.7081` n `97` status `ready` deltaP `-8.0314` edge `-0.0026` maxDD `-0.5627`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
