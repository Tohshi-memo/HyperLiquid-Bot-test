# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T15:52:19.614830+00:00`
- Price records: `659`
- Market context records: `770`
- Flow alert records: `2171`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1170`

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

- `market_context_high->crypto_major_24h` score `13.4376` n `147` status `ready` deltaP `32.0091` edge `0.9398` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.6474` n `147` status `ready` deltaP `7.3126` edge `0.51` maxDD `-0.0508`
- `risk_on_high->equity_4h` score `3.0934` n `30` status `ready` deltaP `9.0611` edge `0.2339` maxDD `-0.9217`
- `risk_on_and_context->equity_4h` score `3.0934` n `30` status `ready` deltaP `9.0611` edge `0.2339` maxDD `-0.9217`
- `risk_on_high->index_4h` score `2.7861` n `30` status `ready` deltaP `18.3881` edge `0.1184` maxDD `-0.038`
- `risk_on_and_context->index_4h` score `2.7861` n `30` status `ready` deltaP `18.3881` edge `0.1184` maxDD `-0.038`
- `risk_on_high->crypto_major_4h` score `2.6752` n `30` status `ready` deltaP `19.8341` edge `0.1279` maxDD `-0.9758`
- `risk_on_and_context->crypto_major_4h` score `2.6752` n `30` status `ready` deltaP `19.8341` edge `0.1279` maxDD `-0.9758`
- `risk_on_high->crypto_alt_4h` score `2.2963` n `30` status `ready` deltaP `21.2597` edge `0.0701` maxDD `-0.6377`
- `risk_on_and_context->crypto_alt_4h` score `2.2963` n `30` status `ready` deltaP `21.2597` edge `0.0701` maxDD `-0.6377`
- `risk_on_high->metal_1h` score `1.0818` n `33` status `ready` deltaP `13.2085` edge `0.0251` maxDD `-0.5074`
- `risk_on_and_context->metal_1h` score `1.0818` n `33` status `ready` deltaP `13.2085` edge `0.0251` maxDD `-0.5074`
- `market_context_high->index_24h` score `0.5648` n `147` status `ready` deltaP `3.0569` edge `0.2262` maxDD `-5.9609`
- `risk_on_high->commodity_4h` score `0.2921` n `30` status `ready` deltaP `1.7058` edge `0.1092` maxDD `-1.3162`
- `risk_on_and_context->commodity_4h` score `0.2921` n `30` status `ready` deltaP `1.7058` edge `0.1092` maxDD `-1.3162`
- `risk_on_high->fx_1h` score `0.2912` n `33` status `ready` deltaP `8.7977` edge `0.0022` maxDD `-0.2147`
- `risk_on_and_context->fx_1h` score `0.2912` n `33` status `ready` deltaP `8.7977` edge `0.0022` maxDD `-0.2147`
- `risk_on_high->commodity_1h` score `0.2496` n `33` status `ready` deltaP `7.6945` edge `0.0183` maxDD `-0.6739`
- `risk_on_and_context->commodity_1h` score `0.2496` n `33` status `ready` deltaP `7.6945` edge `0.0183` maxDD `-0.6739`
- `market_context_high->equity_24h` score `-0.0278` n `147` status `ready` deltaP `1.6283` edge `0.2473` maxDD `-10.5047`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
