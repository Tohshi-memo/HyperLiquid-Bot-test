# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T04:37:31.721968+00:00`
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

- `market_context_high->unknown_4h` score `43.5627` n `85` status `ready` deltaP `-7.8282` edge `3.7363` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.8163` n `83` status `ready` deltaP `38.4622` edge `0.6045` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `8.7278` n `83` status `ready` deltaP `17.8903` edge `1.3145` maxDD `-17.8526`
- `market_context_high->crypto_major_4h` score `1.3088` n `85` status `ready` deltaP `15.773` edge `0.2028` maxDD `-7.5461`
- `market_context_high->fx_4h` score `0.4996` n `85` status `ready` deltaP `13.5097` edge `0.0091` maxDD `-0.2692`
- `market_context_high->fx_1h` score `0.1575` n `97` status `ready` deltaP `6.4665` edge `0.0013` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.0523` n `97` status `ready` deltaP `8.4295` edge `0.0394` maxDD `-3.7778`
- `market_context_high->crypto_alt_24h` score `-0.0689` n `83` status `ready` deltaP `5.9843` edge `0.5625` maxDD `-35.5652`
- `market_context_high->commodity_1h` score `-0.1356` n `97` status `ready` deltaP `1.6282` edge `0.0052` maxDD `-0.3417`
- `market_context_high->commodity_4h` score `-0.3371` n `85` status `ready` deltaP `2.0732` edge `-0.0037` maxDD `-1.6002`
- `market_context_high->index_24h` score `-0.4176` n `83` status `ready` deltaP `6.8419` edge `0.0918` maxDD `-1.9432`
- `market_context_high->metal_1h` score `-0.4582` n `97` status `ready` deltaP `-1.2809` edge `0.001` maxDD `-0.7626`
- `market_context_high->metal_24h` score `-0.4956` n `83` status `ready` deltaP `5.3799` edge `0.0491` maxDD `-3.5466`
- `market_context_high->crypto_alt_1h` score `-0.8905` n `97` status `ready` deltaP `-1.747` edge `0.0134` maxDD `-4.9401`
- `market_context_high->metal_4h` score `-1.2335` n `85` status `ready` deltaP `-10.6761` edge `0.0138` maxDD `-1.0613`
- `market_context_high->equity_4h` score `-1.4688` n `85` status `ready` deltaP `-6.1191` edge `0.0016` maxDD `-5.5962`
- `market_context_high->equity_1h` score `-1.4758` n `97` status `ready` deltaP `-4.4586` edge `-0.0063` maxDD `-2.2898`
- `market_context_high->crypto_alt_4h` score `-1.6473` n `85` status `ready` deltaP `-10.434` edge `0.0678` maxDD `-10.0875`
- `market_context_high->index_1h` score `-1.7846` n `97` status `ready` deltaP `-8.9126` edge `-0.0031` maxDD `-0.5627`
- `market_context_high->fx_24h` score `-1.9906` n `83` status `ready` deltaP `-5.0745` edge `-0.0068` maxDD `-2.8323`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
