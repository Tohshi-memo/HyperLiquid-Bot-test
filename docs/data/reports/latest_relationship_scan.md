# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-09T17:07:31.488170+00:00`
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

- `market_context_high->unknown_4h` score `40.5179` n `91` status `ready` deltaP `-4.9685` edge `3.4635` maxDD `-2.3109`
- `market_context_high->equity_24h` score `10.1532` n `91` status `ready` deltaP `34.0335` edge `0.6621` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `8.9252` n `91` status `ready` deltaP `20.2763` edge `1.3239` maxDD `-17.8526`
- `market_context_high->crypto_alt_24h` score `2.4382` n `91` status `ready` deltaP `12.0632` edge `0.8434` maxDD `-35.5652`
- `market_context_high->crypto_major_4h` score `1.7237` n `91` status `ready` deltaP `18.4686` edge `0.2309` maxDD `-6.9761`
- `market_context_high->fx_1h` score `0.3362` n `91` status `ready` deltaP `7.5953` edge `0.0016` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.3044` n `91` status `ready` deltaP `10.4429` edge `0.0583` maxDD `-3.7778`
- `market_context_high->fx_4h` score `0.2594` n `91` status `ready` deltaP `13.0947` edge `0.009` maxDD `-0.3077`
- `market_context_high->metal_24h` score `0.1432` n `91` status `ready` deltaP `10.9585` edge `0.0938` maxDD `-3.5466`
- `market_context_high->metal_1h` score `-0.2702` n `91` status `ready` deltaP `4.0469` edge `0.0017` maxDD `-0.7626`
- `market_context_high->index_24h` score `-0.2895` n `91` status `ready` deltaP `8.3009` edge `0.0985` maxDD `-1.9432`
- `market_context_high->crypto_alt_4h` score `-0.3974` n `91` status `ready` deltaP `-5.8849` edge `0.1816` maxDD `-8.7986`
- `market_context_high->commodity_1h` score `-0.4909` n `91` status `ready` deltaP `-0.1957` edge `-0.002` maxDD `-0.3417`
- `market_context_high->equity_1h` score `-0.8168` n `91` status `ready` deltaP `-2.7916` edge `-0.0021` maxDD `-2.0542`
- `market_context_high->crypto_alt_1h` score `-0.8377` n `91` status `ready` deltaP `-1.1959` edge `0.052` maxDD `-4.7735`
- `market_context_high->commodity_4h` score `-0.8985` n `91` status `ready` deltaP `-3.0136` edge `-0.0251` maxDD `-1.6002`
- `market_context_high->metal_4h` score `-0.9781` n `91` status `ready` deltaP `-5.4661` edge `0.0118` maxDD `-1.0609`
- `market_context_high->index_1h` score `-1.1765` n `91` status `ready` deltaP `-9.2897` edge `-0.0027` maxDD `-0.5627`
- `market_context_high->equity_4h` score `-1.2047` n `91` status `ready` deltaP `-3.2866` edge `0.0144` maxDD `-5.4217`
- `market_context_high->index_4h` score `-1.2098` n `91` status `ready` deltaP `-9.4931` edge `0.0014` maxDD `-1.1242`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
