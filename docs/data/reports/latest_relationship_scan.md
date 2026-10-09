# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-09T09:37:40.106446+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8370`

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

- `market_context_high->unknown_4h` score `40.3033` n `91` status `ready` deltaP `-4.816` edge `3.4446` maxDD `-2.3109`
- `market_context_high->equity_24h` score `10.0663` n `90` status `ready` deltaP `33.4722` edge `0.6586` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `10.0198` n `90` status `ready` deltaP `22.3611` edge `1.4329` maxDD `-16.7906`
- `market_context_high->crypto_alt_24h` score `3.5735` n `90` status `ready` deltaP `14.0625` edge `0.9582` maxDD `-34.5048`
- `market_context_high->crypto_major_4h` score `1.8817` n `91` status `ready` deltaP `18.0113` edge `0.2542` maxDD `-6.9761`
- `market_context_high->metal_24h` score `0.7183` n `90` status `ready` deltaP `15.7639` edge `0.1355` maxDD `-3.5466`
- `market_context_high->fx_1h` score `0.2835` n `91` status `ready` deltaP `6.9965` edge `0.0012` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.2718` n `91` status `ready` deltaP `9.6944` edge `0.0591` maxDD `-3.7778`
- `market_context_high->fx_4h` score `0.0977` n `91` status `ready` deltaP `11.4179` edge `0.0067` maxDD `-0.3077`
- `market_context_high->metal_1h` score `-0.2199` n `91` status `ready` deltaP `4.3463` edge `0.0039` maxDD `-0.7626`
- `market_context_high->index_24h` score `-0.3336` n `90` status `ready` deltaP `7.8125` edge `0.0961` maxDD `-1.9432`
- `market_context_high->commodity_1h` score `-0.3699` n `91` status `ready` deltaP `0.8522` edge `0.0011` maxDD `-0.3417`
- `market_context_high->crypto_alt_4h` score `-0.4256` n `91` status `ready` deltaP `-6.9519` edge `0.1851` maxDD `-8.7986`
- `market_context_high->metal_4h` score `-0.8296` n `91` status `ready` deltaP `-4.0941` edge `0.0217` maxDD `-1.0609`
- `market_context_high->equity_1h` score `-0.8839` n `91` status `ready` deltaP `-3.2407` edge `-0.0077` maxDD `-2.0542`
- `market_context_high->crypto_alt_1h` score `-0.9264` n `91` status `ready` deltaP `-1.9444` edge `0.0496` maxDD `-4.7735`
- `market_context_high->commodity_4h` score `-0.9287` n `91` status `ready` deltaP `-3.6233` edge `-0.0249` maxDD `-1.6002`
- `market_context_high->index_1h` score `-1.259` n `91` status `ready` deltaP `-10.637` edge `-0.0043` maxDD `-0.5627`
- `market_context_high->index_4h` score `-1.3725` n `91` status `ready` deltaP `-11.9322` edge `-0.0032` maxDD `-1.1242`
- `market_context_high->equity_4h` score `-1.3908` n `91` status `ready` deltaP `-4.811` edge `0.0007` maxDD `-5.4217`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
