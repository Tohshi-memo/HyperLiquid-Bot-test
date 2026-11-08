# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T04:07:30.907360+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4428`

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

- `market_context_high->unknown_4h` score `121.1223` n `37` status `ready` deltaP `-6.3777` edge `10.1808` maxDD `-0.9139`
- `market_context_high->fx_4h` score `3.3496` n `37` status `ready` deltaP `36.3629` edge `0.0457` maxDD `-0.0521`
- `market_context_high->equity_1h` score `3.2341` n `37` status `ready` deltaP `10.208` edge `0.2474` maxDD `-2.3425`
- `market_context_high->index_4h` score `1.9025` n `37` status `ready` deltaP `24.9835` edge `0.039` maxDD `-2.4279`
- `news_risk_high->fx_24h` score `1.7696` n `52` status `ready` deltaP `10.6303` edge `0.0987` maxDD `-0.1014`
- `news_risk_high->equity_4h` score `0.9185` n `52` status `ready` deltaP `7.5985` edge `0.141` maxDD `-4.2454`
- `market_context_high->crypto_major_1h` score `0.7495` n `37` status `ready` deltaP `9.4514` edge `0.058` maxDD `-3.0172`
- `market_context_high->crypto_alt_1h` score `0.4592` n `37` status `ready` deltaP `10.9484` edge `0.0674` maxDD `-3.1881`
- `market_context_high->fx_1h` score `0.4589` n `37` status `ready` deltaP `7.5215` edge `0.0152` maxDD `-0.1681`
- `news_risk_high->index_4h` score `0.2741` n `52` status `ready` deltaP `9.287` edge `0.021` maxDD `-0.4888`
- `market_context_high->index_1h` score `0.2482` n `37` status `ready` deltaP `1.3514` edge `0.0387` maxDD `-0.1621`
- `news_risk_high->index_24h` score `0.2383` n `52` status `ready` deltaP `6.851` edge `0.1517` maxDD `-6.6786`
- `market_context_high->commodity_1h` score `0.1452` n `37` status `ready` deltaP `9.4676` edge `0.0101` maxDD `-1.7019`
- `market_context_high->commodity_4h` score `0.0897` n `37` status `ready` deltaP `4.8163` edge `0.0248` maxDD `-1.633`
- `news_risk_high->fx_4h` score `0.0851` n `52` status `ready` deltaP `7.1529` edge `0.0071` maxDD `-0.1771`
- `market_context_high->metal_1h` score `-0.01` n `37` status `ready` deltaP `2.2496` edge `0.0165` maxDD `-0.6226`
- `news_risk_high->index_1h` score `-0.0302` n `52` status `ready` deltaP `5.7692` edge `0.003` maxDD `-0.2931`
- `news_risk_high->equity_1h` score `-0.2566` n `52` status `ready` deltaP `-3.0977` edge `0.0427` maxDD `-1.396`
- `news_risk_high->fx_1h` score `-0.3192` n `52` status `ready` deltaP `-0.7945` edge `0.0029` maxDD `-0.0826`
- `market_context_high->equity_4h` score `-0.7047` n `37` status `ready` deltaP `22.0996` edge `0.0903` maxDD `-24.9053`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
