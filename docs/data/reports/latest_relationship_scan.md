# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-10T04:37:30.856392+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7647`

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

- `market_context_high->unknown_4h` score `40.8533` n `91` status `ready` deltaP `-6.3404` edge `3.5006` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.3849` n `91` status `ready` deltaP `33.2641` edge `0.6032` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `8.7265` n `91` status `ready` deltaP `18.6166` edge `1.3095` maxDD `-17.8526`
- `market_context_high->crypto_alt_24h` score `1.6343` n `91` status `ready` deltaP `10.0578` edge `0.7537` maxDD `-35.5652`
- `market_context_high->crypto_major_4h` score `1.4835` n `91` status `ready` deltaP `17.554` edge `0.2062` maxDD `-6.9761`
- `market_context_high->fx_1h` score `0.2368` n `91` status `ready` deltaP `6.3977` edge `0.0013` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.207` n `91` status `ready` deltaP `9.8441` edge `0.0498` maxDD `-3.7778`
- `market_context_high->fx_4h` score `0.0559` n `91` status `ready` deltaP `10.6557` edge `0.0083` maxDD `-0.3077`
- `market_context_high->metal_1h` score `-0.3217` n `91` status `ready` deltaP `3.4481` edge `0.0014` maxDD `-0.7626`
- `market_context_high->commodity_1h` score `-0.3351` n `91` status `ready` deltaP `1.0019` edge `0.003` maxDD `-0.3417`
- `market_context_high->metal_24h` score `-0.3586` n `91` status `ready` deltaP `6.5439` edge `0.0589` maxDD `-3.5466`
- `market_context_high->index_24h` score `-0.3746` n `91` status `ready` deltaP `7.8638` edge `0.0905` maxDD `-1.9432`
- `market_context_high->commodity_4h` score `-0.6649` n `91` status `ready` deltaP `-0.727` edge `-0.0104` maxDD `-1.6002`
- `market_context_high->equity_1h` score `-0.9064` n `91` status `ready` deltaP `-4.1389` edge `-0.0046` maxDD `-2.0542`
- `market_context_high->unknown_1h` score `-0.9594` n `91` status `ready` deltaP `-3.7688` edge `-0.0133` maxDD `-0.9885`
- `market_context_high->metal_4h` score `-1.014` n `91` status `ready` deltaP `-6.3807` edge `0.0133` maxDD `-1.0609`
- `market_context_high->crypto_alt_4h` score `-1.0423` n `91` status `ready` deltaP `-7.5617` edge `0.1101` maxDD `-8.7986`
- `market_context_high->crypto_alt_1h` score `-1.1616` n `91` status `ready` deltaP `-2.0941` edge `0.031` maxDD `-4.7735`
- `market_context_high->index_1h` score `-1.21` n `91` status `ready` deltaP `-9.8885` edge `-0.003` maxDD `-0.5627`
- `market_context_high->index_4h` score `-1.2304` n `91` status `ready` deltaP `-9.798` edge `0.0008` maxDD `-1.1242`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
