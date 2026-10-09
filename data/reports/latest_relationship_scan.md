# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-09T08:52:36.995014+00:00`
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

- `market_context_high->unknown_4h` score `40.4671` n `91` status `ready` deltaP `-4.3587` edge `3.4552` maxDD `-2.3109`
- `market_context_high->crypto_major_24h` score `10.0128` n `90` status `ready` deltaP `22.3611` edge `1.432` maxDD `-16.7906`
- `market_context_high->equity_24h` score `9.9635` n `90` status `ready` deltaP `32.9514` edge `0.6535` maxDD `-1.0977`
- `market_context_high->crypto_alt_24h` score `3.5727` n `90` status `ready` deltaP `14.0625` edge `0.9581` maxDD `-34.5048`
- `market_context_high->crypto_major_4h` score `1.8597` n `91` status `ready` deltaP `17.8588` edge `0.2524` maxDD `-6.9761`
- `market_context_high->metal_24h` score `0.7743` n `90` status `ready` deltaP `16.2847` edge `0.1392` maxDD `-3.5466`
- `market_context_high->fx_1h` score `0.2835` n `91` status `ready` deltaP `6.9965` edge `0.0012` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.2718` n `91` status `ready` deltaP `9.6944` edge `0.0591` maxDD `-3.7778`
- `market_context_high->fx_4h` score `0.1135` n `91` status `ready` deltaP `11.5703` edge `0.007` maxDD `-0.3077`
- `market_context_high->metal_1h` score `-0.2522` n `91` status `ready` deltaP `4.0469` edge `0.0032` maxDD `-0.7626`
- `market_context_high->commodity_1h` score `-0.3327` n `91` status `ready` deltaP `1.1516` edge `0.0022` maxDD `-0.3417`
- `market_context_high->index_24h` score `-0.3407` n `90` status `ready` deltaP `7.8125` edge `0.0952` maxDD `-1.9432`
- `market_context_high->crypto_alt_4h` score `-0.4421` n `91` status `ready` deltaP `-7.1044` edge `0.184` maxDD `-8.7986`
- `market_context_high->metal_4h` score `-0.8296` n `91` status `ready` deltaP `-4.0941` edge `0.0217` maxDD `-1.0609`
- `market_context_high->equity_1h` score `-0.9096` n `91` status `ready` deltaP `-3.5401` edge `-0.009` maxDD `-2.0542`
- `market_context_high->commodity_4h` score `-0.9123` n `91` status `ready` deltaP `-3.6233` edge `-0.0228` maxDD `-1.6002`
- `market_context_high->crypto_alt_1h` score `-0.9599` n `91` status `ready` deltaP `-2.2438` edge `0.0488` maxDD `-4.7735`
- `market_context_high->index_1h` score `-1.2769` n `91` status `ready` deltaP `-10.9364` edge `-0.0046` maxDD `-0.5627`
- `market_context_high->index_4h` score `-1.3741` n `91` status `ready` deltaP `-11.9322` edge `-0.0034` maxDD `-1.1242`
- `market_context_high->equity_4h` score `-1.3924` n `91` status `ready` deltaP `-4.811` edge `0.0005` maxDD `-5.4217`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
