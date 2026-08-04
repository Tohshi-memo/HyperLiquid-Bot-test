# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T06:22:31.371795+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9833`

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

- `market_context_high->unknown_24h` score `37.4319` n `46` status `ready` deltaP `26.2983` edge `2.9483` maxDD `-0.0103`
- `market_context_high->crypto_alt_24h` score `9.1428` n `46` status `ready` deltaP `44.6936` edge `0.4813` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `8.084` n `46` status `ready` deltaP `37.3943` edge `0.4423` maxDD `-0.434`
- `market_context_high->unknown_4h` score `5.8393` n `88` status `ready` deltaP `2.2727` edge `0.571` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.1664` n `88` status `ready` deltaP `15.0638` edge `0.0814` maxDD `-2.7703`
- `market_context_high->fx_4h` score `0.3651` n `88` status `ready` deltaP `18.3897` edge `0.0102` maxDD `-1.8797`
- `market_context_high->commodity_1h` score `0.2541` n `88` status `ready` deltaP `5.8315` edge `0.0239` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.2083` n `88` status `ready` deltaP `8.2812` edge `-0.003` maxDD `-0.7878`
- `market_context_high->index_1h` score `-0.4499` n `88` status `ready` deltaP `1.8781` edge `-0.0168` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.4755` n `88` status `ready` deltaP `5.8066` edge `0.0238` maxDD `-3.211`
- `market_context_high->metal_1h` score `-0.5276` n `88` status `ready` deltaP `-1.4698` edge `-0.0084` maxDD `-1.6224`
- `market_context_high->crypto_alt_4h` score `-0.9709` n `88` status `ready` deltaP `3.2567` edge `-0.0072` maxDD `-5.7857`
- `market_context_high->crypto_alt_1h` score `-1.2623` n `88` status `ready` deltaP `-3.4703` edge `-0.011` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.5229` n `88` status `ready` deltaP `5.9132` edge `-0.0811` maxDD `-10.619`
- `market_context_high->fx_24h` score `-1.6819` n `46` status `ready` deltaP `-4.227` edge `0.0086` maxDD `-4.3126`
- `market_context_high->index_4h` score `-1.7757` n `88` status `ready` deltaP `-8.8969` edge `-0.0429` maxDD `-4.7021`
- `market_context_high->unknown_1h` score `-3.3476` n `88` status `ready` deltaP `2.8988` edge `-0.2536` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.6032` n `88` status `ready` deltaP `-12.6497` edge `-0.0786` maxDD `-7.6533`
- `market_context_high->metal_24h` score `-4.8511` n `46` status `ready` deltaP `-23.9885` edge `-0.1275` maxDD `-2.6802`
- `market_context_high->equity_4h` score `-6.4438` n `88` status `ready` deltaP `1.5521` edge `-0.3034` maxDD `-35.3129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
