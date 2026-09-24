# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T23:52:31.759471+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `10145`

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

- `market_context_high->unknown_1h` score `83.9659` n `47` status `ready` deltaP `9.6669` edge `6.9398` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `46.8521` n `47` status `ready` deltaP `30.4226` edge `3.7408` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `30.922` n `47` status `ready` deltaP `24.782` edge `2.4496` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.6524` n `47` status `ready` deltaP `33.8948` edge `1.9473` maxDD `-2.1786`
- `news_risk_high->unknown_1h` score `9.6219` n `114` status `ready` deltaP `-1.8673` edge `0.8387` maxDD `-0.9543`
- `market_context_high->index_24h` score `8.1145` n `47` status `ready` deltaP `37.5406` edge `0.4389` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.3501` n `47` status `ready` deltaP `36.6209` edge `0.1422` maxDD `-0.2401`
- `news_risk_high->commodity_24h` score `3.4019` n `70` status `ready` deltaP `31.6518` edge `0.1073` maxDD `-1.7857`
- `news_risk_high->crypto_alt_1h` score `3.0087` n `114` status `ready` deltaP `15.4297` edge `0.1988` maxDD `-1.7416`
- `market_context_high->index_4h` score `2.9195` n `47` status `ready` deltaP `33.569` edge `0.0349` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.3975` n `47` status `ready` deltaP `17.1445` edge `0.1273` maxDD `-1.3444`
- `news_risk_high->crypto_major_1h` score `2.0876` n `114` status `ready` deltaP `15.343` edge `0.1276` maxDD `-2.4737`
- `news_risk_high->metal_1h` score `1.3748` n `114` status `ready` deltaP `18.056` edge `0.0227` maxDD `-0.6142`
- `news_risk_high->fx_4h` score `1.0058` n `102` status `ready` deltaP `17.4468` edge `0.0311` maxDD `-0.421`
- `market_context_high->index_1h` score `0.9583` n `47` status `ready` deltaP `14.6101` edge `0.0103` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.9055` n `47` status `ready` deltaP `11.3167` edge `0.0403` maxDD `-1.5564`
- `news_risk_high->crypto_major_4h` score `0.6709` n `102` status `ready` deltaP `11.3343` edge `0.1935` maxDD `-13.719`
- `news_risk_high->crypto_alt_4h` score `0.4606` n `102` status `ready` deltaP `5.1919` edge `0.2489` maxDD `-15.9436`
- `news_risk_high->metal_24h` score `0.2325` n `70` status `ready` deltaP `19.2957` edge `0.046` maxDD `-7.2536`
- `news_risk_high->fx_24h` score `0.2066` n `70` status `ready` deltaP `16.1855` edge `0.0817` maxDD `-1.7159`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
