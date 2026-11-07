# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T19:52:26.047095+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4367`

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

- `market_context_high->unknown_4h` score `120.2376` n `37` status `ready` deltaP `-8.5118` edge `10.1213` maxDD `-0.9139`
- `market_context_high->fx_4h` score `3.4544` n `37` status `ready` deltaP `37.5824` edge `0.0463` maxDD `-0.0521`
- `market_context_high->equity_1h` score `3.1526` n `37` status `ready` deltaP `9.3098` edge `0.2466` maxDD `-2.3425`
- `market_context_high->index_4h` score `1.8855` n `37` status `ready` deltaP `24.8311` edge `0.0386` maxDD `-2.4279`
- `news_risk_high->fx_24h` score `1.64` n `52` status `ready` deltaP `9.415` edge `0.096` maxDD `-0.1014`
- `news_risk_high->equity_4h` score `0.817` n `52` status `ready` deltaP `6.5314` edge `0.1351` maxDD `-4.2454`
- `market_context_high->crypto_major_1h` score `0.7376` n `37` status `ready` deltaP `9.3017` edge `0.058` maxDD `-3.0172`
- `market_context_high->fx_1h` score `0.52` n `37` status `ready` deltaP `8.27` edge `0.0153` maxDD `-0.1681`
- `market_context_high->crypto_alt_1h` score `0.4163` n `37` status `ready` deltaP `10.649` edge `0.0639` maxDD `-3.1881`
- `news_risk_high->index_4h` score `0.263` n `52` status `ready` deltaP `9.1346` edge `0.0206` maxDD `-0.4888`
- `market_context_high->index_1h` score `0.2482` n `37` status `ready` deltaP `1.3514` edge `0.0387` maxDD `-0.1621`
- `news_risk_high->index_24h` score `0.1993` n `52` status `ready` deltaP `6.851` edge `0.1467` maxDD `-6.6786`
- `news_risk_high->fx_4h` score `0.1532` n `52` status `ready` deltaP `8.3724` edge `0.0077` maxDD `-0.1771`
- `market_context_high->commodity_1h` score `0.1163` n `37` status `ready` deltaP `9.0185` edge `0.0094` maxDD `-1.7019`
- `market_context_high->commodity_4h` score `-0.0218` n `37` status `ready` deltaP `2.987` edge `0.0227` maxDD `-1.633`
- `news_risk_high->index_1h` score `-0.0302` n `52` status `ready` deltaP `5.7692` edge `0.003` maxDD `-0.2931`
- `market_context_high->metal_1h` score `-0.0583` n `37` status `ready` deltaP `1.3514` edge `0.0163` maxDD `-0.6226`
- `news_risk_high->fx_1h` score `-0.2795` n `52` status `ready` deltaP `-0.046` edge `0.003` maxDD `-0.0826`
- `news_risk_high->equity_1h` score `-0.3096` n `52` status `ready` deltaP `-3.9959` edge `0.0419` maxDD `-1.396`
- `market_context_high->equity_4h` score `-0.8063` n `37` status `ready` deltaP `21.0325` edge `0.0844` maxDD `-24.9053`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
