# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-10T09:37:25.687497+00:00`
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

- `market_context_high->unknown_4h` score `40.9579` n `91` status `ready` deltaP `-6.188` edge `3.5083` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.7248` n `91` status `ready` deltaP `35.8638` edge `0.6142` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `8.9502` n `91` status `ready` deltaP `19.4832` edge `1.3324` maxDD `-17.8526`
- `market_context_high->crypto_alt_24h` score `1.6491` n `91` status `ready` deltaP `10.0578` edge `0.7556` maxDD `-35.5652`
- `market_context_high->crypto_major_4h` score `1.2871` n `91` status `ready` deltaP `14.9625` edge `0.1983` maxDD `-6.9761`
- `market_context_high->fx_1h` score `0.2619` n `91` status `ready` deltaP `6.6971` edge `0.0014` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.1307` n `91` status `ready` deltaP `8.7962` edge `0.047` maxDD `-3.7778`
- `market_context_high->fx_4h` score `-0.1062` n `91` status `ready` deltaP `8.674` edge `0.008` maxDD `-0.3077`
- `market_context_high->index_24h` score `-0.261` n `91` status `ready` deltaP `9.9435` edge `0.0912` maxDD `-1.9432`
- `market_context_high->metal_1h` score `-0.2966` n `91` status `ready` deltaP `3.7475` edge `0.0015` maxDD `-0.7626`
- `market_context_high->commodity_1h` score `-0.3471` n `91` status `ready` deltaP `0.8522` edge `0.003` maxDD `-0.3417`
- `market_context_high->metal_24h` score `-0.368` n `91` status `ready` deltaP `6.5439` edge `0.0577` maxDD `-3.5466`
- `market_context_high->commodity_4h` score `-0.7505` n `91` status `ready` deltaP `-2.2514` edge `-0.0112` maxDD `-1.6002`
- `market_context_high->equity_1h` score `-0.922` n `91` status `ready` deltaP `-4.4383` edge `-0.0046` maxDD `-2.0542`
- `market_context_high->unknown_1h` score `-0.9293` n `91` status `ready` deltaP `-4.0682` edge `-0.0088` maxDD `-0.9885`
- `market_context_high->metal_4h` score `-0.9482` n `91` status `ready` deltaP `-5.1612` edge `0.0136` maxDD `-1.0609`
- `market_context_high->crypto_alt_4h` score `-1.1495` n `91` status `ready` deltaP `-8.019` edge `0.0994` maxDD `-8.7986`
- `market_context_high->crypto_alt_1h` score `-1.1891` n `91` status `ready` deltaP `-2.2438` edge `0.0297` maxDD `-4.7735`
- `market_context_high->index_1h` score `-1.2325` n `91` status `ready` deltaP `-10.3376` edge `-0.0029` maxDD `-0.5627`
- `market_context_high->index_4h` score `-1.2779` n `91` status `ready` deltaP `-10.7127` edge `0.0008` maxDD `-1.1242`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
