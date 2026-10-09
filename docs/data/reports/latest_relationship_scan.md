# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-09T17:37:33.170574+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7791`

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

- `market_context_high->unknown_4h` score `40.6671` n `91` status `ready` deltaP `-4.6636` edge `3.4739` maxDD `-2.3109`
- `market_context_high->equity_24h` score `10.0474` n `91` status `ready` deltaP `33.6863` edge `0.6556` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `8.8127` n `91` status `ready` deltaP `19.9291` edge `1.3118` maxDD `-17.8526`
- `market_context_high->crypto_alt_24h` score `2.2774` n `91` status `ready` deltaP `11.7159` edge `0.8251` maxDD `-35.5652`
- `market_context_high->crypto_major_4h` score `1.6682` n `91` status `ready` deltaP `18.3162` edge `0.2248` maxDD `-6.9761`
- `market_context_high->fx_1h` score `0.311` n `91` status `ready` deltaP `7.2959` edge `0.0015` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.299` n `91` status `ready` deltaP `10.4429` edge `0.0576` maxDD `-3.7778`
- `market_context_high->fx_4h` score `0.2338` n `91` status `ready` deltaP `12.7898` edge `0.0089` maxDD `-0.3077`
- `market_context_high->metal_24h` score `0.1072` n `91` status `ready` deltaP `10.6113` edge `0.0915` maxDD `-3.5466`
- `market_context_high->metal_1h` score `-0.3038` n `91` status `ready` deltaP `3.7475` edge `0.0009` maxDD `-0.7626`
- `market_context_high->index_24h` score `-0.3154` n `91` status `ready` deltaP `7.9537` edge `0.0975` maxDD `-1.9432`
- `market_context_high->commodity_1h` score `-0.4574` n `91` status `ready` deltaP `0.1037` edge `-0.0012` maxDD `-0.3417`
- `market_context_high->crypto_alt_4h` score `-0.5045` n `91` status `ready` deltaP `-6.1897` edge `0.1699` maxDD `-8.7986`
- `market_context_high->crypto_alt_1h` score `-0.8317` n `91` status `ready` deltaP `-1.1959` edge `0.0525` maxDD `-4.7735`
- `market_context_high->equity_1h` score `-0.8418` n `91` status `ready` deltaP `-3.091` edge `-0.0033` maxDD `-2.0542`
- `market_context_high->commodity_4h` score `-0.8899` n `91` status `ready` deltaP `-3.0136` edge `-0.024` maxDD `-1.6002`
- `market_context_high->metal_4h` score `-0.9892` n `91` status `ready` deltaP `-5.6185` edge `0.0114` maxDD `-1.0609`
- `market_context_high->index_1h` score `-1.178` n `91` status `ready` deltaP `-9.2897` edge `-0.0029` maxDD `-0.5627`
- `market_context_high->index_4h` score `-1.2193` n `91` status `ready` deltaP `-9.6456` edge `0.0012` maxDD `-1.1242`
- `market_context_high->equity_4h` score `-1.2212` n `91` status `ready` deltaP `-3.439` edge `0.0133` maxDD `-5.4217`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
