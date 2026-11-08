# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T04:22:23.340716+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4440`

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

- `market_context_high->unknown_4h` score `121.1585` n `37` status `ready` deltaP `-6.2253` edge `10.1828` maxDD `-0.9139`
- `market_context_high->fx_4h` score `3.3374` n `37` status `ready` deltaP `36.2105` edge `0.0457` maxDD `-0.0521`
- `market_context_high->equity_1h` score `3.2484` n `37` status `ready` deltaP `10.3577` edge `0.2476` maxDD `-2.3425`
- `market_context_high->index_4h` score `1.9147` n `37` status `ready` deltaP `25.136` edge `0.039` maxDD `-2.4279`
- `news_risk_high->fx_24h` score `1.7744` n `52` status `ready` deltaP `10.6303` edge `0.0991` maxDD `-0.1014`
- `news_risk_high->equity_4h` score `0.9295` n `52` status `ready` deltaP `7.7509` edge `0.1414` maxDD `-4.2454`
- `market_context_high->crypto_major_1h` score `0.7495` n `37` status `ready` deltaP `9.4514` edge `0.058` maxDD `-3.0172`
- `market_context_high->crypto_alt_1h` score `0.4693` n `37` status `ready` deltaP `11.0981` edge `0.0677` maxDD `-3.1881`
- `market_context_high->fx_1h` score `0.4589` n `37` status `ready` deltaP `7.5215` edge `0.0152` maxDD `-0.1681`
- `news_risk_high->index_4h` score `0.282` n `52` status `ready` deltaP `9.4395` edge `0.021` maxDD `-0.4888`
- `market_context_high->index_1h` score `0.2602` n `37` status `ready` deltaP `1.5011` edge `0.0387` maxDD `-0.1621`
- `news_risk_high->index_24h` score `0.2422` n `52` status `ready` deltaP `6.851` edge `0.1522` maxDD `-6.6786`
- `market_context_high->commodity_1h` score `0.1452` n `37` status `ready` deltaP `9.4676` edge `0.0101` maxDD `-1.7019`
- `market_context_high->commodity_4h` score `0.081` n `37` status `ready` deltaP `4.6639` edge `0.0247` maxDD `-1.633`
- `news_risk_high->fx_4h` score `0.0771` n `52` status `ready` deltaP `7.0005` edge `0.0071` maxDD `-0.1771`
- `market_context_high->metal_1h` score `-0.0022` n `37` status `ready` deltaP `2.3993` edge `0.0165` maxDD `-0.6226`
- `news_risk_high->index_1h` score `-0.0224` n `52` status `ready` deltaP `5.9189` edge `0.003` maxDD `-0.2931`
- `news_risk_high->equity_1h` score `-0.2473` n `52` status `ready` deltaP `-2.948` edge `0.0429` maxDD `-1.396`
- `news_risk_high->fx_1h` score `-0.3192` n `52` status `ready` deltaP `-0.7945` edge `0.0029` maxDD `-0.0826`
- `market_context_high->equity_4h` score `-0.6937` n `37` status `ready` deltaP `22.252` edge `0.0907` maxDD `-24.9053`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
