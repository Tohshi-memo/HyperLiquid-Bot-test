# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T06:07:28.615079+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `5944`

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

- `market_context_high->unknown_4h` score `42.8043` n `85` status `ready` deltaP `-12.9484` edge `3.7114` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.6665` n `77` status `ready` deltaP `38.6589` edge `0.5907` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `7.9645` n `77` status `ready` deltaP `15.3928` edge `1.2333` maxDD `-17.8526`
- `market_context_high->fx_4h` score `1.2272` n `85` status `ready` deltaP `18.6298` edge `0.0106` maxDD `-0.2692`
- `market_context_high->crypto_major_4h` score `0.6044` n `85` status `ready` deltaP `9.6288` edge `0.1709` maxDD `-8.9421`
- `market_context_high->fx_1h` score `0.0658` n `97` status `ready` deltaP `4.704` edge `0.0013` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `-0.0323` n `97` status `ready` deltaP `6.6671` edge `0.0403` maxDD `-3.7778`
- `market_context_high->commodity_1h` score `-0.0484` n `97` status `ready` deltaP `3.3907` edge `0.0068` maxDD `-0.3417`
- `market_context_high->commodity_4h` score `-0.0749` n `85` status `ready` deltaP `6.1693` edge `0.0026` maxDD `-1.6002`
- `market_context_high->index_24h` score `-0.2524` n `77` status `ready` deltaP `7.5037` edge `0.0954` maxDD `-1.8889`
- `market_context_high->metal_24h` score `-0.6326` n `77` status `ready` deltaP `3.1498` edge `0.0464` maxDD `-3.5466`
- `market_context_high->metal_1h` score `-0.7088` n `97` status `ready` deltaP `-4.8058` edge `0.0007` maxDD `-0.7626`
- `market_context_high->crypto_alt_1h` score `-0.87` n `97` status `ready` deltaP `-2.6282` edge `0.0219` maxDD `-4.9401`
- `market_context_high->crypto_alt_24h` score `-1.0288` n `77` status `ready` deltaP `2.1351` edge `0.4651` maxDD `-35.5652`
- `market_context_high->metal_4h` score `-1.3457` n `85` status `ready` deltaP `-12.7242` edge `0.0135` maxDD `-1.0957`
- `market_context_high->fx_24h` score `-1.5331` n `77` status `ready` deltaP `-1.6009` edge `-0.0025` maxDD `-2.337`
- `market_context_high->equity_1h` score `-1.6933` n `97` status `ready` deltaP `-7.1023` edge `-0.0068` maxDD `-2.2898`
- `market_context_high->index_1h` score `-1.7117` n `97` status `ready` deltaP `-8.0314` edge `-0.0029` maxDD `-0.5627`
- `market_context_high->index_4h` score `-2.2695` n `85` status `ready` deltaP `-14.401` edge `0.0001` maxDD `-1.1242`
- `market_context_high->equity_4h` score `-2.8999` n `85` status `ready` deltaP `-12.2633` edge `-0.0052` maxDD `-6.043`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
