# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T05:37:30.981329+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `5933`

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

- `market_context_high->unknown_4h` score `42.9902` n `85` status `ready` deltaP `-11.9243` edge `3.7159` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.7092` n `79` status `ready` deltaP `38.6076` edge `0.5946` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `8.1707` n `79` status `ready` deltaP `16.1634` edge `1.2546` maxDD `-17.8526`
- `market_context_high->fx_4h` score `0.9586` n `85` status `ready` deltaP `16.5818` edge `0.0102` maxDD `-0.2692`
- `market_context_high->crypto_major_4h` score `0.8903` n `85` status `ready` deltaP `11.6768` edge `0.1839` maxDD `-8.1419`
- `market_context_high->fx_1h` score `0.1583` n `97` status `ready` deltaP `6.4665` edge `0.0014` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.0628` n `97` status `ready` deltaP `7.5483` edge `0.0438` maxDD `-3.7778`
- `market_context_high->commodity_1h` score `-0.046` n `97` status `ready` deltaP `3.3907` edge `0.007` maxDD `-0.3417`
- `market_context_high->commodity_4h` score `-0.143` n `85` status `ready` deltaP `5.1453` edge `0.0007` maxDD `-1.6002`
- `market_context_high->index_24h` score `-0.4009` n `79` status `ready` deltaP `6.1885` edge `0.0938` maxDD `-1.9163`
- `market_context_high->metal_24h` score `-0.5911` n `79` status `ready` deltaP `3.8875` edge `0.0468` maxDD `-3.5466`
- `market_context_high->metal_1h` score `-0.6446` n `97` status `ready` deltaP `-4.8058` edge `0.0006` maxDD `-0.7626`
- `market_context_high->crypto_alt_24h` score `-0.7668` n `79` status `ready` deltaP `3.4832` edge `0.4897` maxDD `-35.5652`
- `market_context_high->crypto_alt_1h` score `-0.7883` n `97` status `ready` deltaP `-1.747` edge `0.0265` maxDD `-4.9401`
- `market_context_high->metal_4h` score `-1.3435` n `85` status `ready` deltaP `-12.7242` edge `0.0136` maxDD `-1.0812`
- `market_context_high->equity_1h` score `-1.5439` n `97` status `ready` deltaP `-5.3398` edge `-0.0061` maxDD `-2.2898`
- `market_context_high->fx_24h` score `-1.6973` n `79` status `ready` deltaP `-2.8174` edge `-0.0045` maxDD `-2.5459`
- `market_context_high->index_1h` score `-1.7834` n `97` status `ready` deltaP `-8.9126` edge `-0.003` maxDD `-0.5627`
- `market_context_high->index_4h` score `-2.2659` n `85` status `ready` deltaP `-14.401` edge `0.0004` maxDD `-1.1242`
- `market_context_high->equity_4h` score `-2.6734` n `85` status `ready` deltaP `-10.2152` edge `-0.0027` maxDD `-5.8254`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
