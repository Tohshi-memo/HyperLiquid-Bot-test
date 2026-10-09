# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-09T16:37:33.569326+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7887`

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

- `market_context_high->unknown_4h` score `40.3927` n `91` status `ready` deltaP `-5.2734` edge `3.4551` maxDD `-2.3109`
- `market_context_high->equity_24h` score `10.2614` n `91` status `ready` deltaP `34.3807` edge `0.6688` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `9.0493` n `91` status `ready` deltaP `20.6235` edge `1.3375` maxDD `-17.8526`
- `market_context_high->crypto_alt_24h` score `2.6091` n `91` status `ready` deltaP `12.4104` edge `0.863` maxDD `-35.5652`
- `market_context_high->crypto_major_4h` score `1.7651` n `91` status `ready` deltaP `18.4686` edge `0.2362` maxDD `-6.9761`
- `market_context_high->crypto_major_1h` score `0.3341` n `91` status `ready` deltaP `10.5926` edge `0.0611` maxDD `-3.7778`
- `market_context_high->fx_1h` score `0.323` n `91` status `ready` deltaP `7.4456` edge `0.0015` maxDD `-0.271`
- `market_context_high->fx_4h` score `0.2716` n `91` status `ready` deltaP `13.2472` edge `0.009` maxDD `-0.3077`
- `market_context_high->metal_24h` score `0.1862` n `91` status `ready` deltaP `11.3057` edge `0.097` maxDD `-3.5466`
- `market_context_high->metal_1h` score `-0.2594` n `91` status `ready` deltaP `4.0469` edge `0.0026` maxDD `-0.7626`
- `market_context_high->index_24h` score `-0.2637` n `91` status `ready` deltaP `8.6482` edge `0.0995` maxDD `-1.9432`
- `market_context_high->crypto_alt_4h` score `-0.302` n `91` status `ready` deltaP `-5.58` edge `0.1918` maxDD `-8.7986`
- `market_context_high->commodity_1h` score `-0.5305` n `91` status `ready` deltaP `-0.4951` edge `-0.0033` maxDD `-0.3417`
- `market_context_high->equity_1h` score `-0.7818` n `91` status `ready` deltaP `-2.4922` edge `0.0004` maxDD `-2.0542`
- `market_context_high->crypto_alt_1h` score `-0.7981` n `91` status `ready` deltaP `-1.0462` edge `0.0543` maxDD `-4.7735`
- `market_context_high->commodity_4h` score `-0.9133` n `91` status `ready` deltaP `-3.0136` edge `-0.027` maxDD `-1.6002`
- `market_context_high->metal_4h` score `-0.9514` n `91` status `ready` deltaP `-5.1612` edge `0.0132` maxDD `-1.0609`
- `market_context_high->index_1h` score `-1.157` n `91` status `ready` deltaP `-8.9903` edge `-0.0022` maxDD `-0.5627`
- `market_context_high->equity_4h` score `-1.1922` n `91` status `ready` deltaP `-3.2866` edge `0.016` maxDD `-5.4217`
- `market_context_high->index_4h` score `-1.1988` n `91` status `ready` deltaP `-9.3407` edge `0.0018` maxDD `-1.1242`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
