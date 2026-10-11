# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T02:07:21.527823+00:00`
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

- `market_context_high->unknown_4h` score `39.322` n `91` status `ready` deltaP `-8.3221` edge `3.3862` maxDD `-2.3109`
- `market_context_high->equity_24h` score `10.1051` n `91` status `ready` deltaP `38.5474` edge `0.628` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `9.5392` n `91` status `ready` deltaP `20.9707` edge `1.398` maxDD `-17.8526`
- `market_context_high->crypto_major_4h` score `1.5883` n `91` status `ready` deltaP `18.7735` edge `0.2115` maxDD `-6.9761`
- `market_context_high->crypto_alt_24h` score `0.9552` n `91` status `ready` deltaP `10.1534` edge `0.666` maxDD `-35.5652`
- `market_context_high->crypto_major_1h` score `0.3213` n `95` status `ready` deltaP `11.2165` edge `0.0553` maxDD `-3.7778`
- `market_context_high->fx_1h` score `0.1297` n `95` status `ready` deltaP `5.0599` edge `0.0013` maxDD `-0.271`
- `market_context_high->fx_4h` score `-0.094` n `91` status `ready` deltaP `8.8264` edge `0.008` maxDD `-0.3077`
- `market_context_high->index_24h` score `-0.2895` n `91` status `ready` deltaP `9.5162` edge `0.0904` maxDD `-1.9432`
- `market_context_high->metal_24h` score `-0.3091` n `91` status `ready` deltaP `7.6599` edge `0.0578` maxDD `-3.5466`
- `market_context_high->metal_1h` score `-0.338` n `95` status `ready` deltaP `3.2446` edge `0.0014` maxDD `-0.7626`
- `market_context_high->commodity_1h` score `-0.5042` n `95` status `ready` deltaP `-0.9612` edge `0.002` maxDD `-0.3417`
- `market_context_high->commodity_4h` score `-0.7429` n `91` status `ready` deltaP `-2.5562` edge `-0.0082` maxDD `-1.6002`
- `market_context_high->crypto_alt_1h` score `-0.8358` n `95` status `ready` deltaP `-0.6618` edge `0.0486` maxDD `-4.7735`
- `market_context_high->equity_1h` score `-0.8538` n `95` status `ready` deltaP `-3.3517` edge `-0.0031` maxDD `-2.0542`
- `market_context_high->crypto_alt_4h` score `-0.9103` n `91` status `ready` deltaP `-5.4275` edge `0.1128` maxDD `-8.7986`
- `market_context_high->metal_4h` score `-0.9807` n `91` status `ready` deltaP `-5.7709` edge `0.0135` maxDD `-1.0609`
- `market_context_high->index_1h` score `-1.1595` n `95` status `ready` deltaP `-8.9474` edge `-0.0028` maxDD `-0.5627`
- `market_context_high->index_4h` score `-1.2257` n `91` status `ready` deltaP `-9.798` edge `0.0014` maxDD `-1.1242`
- `market_context_high->equity_4h` score `-1.2327` n `91` status `ready` deltaP `-3.1342` edge `0.0098` maxDD `-5.4217`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
