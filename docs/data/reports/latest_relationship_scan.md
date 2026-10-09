# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-09T19:37:29.581316+00:00`
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

- `market_context_high->unknown_4h` score `41.0167` n `91` status `ready` deltaP `-4.3889` edge `3.5012` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.7881` n `91` status `ready` deltaP `33.2641` edge `0.6368` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `8.498` n `91` status `ready` deltaP `18.6166` edge `1.2802` maxDD `-17.8526`
- `market_context_high->crypto_alt_24h` score `1.763` n `91` status `ready` deltaP `10.4044` edge `0.7679` maxDD `-35.5652`
- `market_context_high->crypto_major_4h` score `1.523` n `91` status `ready` deltaP `18.0892` edge `0.2077` maxDD `-6.9761`
- `market_context_high->fx_1h` score `0.2859` n `91` status `ready` deltaP `6.9965` edge `0.0014` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.2818` n `91` status `ready` deltaP `10.2932` edge `0.0564` maxDD `-3.7778`
- `market_context_high->fx_4h` score `0.2022` n `91` status `ready` deltaP `12.4091` edge `0.0088` maxDD `-0.3077`
- `market_context_high->metal_24h` score `0.0414` n `91` status `ready` deltaP `10.5301` edge `0.0836` maxDD `-3.5466`
- `market_context_high->index_24h` score `-0.3411` n `91` status `ready` deltaP `7.8638` edge `0.0948` maxDD `-1.9432`
- `market_context_high->metal_1h` score `-0.3433` n `91` status `ready` deltaP `3.2984` edge `0.0006` maxDD `-0.7626`
- `market_context_high->commodity_1h` score `-0.3471` n `91` status `ready` deltaP `1.0019` edge `0.002` maxDD `-0.3417`
- `market_context_high->commodity_4h` score `-0.7748` n `91` status `ready` deltaP `-2.0138` edge `-0.0159` maxDD `-1.6002`
- `market_context_high->crypto_alt_4h` score `-0.8769` n `91` status `ready` deltaP `-7.1705` edge `0.1287` maxDD `-8.7986`
- `market_context_high->equity_1h` score `-0.8776` n `91` status `ready` deltaP `-3.5401` edge `-0.0049` maxDD `-2.0542`
- `market_context_high->crypto_alt_1h` score `-0.8857` n `91` status `ready` deltaP `-1.3456` edge `0.049` maxDD `-4.7735`
- `market_context_high->metal_4h` score `-0.9688` n `91` status `ready` deltaP `-5.3925` edge `0.0125` maxDD `-1.0609`
- `market_context_high->index_1h` score `-1.2115` n `91` status `ready` deltaP `-9.8885` edge `-0.0032` maxDD `-0.5627`
- `market_context_high->index_4h` score `-1.2343` n `91` status `ready` deltaP `-9.8734` edge `0.0008` maxDD `-1.1242`
- `market_context_high->equity_4h` score `-1.2945` n `91` status `ready` deltaP `-4.2634` edge `0.0094` maxDD `-5.4217`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
