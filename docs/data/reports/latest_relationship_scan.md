# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T04:52:28.883790+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `5927`

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

- `market_context_high->unknown_4h` score `43.3896` n `85` status `ready` deltaP `-8.8522` edge `3.7287` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.7812` n `82` status `ready` deltaP `38.5036` edge `0.6013` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `8.577` n `82` status `ready` deltaP `17.3908` edge `1.2985` maxDD `-17.8526`
- `market_context_high->crypto_major_4h` score `1.2303` n `85` status `ready` deltaP `14.7489` edge `0.1999` maxDD `-7.5726`
- `market_context_high->fx_4h` score `0.6351` n `85` status `ready` deltaP `14.5338` edge `0.0094` maxDD `-0.2692`
- `market_context_high->fx_1h` score `0.2041` n `97` status `ready` deltaP `7.3477` edge `0.0014` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.0742` n `97` status `ready` deltaP `8.4295` edge `0.0422` maxDD `-3.7778`
- `market_context_high->commodity_1h` score `-0.0851` n `97` status `ready` deltaP `2.5094` edge `0.0058` maxDD `-0.3417`
- `market_context_high->crypto_alt_24h` score `-0.2469` n `82` status `ready` deltaP `5.3819` edge `0.5437` maxDD `-35.5652`
- `market_context_high->commodity_4h` score `-0.2729` n `85` status `ready` deltaP `3.0972` edge `-0.0023` maxDD `-1.6002`
- `market_context_high->index_24h` score `-0.4376` n `82` status `ready` deltaP `6.4278` edge `0.092` maxDD `-1.9432`
- `market_context_high->metal_1h` score `-0.5048` n `97` status `ready` deltaP `-2.1622` edge `0.0009` maxDD `-0.7626`
- `market_context_high->metal_24h` score `-0.5211` n `82` status `ready` deltaP `5.0686` edge `0.0479` maxDD `-3.5466`
- `market_context_high->crypto_alt_1h` score `-0.8671` n `97` status `ready` deltaP `-1.747` edge `0.0164` maxDD `-4.9401`
- `market_context_high->metal_4h` score `-1.288` n `85` status `ready` deltaP `-11.7001` edge `0.0137` maxDD `-1.0663`
- `market_context_high->equity_1h` score `-1.4734` n `97` status `ready` deltaP `-4.4586` edge `-0.0061` maxDD `-2.2898`
- `market_context_high->equity_4h` score `-1.54` n `85` status `ready` deltaP `-7.1431` edge `0.0002` maxDD `-5.6676`
- `market_context_high->index_1h` score `-1.7846` n `97` status `ready` deltaP `-8.9126` edge `-0.0031` maxDD `-0.5627`
- `market_context_high->crypto_alt_4h` score `-1.7848` n `85` status `ready` deltaP `-11.4581` edge `0.059` maxDD `-10.2476`
- `market_context_high->fx_24h` score `-1.9224` n `82` status `ready` deltaP `-4.5308` edge `-0.0065` maxDD `-2.781`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
