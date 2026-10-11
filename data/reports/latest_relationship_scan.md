# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T10:52:27.139735+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `6933`

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

- `market_context_high->unknown_24h` score `86.3734` n `58` status `ready` deltaP `-17.8879` edge `7.3534` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `43.018` n `85` status `ready` deltaP `-8.8522` edge `3.7019` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.1563` n `58` status `ready` deltaP `35.1772` edge `0.5714` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `5.5765` n `58` status `ready` deltaP `3.8793` edge `1.0039` maxDD `-17.8526`
- `market_context_high->index_24h` score `1.4824` n `58` status `ready` deltaP `23.4794` edge `0.1227` maxDD `-1.1338`
- `market_context_high->fx_4h` score `1.2688` n `85` status `ready` deltaP `18.6298` edge `0.0099` maxDD `-0.2692`
- `market_context_high->commodity_4h` score `0.2868` n `85` status `ready` deltaP `10.2655` edge `0.0088` maxDD `-1.6002`
- `market_context_high->commodity_1h` score `0.2451` n `90` status `ready` deltaP `5.509` edge `0.0088` maxDD `-0.3417`
- `market_context_high->fx_24h` score `0.1764` n `58` status `ready` deltaP `13.4459` edge `0.0179` maxDD `-0.7939`
- `market_context_high->fx_1h` score `0.1034` n `90` status `ready` deltaP `4.6108` edge `0.0021` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `-0.4795` n `90` status `ready` deltaP `0.3626` edge `0.025` maxDD `-3.7778`
- `market_context_high->metal_4h` score `-0.5712` n `85` status `ready` deltaP `-2.4839` edge `0.0156` maxDD `-1.1153`
- `market_context_high->metal_1h` score `-0.6154` n `90` status `ready` deltaP `-3.1204` edge `0.0014` maxDD `-0.7591`
- `market_context_high->crypto_alt_1h` score `-0.8728` n `90` status `ready` deltaP `-4.6174` edge `0.0223` maxDD `-4.9401`
- `market_context_high->crypto_major_4h` score `-1.238` n `85` status `ready` deltaP `-4.7076` edge `0.0813` maxDD `-11.0244`
- `market_context_high->index_4h` score `-1.3162` n `85` status `ready` deltaP `-11.3289` edge `0.0` maxDD `-1.1242`
- `market_context_high->metal_24h` score `-1.5241` n `58` status `ready` deltaP `-10.8897` edge `0.0257` maxDD `-3.5466`
- `market_context_high->index_1h` score `-1.5337` n `90` status `ready` deltaP `-5.7917` edge `-0.003` maxDD `-0.5627`
- `market_context_high->equity_1h` score `-1.6087` n `90` status `ready` deltaP `-5.9248` edge `-0.0076` maxDD `-2.2898`
- `market_context_high->crypto_alt_4h` score `-2.0081` n `85` status `ready` deltaP `-8.3859` edge `0.0543` maxDD `-13.8008`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
