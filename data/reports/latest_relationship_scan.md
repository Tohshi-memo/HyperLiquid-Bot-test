# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-10T09:52:28.525011+00:00`
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

- `market_context_high->unknown_4h` score `40.9747` n `91` status `ready` deltaP `-6.188` edge `3.5097` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.7483` n `91` status `ready` deltaP `36.0371` edge `0.615` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `8.9643` n `91` status `ready` deltaP `19.4832` edge `1.3342` maxDD `-17.8526`
- `market_context_high->crypto_alt_24h` score `1.6584` n `91` status `ready` deltaP `10.0578` edge `0.7568` maxDD `-35.5652`
- `market_context_high->crypto_major_4h` score `1.2974` n `91` status `ready` deltaP `15.1149` edge `0.1986` maxDD `-6.9761`
- `market_context_high->fx_1h` score `0.2619` n `91` status `ready` deltaP `6.6971` edge `0.0014` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.1314` n `91` status `ready` deltaP `8.7962` edge `0.0471` maxDD `-3.7778`
- `market_context_high->fx_4h` score `-0.1062` n `91` status `ready` deltaP `8.674` edge `0.008` maxDD `-0.3077`
- `market_context_high->index_24h` score `-0.2512` n `91` status `ready` deltaP `10.1168` edge `0.0913` maxDD `-1.9432`
- `market_context_high->metal_1h` score `-0.2846` n `91` status `ready` deltaP `3.8972` edge `0.0015` maxDD `-0.7626`
- `market_context_high->commodity_1h` score `-0.3315` n `91` status `ready` deltaP `1.0019` edge `0.0033` maxDD `-0.3417`
- `market_context_high->metal_24h` score `-0.3777` n `91` status `ready` deltaP `6.3706` edge `0.0576` maxDD `-3.5466`
- `market_context_high->commodity_4h` score `-0.7394` n `91` status `ready` deltaP `-2.0989` edge `-0.0108` maxDD `-1.6002`
- `market_context_high->equity_1h` score `-0.9212` n `91` status `ready` deltaP `-4.4383` edge `-0.0045` maxDD `-2.0542`
- `market_context_high->unknown_1h` score `-0.9281` n `91` status `ready` deltaP `-4.0682` edge `-0.0087` maxDD `-0.9885`
- `market_context_high->metal_4h` score `-0.9562` n `91` status `ready` deltaP `-5.3136` edge `0.0136` maxDD `-1.0609`
- `market_context_high->crypto_alt_4h` score `-1.1338` n `91` status `ready` deltaP `-7.8666` edge `0.1004` maxDD `-8.7986`
- `market_context_high->crypto_alt_1h` score `-1.1963` n `91` status `ready` deltaP `-2.2438` edge `0.0291` maxDD `-4.7735`
- `market_context_high->index_1h` score `-1.2411` n `91` status `ready` deltaP `-10.4873` edge `-0.003` maxDD `-0.5627`
- `market_context_high->index_4h` score `-1.27` n `91` status `ready` deltaP `-10.5602` edge `0.0008` maxDD `-1.1242`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
