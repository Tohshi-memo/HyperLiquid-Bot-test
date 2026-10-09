# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-09T21:07:27.626840+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7623`

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

- `market_context_high->unknown_4h` score `41.0415` n `91` status `ready` deltaP `-4.6933` edge `3.5053` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.6993` n `91` status `ready` deltaP `33.2641` edge `0.6294` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `8.4749` n `91` status `ready` deltaP `18.4433` edge `1.2784` maxDD `-17.8526`
- `market_context_high->crypto_alt_24h` score `1.6514` n `91` status `ready` deltaP `10.0578` edge `0.7559` maxDD `-35.5652`
- `market_context_high->crypto_major_4h` score `1.4606` n `91` status `ready` deltaP `18.0892` edge `0.1997` maxDD `-6.9761`
- `market_context_high->fx_1h` score `0.2499` n `91` status `ready` deltaP `6.5474` edge `0.0014` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.2031` n `91` status `ready` deltaP `9.9938` edge `0.0483` maxDD `-3.7778`
- `market_context_high->fx_4h` score `0.1499` n `91` status `ready` deltaP `11.8003` edge `0.0085` maxDD `-0.3077`
- `market_context_high->metal_24h` score `-0.0008` n `91` status `ready` deltaP `10.5301` edge `0.0782` maxDD `-3.5466`
- `market_context_high->metal_1h` score `-0.3122` n `91` status `ready` deltaP `3.5978` edge `0.0012` maxDD `-0.7626`
- `market_context_high->index_24h` score `-0.3481` n `91` status `ready` deltaP `7.8638` edge `0.0939` maxDD `-1.9432`
- `market_context_high->commodity_1h` score `-0.3603` n `91` status `ready` deltaP `0.8522` edge `0.0019` maxDD `-0.3417`
- `market_context_high->commodity_4h` score `-0.6914` n `91` status `ready` deltaP `-1.1005` edge `-0.0113` maxDD `-1.6002`
- `market_context_high->equity_1h` score `-0.8955` n `91` status `ready` deltaP `-3.8395` edge `-0.0052` maxDD `-2.0542`
- `market_context_high->metal_4h` score `-0.946` n `91` status `ready` deltaP `-5.0881` edge `0.0134` maxDD `-1.0609`
- `market_context_high->crypto_alt_4h` score `-1.0118` n `91` status `ready` deltaP `-7.1705` edge `0.1114` maxDD `-8.7986`
- `market_context_high->crypto_alt_1h` score `-1.1352` n `91` status `ready` deltaP `-1.9444` edge `0.0322` maxDD `-4.7735`
- `market_context_high->index_1h` score `-1.2271` n `91` status `ready` deltaP `-10.1879` edge `-0.0032` maxDD `-0.5627`
- `market_context_high->index_4h` score `-1.2422` n `91` status `ready` deltaP `-10.0256` edge `0.0008` maxDD `-1.1242`
- `market_context_high->equity_4h` score `-1.3071` n `91` status `ready` deltaP `-4.4156` edge `0.0088` maxDD `-5.4217`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
