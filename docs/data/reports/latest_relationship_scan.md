# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-10T07:07:29.764400+00:00`
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

- `market_context_high->unknown_4h` score `40.8907` n `91` status `ready` deltaP `-6.188` edge `3.5027` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.477` n `91` status `ready` deltaP `34.1307` edge `0.6051` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `8.7995` n `91` status `ready` deltaP `18.7899` edge `1.3177` maxDD `-17.8526`
- `market_context_high->crypto_alt_24h` score `1.5726` n `91` status `ready` deltaP `10.0578` edge `0.7458` maxDD `-35.5652`
- `market_context_high->crypto_major_4h` score `1.3778` n `91` status `ready` deltaP `16.182` edge `0.2018` maxDD `-6.9761`
- `market_context_high->fx_1h` score `0.2607` n `91` status `ready` deltaP `6.6971` edge `0.0013` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.1673` n `91` status `ready` deltaP `9.395` edge `0.0477` maxDD `-3.7778`
- `market_context_high->fx_4h` score `-0.0551` n `91` status `ready` deltaP `9.2837` edge `0.0082` maxDD `-0.3077`
- `market_context_high->metal_1h` score `-0.2846` n `91` status `ready` deltaP `3.8972` edge `0.0015` maxDD `-0.7626`
- `market_context_high->index_24h` score `-0.3597` n `91` status `ready` deltaP `8.2104` edge `0.0901` maxDD `-1.9432`
- `market_context_high->metal_24h` score `-0.3934` n `91` status `ready` deltaP `6.024` edge `0.0579` maxDD `-3.5466`
- `market_context_high->commodity_1h` score `-0.413` n `91` status `ready` deltaP `0.1037` edge `0.0025` maxDD `-0.3417`
- `market_context_high->commodity_4h` score `-0.7551` n `91` status `ready` deltaP `-2.2514` edge `-0.0118` maxDD `-1.6002`
- `market_context_high->equity_1h` score `-0.9313` n `91` status `ready` deltaP `-4.588` edge `-0.0048` maxDD `-2.0542`
- `market_context_high->metal_4h` score `-0.9569` n `91` status `ready` deltaP `-5.3136` edge `0.0135` maxDD `-1.0609`
- `market_context_high->unknown_1h` score `-1.0182` n `91` status `ready` deltaP `-3.9185` edge `-0.0172` maxDD `-0.9885`
- `market_context_high->crypto_alt_4h` score `-1.1513` n `91` status `ready` deltaP `-8.3239` edge `0.1012` maxDD `-8.7986`
- `market_context_high->crypto_alt_1h` score `-1.1676` n `91` status `ready` deltaP `-2.0941` edge `0.0305` maxDD `-4.7735`
- `market_context_high->index_1h` score `-1.2497` n `91` status `ready` deltaP `-10.637` edge `-0.0031` maxDD `-0.5627`
- `market_context_high->index_4h` score `-1.2969` n `91` status `ready` deltaP `-11.0175` edge `0.0004` maxDD `-1.1242`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
