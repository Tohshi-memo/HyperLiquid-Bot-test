# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-09T14:37:27.290881+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8541`

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

- `market_context_high->unknown_4h` score `40.2259` n `91` status `ready` deltaP `-5.2734` edge `3.4412` maxDD `-2.3109`
- `market_context_high->equity_24h` score `10.3379` n `91` status `ready` deltaP `34.9016` edge `0.6717` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `9.4529` n `91` status `ready` deltaP `21.6652` edge `1.3823` maxDD `-17.8526`
- `market_context_high->crypto_alt_24h` score `3.111` n `91` status `ready` deltaP `13.452` edge `0.9204` maxDD `-35.5652`
- `market_context_high->crypto_major_4h` score `1.9087` n `91` status `ready` deltaP `18.621` edge `0.2536` maxDD `-6.9761`
- `market_context_high->crypto_major_1h` score `0.3824` n `91` status `ready` deltaP `10.7423` edge `0.0663` maxDD `-3.7778`
- `market_context_high->metal_24h` score `0.3754` n `91` status `ready` deltaP `12.6946` edge `0.112` maxDD `-3.5466`
- `market_context_high->fx_1h` score `0.2691` n `91` status `ready` deltaP `6.8468` edge `0.001` maxDD `-0.271`
- `market_context_high->fx_4h` score `0.2388` n `91` status `ready` deltaP `12.9423` edge `0.0083` maxDD `-0.3077`
- `market_context_high->crypto_alt_4h` score `-0.1455` n `91` status `ready` deltaP `-4.9702` edge `0.2078` maxDD `-8.7986`
- `market_context_high->metal_1h` score `-0.2211` n `91` status `ready` deltaP `4.3463` edge `0.0038` maxDD `-0.7626`
- `market_context_high->index_24h` score `-0.2213` n `91` status `ready` deltaP `9.3426` edge `0.1003` maxDD `-1.9432`
- `market_context_high->commodity_1h` score `-0.5125` n `91` status `ready` deltaP `-0.3454` edge `-0.0028` maxDD `-0.3417`
- `market_context_high->crypto_alt_1h` score `-0.701` n `91` status `ready` deltaP `-0.5971` edge `0.0594` maxDD `-4.7735`
- `market_context_high->equity_1h` score `-0.809` n `91` status `ready` deltaP `-2.7916` edge `-0.0011` maxDD `-2.0542`
- `market_context_high->metal_4h` score `-0.8396` n `91` status `ready` deltaP `-3.9417` edge `0.0194` maxDD `-1.0609`
- `market_context_high->commodity_4h` score `-0.9133` n `91` status `ready` deltaP `-3.0136` edge `-0.027` maxDD `-1.6002`
- `market_context_high->index_1h` score `-1.1757` n `91` status `ready` deltaP `-9.2897` edge `-0.0026` maxDD `-0.5627`
- `market_context_high->index_4h` score `-1.2067` n `91` status `ready` deltaP `-9.4931` edge `0.0018` maxDD `-1.1242`
- `market_context_high->equity_4h` score `-1.2111` n `91` status `ready` deltaP `-3.439` edge `0.0146` maxDD `-5.4217`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
