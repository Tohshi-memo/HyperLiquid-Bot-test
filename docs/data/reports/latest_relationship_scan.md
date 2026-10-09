# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-09T07:07:48.616905+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8870`

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

- `market_context_high->unknown_4h` score `40.9712` n `91` status `ready` deltaP `-3.2917` edge `3.4901` maxDD `-2.3109`
- `market_context_high->crypto_major_24h` score `10.0112` n `90` status `ready` deltaP `22.3611` edge `1.4318` maxDD `-16.7906`
- `market_context_high->equity_24h` score `9.7366` n `90` status `ready` deltaP `31.7361` edge `0.6427` maxDD `-1.0977`
- `market_context_high->crypto_alt_24h` score `3.6078` n `90` status `ready` deltaP `14.0625` edge `0.9626` maxDD `-34.5048`
- `market_context_high->crypto_major_4h` score `1.8636` n `91` status `ready` deltaP `17.8588` edge `0.2529` maxDD `-6.9761`
- `market_context_high->metal_24h` score `0.9147` n `90` status `ready` deltaP `17.5` edge `0.1491` maxDD `-3.5466`
- `market_context_high->fx_1h` score `0.3362` n `91` status `ready` deltaP `7.5953` edge `0.0016` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.3006` n `91` status `ready` deltaP `9.9938` edge `0.0608` maxDD `-3.7778`
- `market_context_high->fx_4h` score `0.2156` n `91` status `ready` deltaP `12.6374` edge `0.0084` maxDD `-0.3077`
- `market_context_high->metal_1h` score `-0.2091` n `91` status `ready` deltaP `4.496` edge `0.0038` maxDD `-0.7626`
- `market_context_high->commodity_1h` score `-0.3459` n `91` status `ready` deltaP `1.0019` edge `0.0021` maxDD `-0.3417`
- `market_context_high->index_24h` score `-0.3594` n `90` status `ready` deltaP `7.8125` edge `0.0928` maxDD `-1.9432`
- `market_context_high->crypto_alt_4h` score `-0.4195` n `91` status `ready` deltaP `-7.1044` edge `0.1869` maxDD `-8.7986`
- `market_context_high->metal_4h` score `-0.7625` n `91` status `ready` deltaP `-3.1795` edge `0.0242` maxDD `-1.0609`
- `market_context_high->commodity_4h` score `-0.8481` n `91` status `ready` deltaP `-3.3184` edge `-0.0166` maxDD `-1.6002`
- `market_context_high->equity_1h` score `-0.8699` n `91` status `ready` deltaP `-2.9413` edge `-0.0079` maxDD `-2.0542`
- `market_context_high->crypto_alt_1h` score `-0.9156` n `91` status `ready` deltaP `-1.9444` edge `0.0505` maxDD `-4.7735`
- `market_context_high->index_1h` score `-1.2598` n `91` status `ready` deltaP `-10.637` edge `-0.0044` maxDD `-0.5627`
- `market_context_high->equity_4h` score `-1.3729` n `91` status `ready` deltaP `-4.811` edge `0.003` maxDD `-5.4217`
- `market_context_high->index_4h` score `-1.3757` n `91` status `ready` deltaP `-11.9322` edge `-0.0036` maxDD `-1.1242`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
