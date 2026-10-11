# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T05:07:28.227264+00:00`
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

- `market_context_high->unknown_4h` score `43.2597` n `85` status `ready` deltaP `-9.8763` edge `3.7247` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.7459` n `81` status `ready` deltaP `38.5417` edge `0.5981` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `8.4303` n `81` status `ready` deltaP `16.8789` edge `1.2831` maxDD `-17.8526`
- `market_context_high->crypto_major_4h` score `1.1521` n `85` status `ready` deltaP `13.7249` edge `0.197` maxDD `-7.597`
- `market_context_high->fx_4h` score `0.7706` n `85` status `ready` deltaP `15.5577` edge `0.0097` maxDD `-0.2692`
- `market_context_high->fx_1h` score `0.2507` n `97` status `ready` deltaP `8.2289` edge `0.0015` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.0929` n `97` status `ready` deltaP `8.4295` edge `0.0446` maxDD `-3.7778`
- `market_context_high->commodity_1h` score `-0.052` n `97` status `ready` deltaP `3.3907` edge `0.0065` maxDD `-0.3417`
- `market_context_high->commodity_4h` score `-0.2056` n `85` status `ready` deltaP `4.1212` edge `-0.0005` maxDD `-1.6002`
- `market_context_high->crypto_alt_24h` score `-0.4202` n `81` status `ready` deltaP `4.7646` edge `0.5256` maxDD `-35.5652`
- `market_context_high->index_24h` score `-0.4568` n `81` status `ready` deltaP `5.9992` edge `0.0924` maxDD `-1.9432`
- `market_context_high->metal_24h` score `-0.5457` n `81` status `ready` deltaP `4.7454` edge `0.0469` maxDD `-3.5466`
- `market_context_high->metal_1h` score `-0.5514` n `97` status `ready` deltaP `-3.0434` edge `0.0008` maxDD `-0.7626`
- `market_context_high->crypto_alt_1h` score `-0.8164` n `97` status `ready` deltaP `-1.747` edge `0.0229` maxDD `-4.9401`
- `market_context_high->metal_4h` score `-1.2885` n `85` status `ready` deltaP `-11.7001` edge `0.0137` maxDD `-1.0714`
- `market_context_high->equity_1h` score `-1.4698` n `97` status `ready` deltaP `-4.4586` edge `-0.0058` maxDD `-2.2898`
- `market_context_high->equity_4h` score `-1.607` n `85` status `ready` deltaP `-8.1671` edge `-0.0009` maxDD `-5.7208`
- `market_context_high->index_1h` score `-1.7834` n `97` status `ready` deltaP `-8.9126` edge `-0.003` maxDD `-0.5627`
- `market_context_high->crypto_alt_4h` score `-1.8261` n `85` status `ready` deltaP `-11.4581` edge `0.0537` maxDD `-10.2476`
- `market_context_high->fx_24h` score `-1.8523` n `81` status `ready` deltaP `-3.9738` edge `-0.0061` maxDD `-2.7244`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
