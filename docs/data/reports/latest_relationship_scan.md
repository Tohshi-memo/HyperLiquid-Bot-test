# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-09T14:22:33.298006+00:00`
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

- `market_context_high->unknown_4h` score `40.2331` n `91` status `ready` deltaP `-5.2734` edge `3.4418` maxDD `-2.3109`
- `market_context_high->equity_24h` score `10.3` n `91` status `ready` deltaP `34.728` edge `0.6697` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `9.4669` n `91` status `ready` deltaP `21.6652` edge `1.3841` maxDD `-17.8526`
- `market_context_high->crypto_alt_24h` score `3.1126` n `91` status `ready` deltaP `13.452` edge `0.9206` maxDD `-35.5652`
- `market_context_high->crypto_major_4h` score `1.9338` n `91` status `ready` deltaP `18.7735` edge `0.2558` maxDD `-6.9761`
- `market_context_high->metal_24h` score `0.3954` n `91` status `ready` deltaP `12.8682` edge `0.1134` maxDD `-3.5466`
- `market_context_high->crypto_major_1h` score `0.384` n `91` status `ready` deltaP `10.7423` edge `0.0665` maxDD `-3.7778`
- `market_context_high->fx_1h` score `0.2823` n `91` status `ready` deltaP `6.9965` edge `0.0011` maxDD `-0.271`
- `market_context_high->fx_4h` score `0.2242` n `91` status `ready` deltaP `12.7898` edge `0.0081` maxDD `-0.3077`
- `market_context_high->crypto_alt_4h` score `-0.1447` n `91` status `ready` deltaP `-4.9702` edge `0.2079` maxDD `-8.7986`
- `market_context_high->index_24h` score `-0.2335` n `91` status `ready` deltaP `9.169` edge `0.0999` maxDD `-1.9432`
- `market_context_high->metal_1h` score `-0.2367` n `91` status `ready` deltaP `4.1966` edge `0.0035` maxDD `-0.7626`
- `market_context_high->commodity_1h` score `-0.4957` n `91` status `ready` deltaP `-0.1957` edge `-0.0024` maxDD `-0.3417`
- `market_context_high->crypto_alt_1h` score `-0.707` n `91` status `ready` deltaP `-0.5971` edge `0.0589` maxDD `-4.7735`
- `market_context_high->equity_1h` score `-0.8262` n `91` status `ready` deltaP `-2.9413` edge `-0.0023` maxDD `-2.0542`
- `market_context_high->metal_4h` score `-0.8262` n `91` status `ready` deltaP `-3.7892` edge `0.0201` maxDD `-1.0609`
- `market_context_high->commodity_4h` score `-0.911` n `91` status `ready` deltaP `-3.0136` edge `-0.0267` maxDD `-1.6002`
- `market_context_high->index_1h` score `-1.1858` n `91` status `ready` deltaP `-9.4394` edge `-0.0029` maxDD `-0.5627`
- `market_context_high->index_4h` score `-1.217` n `91` status `ready` deltaP `-9.6456` edge `0.0015` maxDD `-1.1242`
- `market_context_high->equity_4h` score `-1.2291` n `91` status `ready` deltaP `-3.5915` edge `0.0133` maxDD `-5.4217`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
