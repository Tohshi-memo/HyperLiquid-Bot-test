# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T10:37:28.322804+00:00`
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

- `market_context_high->unknown_4h` score `42.8905` n `85` status `ready` deltaP `-9.8763` edge `3.6981` maxDD `-2.3109`
- `market_context_high->unknown_24h` score `37.3472` n `59` status `ready` deltaP `-19.0001` edge `3.2753` maxDD `-1.2425`
- `market_context_high->equity_24h` score `9.223` n `59` status `ready` deltaP `35.4402` edge `0.5752` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `5.7954` n `59` status `ready` deltaP `4.6993` edge `1.0265` maxDD `-17.8526`
- `market_context_high->index_24h` score `1.379` n `59` status `ready` deltaP `22.3105` edge `0.1214` maxDD `-1.1341`
- `market_context_high->fx_4h` score `1.2724` n `85` status `ready` deltaP `18.6298` edge `0.0102` maxDD `-0.2692`
- `market_context_high->commodity_4h` score `0.2892` n `85` status `ready` deltaP `10.2655` edge `0.009` maxDD `-1.6002`
- `market_context_high->commodity_1h` score `0.2695` n `91` status `ready` deltaP `5.7989` edge `0.0089` maxDD `-0.3417`
- `market_context_high->fx_24h` score `0.0726` n `59` status `ready` deltaP `12.3647` edge `0.0168` maxDD `-0.8603`
- `market_context_high->fx_1h` score `0.0626` n `91` status `ready` deltaP `4.1012` edge `0.0021` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `-0.4507` n `91` status `ready` deltaP `0.7502` edge `0.0261` maxDD `-3.7778`
- `market_context_high->metal_4h` score `-0.5704` n `85` status `ready` deltaP `-2.4839` edge `0.0157` maxDD `-1.1153`
- `market_context_high->metal_1h` score `-0.6427` n `91` status `ready` deltaP `-3.6455` edge `0.0014` maxDD `-0.7599`
- `market_context_high->crypto_alt_1h` score `-0.9459` n `91` status `ready` deltaP `-5.1425` edge `0.0206` maxDD `-4.9401`
- `market_context_high->crypto_major_4h` score `-1.1232` n `85` status `ready` deltaP `-3.6837` edge `0.0857` maxDD `-10.7452`
- `market_context_high->index_4h` score `-1.3154` n `85` status `ready` deltaP `-11.3289` edge `0.0001` maxDD `-1.1242`
- `market_context_high->metal_24h` score `-1.4365` n `59` status `ready` deltaP `-9.9253` edge `0.0305` maxDD `-3.5466`
- `market_context_high->index_1h` score `-1.4859` n `91` status `ready` deltaP `-5.1935` edge `-0.003` maxDD `-0.5627`
- `market_context_high->equity_1h` score `-1.5728` n `91` status `ready` deltaP `-5.5372` edge `-0.0072` maxDD `-2.2898`
- `market_context_high->crypto_alt_4h` score `-2.0058` n `85` status `ready` deltaP `-8.3859` edge `0.0546` maxDD `-13.8008`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
