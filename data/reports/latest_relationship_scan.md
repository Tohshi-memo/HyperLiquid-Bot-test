# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-14T02:22:26.529159+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11712`

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

- `market_context_high->unknown_24h` score `90.7243` n `150` status `ready` deltaP `-28.4097` edge `8.041` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.4301` n `32` status `ready` deltaP `-42.5347` edge `4.6445` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.4301` n `32` status `ready` deltaP `-42.5347` edge `4.6445` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `9.7246` n `36` status `ready` deltaP `10.0694` edge `0.7812` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `6.6976` n `36` status `ready` deltaP `35.9756` edge `0.3183` maxDD `0.0`
- `risk_on_high->commodity_24h` score `4.7421` n `32` status `ready` deltaP `32.2917` edge `0.1799` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.7421` n `32` status `ready` deltaP `32.2917` edge `0.1799` maxDD `0.0`
- `risk_on_high->commodity_4h` score `3.0027` n `32` status `ready` deltaP `21.2652` edge `0.1267` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `3.0027` n `32` status `ready` deltaP `21.2652` edge `0.1267` maxDD `-0.1258`
- `market_context_high->commodity_24h` score `2.815` n `150` status `ready` deltaP `22.2917` edge `0.1663` maxDD `-2.4263`
- `news_risk_high->index_24h` score `2.2911` n `36` status `ready` deltaP `14.5833` edge `0.0937` maxDD `0.0`
- `market_context_high->commodity_4h` score `1.6412` n `150` status `ready` deltaP `17.8069` edge `0.0819` maxDD `-2.1077`
- `news_risk_high->index_4h` score `1.5208` n `36` status `ready` deltaP `18.2418` edge `0.0183` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.5008` n `36` status `ready` deltaP `7.2356` edge `0.1087` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.3474` n `32` status `ready` deltaP `14.259` edge `0.0405` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.3474` n `32` status `ready` deltaP `14.259` edge `0.0405` maxDD `-0.1957`
- `risk_on_high->fx_24h` score `1.3058` n `32` status `ready` deltaP `15.2778` edge `0.0254` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.3058` n `32` status `ready` deltaP `15.2778` edge `0.0254` maxDD `-0.1418`
- `risk_on_high->fx_4h` score `1.017` n `32` status `ready` deltaP `11.814` edge `0.0201` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `1.017` n `32` status `ready` deltaP `11.814` edge `0.0201` maxDD `-0.1285`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
