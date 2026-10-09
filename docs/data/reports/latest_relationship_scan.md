# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-09T12:22:30.068594+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8505`

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

- `market_context_high->unknown_4h` score `40.4455` n `91` status `ready` deltaP `-5.2734` edge `3.4595` maxDD `-2.3109`
- `market_context_high->equity_24h` score `10.0845` n `91` status `ready` deltaP `33.3391` edge `0.661` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `9.6089` n `91` status `ready` deltaP `21.6652` edge `1.4023` maxDD `-17.8526`
- `market_context_high->crypto_alt_24h` score `3.1765` n `91` status `ready` deltaP `13.452` edge `0.9288` maxDD `-35.5652`
- `market_context_high->crypto_major_4h` score `1.9923` n `91` status `ready` deltaP `18.7735` edge `0.2633` maxDD `-6.9761`
- `market_context_high->metal_24h` score `0.5589` n `91` status `ready` deltaP `14.2571` edge `0.1251` maxDD `-3.5466`
- `market_context_high->fx_1h` score `0.3074` n `91` status `ready` deltaP `7.2959` edge `0.0012` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.3045` n `91` status `ready` deltaP `9.9938` edge `0.0613` maxDD `-3.7778`
- `market_context_high->fx_4h` score `0.1123` n `91` status `ready` deltaP `11.5703` edge `0.0069` maxDD `-0.3077`
- `market_context_high->crypto_alt_4h` score `-0.2419` n `91` status `ready` deltaP `-5.58` edge `0.1995` maxDD `-8.7986`
- `market_context_high->metal_1h` score `-0.2534` n `91` status `ready` deltaP `4.0469` edge `0.0031` maxDD `-0.7626`
- `market_context_high->index_24h` score `-0.2942` n `91` status `ready` deltaP `8.3009` edge `0.0979` maxDD `-1.9432`
- `market_context_high->commodity_1h` score `-0.4418` n `91` status `ready` deltaP `0.2534` edge `-0.0009` maxDD `-0.3417`
- `market_context_high->metal_4h` score `-0.7924` n `91` status `ready` deltaP `-3.4844` edge `0.0224` maxDD `-1.0609`
- `market_context_high->crypto_alt_1h` score `-0.8604` n `91` status `ready` deltaP `-1.645` edge `0.0531` maxDD `-4.7735`
- `market_context_high->equity_1h` score `-0.8691` n `91` status `ready` deltaP `-3.091` edge `-0.0068` maxDD `-2.0542`
- `market_context_high->commodity_4h` score `-0.8795` n `91` status `ready` deltaP `-2.7087` edge `-0.0247` maxDD `-1.6002`
- `market_context_high->index_1h` score `-1.2326` n `91` status `ready` deltaP `-10.1879` edge `-0.0039` maxDD `-0.5627`
- `market_context_high->index_4h` score `-1.303` n `91` status `ready` deltaP `-10.8651` edge `-0.0014` maxDD `-1.1242`
- `market_context_high->equity_4h` score `-1.3578` n `91` status `ready` deltaP `-4.5061` edge `0.0029` maxDD `-5.4217`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
