# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-09T18:22:31.094217+00:00`
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

- `market_context_high->unknown_4h` score `41.0899` n `91` status `ready` deltaP `-4.3587` edge `3.5071` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.9622` n `91` status `ready` deltaP `33.6863` edge `0.6485` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `8.6585` n `91` status `ready` deltaP `19.4082` edge `1.2955` maxDD `-17.8526`
- `market_context_high->crypto_alt_24h` score `2.0304` n `91` status `ready` deltaP `11.1951` edge `0.7969` maxDD `-35.5652`
- `market_context_high->crypto_major_4h` score `1.5868` n `91` status `ready` deltaP `18.0113` edge `0.2164` maxDD `-6.9761`
- `market_context_high->crypto_major_1h` score `0.2881` n `91` status `ready` deltaP `10.2932` edge `0.0572` maxDD `-3.7778`
- `market_context_high->fx_1h` score `0.2859` n `91` status `ready` deltaP `6.9965` edge `0.0014` maxDD `-0.271`
- `market_context_high->fx_4h` score `0.2216` n `91` status `ready` deltaP `12.6374` edge `0.0089` maxDD `-0.3077`
- `market_context_high->metal_24h` score `0.0838` n `91` status `ready` deltaP `10.6113` edge `0.0885` maxDD `-3.5466`
- `market_context_high->index_24h` score `-0.3232` n `91` status `ready` deltaP `7.9537` edge `0.0965` maxDD `-1.9432`
- `market_context_high->metal_1h` score `-0.3301` n `91` status `ready` deltaP `3.4481` edge `0.0007` maxDD `-0.7626`
- `market_context_high->commodity_1h` score `-0.425` n `91` status `ready` deltaP `0.4031` edge `-0.0005` maxDD `-0.3417`
- `market_context_high->crypto_alt_4h` score `-0.6773` n `91` status `ready` deltaP `-6.6471` edge `0.1508` maxDD `-8.7986`
- `market_context_high->crypto_alt_1h` score `-0.8509` n `91` status `ready` deltaP `-1.3456` edge `0.0519` maxDD `-4.7735`
- `market_context_high->equity_1h` score `-0.8534` n `91` status `ready` deltaP `-3.2407` edge `-0.0038` maxDD `-2.0542`
- `market_context_high->commodity_4h` score `-0.8561` n `91` status `ready` deltaP `-2.7087` edge `-0.0217` maxDD `-1.6002`
- `market_context_high->metal_4h` score `-0.9679` n `91` status `ready` deltaP `-5.3136` edge `0.0121` maxDD `-1.0609`
- `market_context_high->index_1h` score `-1.178` n `91` status `ready` deltaP `-9.2897` edge `-0.0029` maxDD `-0.5627`
- `market_context_high->index_4h` score `-1.228` n `91` status `ready` deltaP `-9.798` edge `0.0011` maxDD `-1.1242`
- `market_context_high->equity_4h` score `-1.2511` n `91` status `ready` deltaP `-3.7439` edge `0.0115` maxDD `-5.4217`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
