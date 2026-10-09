# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-09T11:37:30.118208+00:00`
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

- `market_context_high->unknown_4h` score `40.1745` n `91` status `ready` deltaP `-5.1209` edge `3.4359` maxDD `-2.3109`
- `market_context_high->equity_24h` score `10.0809` n `91` status `ready` deltaP `33.3391` edge `0.6607` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `9.6729` n `91` status `ready` deltaP `21.6652` edge `1.4105` maxDD `-17.8526`
- `market_context_high->crypto_alt_24h` score `3.2374` n `91` status `ready` deltaP `13.452` edge `0.9366` maxDD `-35.5652`
- `market_context_high->crypto_major_4h` score `1.9806` n `91` status `ready` deltaP `18.7735` edge `0.2618` maxDD `-6.9761`
- `market_context_high->metal_24h` score `0.6187` n `91` status `ready` deltaP `14.778` edge `0.1293` maxDD `-3.5466`
- `market_context_high->crypto_major_1h` score `0.3333` n `91` status `ready` deltaP `10.1435` edge `0.064` maxDD `-3.7778`
- `market_context_high->fx_1h` score `0.3074` n `91` status `ready` deltaP `7.2959` edge `0.0012` maxDD `-0.271`
- `market_context_high->fx_4h` score `0.0953` n `91` status `ready` deltaP `11.4179` edge `0.0065` maxDD `-0.3077`
- `market_context_high->metal_1h` score `-0.2355` n `91` status `ready` deltaP `4.1966` edge `0.0036` maxDD `-0.7626`
- `market_context_high->index_24h` score `-0.2965` n `91` status `ready` deltaP `8.3009` edge `0.0976` maxDD `-1.9432`
- `market_context_high->crypto_alt_4h` score `-0.3039` n `91` status `ready` deltaP `-6.0373` edge `0.1946` maxDD `-8.7986`
- `market_context_high->commodity_1h` score `-0.4562` n `91` status `ready` deltaP `0.1037` edge `-0.0011` maxDD `-0.3417`
- `market_context_high->crypto_alt_1h` score `-0.8017` n `91` status `ready` deltaP `-1.3456` edge `0.056` maxDD `-4.7735`
- `market_context_high->metal_4h` score `-0.8114` n `91` status `ready` deltaP `-3.7892` edge `0.022` maxDD `-1.0609`
- `market_context_high->equity_1h` score `-0.8356` n `91` status `ready` deltaP `-2.6419` edge `-0.0055` maxDD `-2.0542`
- `market_context_high->commodity_4h` score `-0.9008` n `91` status `ready` deltaP `-3.0136` edge `-0.0254` maxDD `-1.6002`
- `market_context_high->index_1h` score `-1.2076` n `91` status `ready` deltaP `-9.7388` edge `-0.0037` maxDD `-0.5627`
- `market_context_high->index_4h` score `-1.333` n `91` status `ready` deltaP `-11.3224` edge `-0.0022` maxDD `-1.1242`
- `market_context_high->equity_4h` score `-1.3774` n `91` status `ready` deltaP `-4.6586` edge `0.0014` maxDD `-5.4217`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
