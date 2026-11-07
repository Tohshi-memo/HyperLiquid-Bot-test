# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T15:37:29.568765+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4172`

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

- `market_context_high->unknown_4h` score `143.6058` n `37` status `ready` deltaP `-8.9692` edge `12.0717` maxDD `-0.9139`
- `market_context_high->fx_4h` score `3.3886` n `37` status `ready` deltaP `36.8202` edge `0.0459` maxDD `-0.0521`
- `market_context_high->equity_1h` score `3.1538` n `37` status `ready` deltaP `9.3098` edge `0.2467` maxDD `-2.3425`
- `market_context_high->index_4h` score `2.0268` n `37` status `ready` deltaP `26.5079` edge `0.0392` maxDD `-2.4279`
- `news_risk_high->fx_24h` score `1.5959` n `52` status `ready` deltaP `8.8942` edge `0.0958` maxDD `-0.1014`
- `news_risk_high->equity_4h` score `0.749` n `52` status `ready` deltaP `5.4643` edge `0.1335` maxDD `-4.2454`
- `market_context_high->crypto_major_1h` score `0.7124` n `37` status `ready` deltaP `9.3017` edge `0.0559` maxDD `-3.0172`
- `market_context_high->fx_1h` score `0.5439` n `37` status `ready` deltaP `8.5694` edge `0.0153` maxDD `-0.1681`
- `market_context_high->crypto_alt_1h` score `0.442` n `37` status `ready` deltaP `11.0981` edge `0.0642` maxDD `-3.1881`
- `news_risk_high->index_4h` score `0.3549` n `52` status `ready` deltaP `10.8114` edge `0.0212` maxDD `-0.4888`
- `market_context_high->index_1h` score `0.2853` n `37` status `ready` deltaP `1.8005` edge `0.0388` maxDD `-0.1621`
- `market_context_high->commodity_1h` score `0.1428` n `37` status `ready` deltaP `9.4676` edge `0.0098` maxDD `-1.7019`
- `news_risk_high->index_24h` score `0.1417` n `52` status `ready` deltaP `5.9829` edge `0.1451` maxDD `-6.6786`
- `news_risk_high->fx_4h` score `0.1104` n `52` status `ready` deltaP `7.6102` edge `0.0073` maxDD `-0.1771`
- `market_context_high->commodity_4h` score `0.009` n `37` status `ready` deltaP `3.4443` edge `0.0236` maxDD `-1.633`
- `news_risk_high->index_1h` score `-0.006` n `52` status `ready` deltaP `6.2183` edge `0.0031` maxDD `-0.2931`
- `market_context_high->metal_1h` score `-0.0669` n `37` status `ready` deltaP `1.2017` edge `0.0162` maxDD `-0.6226`
- `news_risk_high->fx_1h` score `-0.264` n `52` status `ready` deltaP `0.2534` edge `0.003` maxDD `-0.0826`
- `news_risk_high->equity_1h` score `-0.3088` n `52` status `ready` deltaP `-3.9959` edge `0.042` maxDD `-1.396`
- `market_context_high->equity_4h` score `-0.8742` n `37` status `ready` deltaP `19.9654` edge `0.0828` maxDD `-24.9053`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
