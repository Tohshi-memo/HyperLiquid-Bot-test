# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T07:07:28.150531+00:00`
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

- `market_context_high->unknown_24h` score `37.3957` n `46` status `ready` deltaP `25.9511` edge `2.9476` maxDD `-0.0103`
- `market_context_high->crypto_alt_24h` score `8.9475` n `46` status `ready` deltaP `44.1727` edge `0.4685` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `8.016` n `46` status `ready` deltaP `36.8735` edge `0.4401` maxDD `-0.434`
- `market_context_high->unknown_4h` score `5.8405` n `88` status `ready` deltaP `2.2727` edge `0.5711` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.1652` n `88` status `ready` deltaP `15.0638` edge `0.0813` maxDD `-2.7703`
- `market_context_high->fx_4h` score `0.3374` n `88` status `ready` deltaP `17.9324` edge `0.0097` maxDD `-1.8797`
- `market_context_high->commodity_1h` score `0.2673` n `88` status `ready` deltaP `5.9812` edge `0.024` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.182` n `88` status `ready` deltaP `7.9818` edge `-0.0032` maxDD `-0.7878`
- `market_context_high->index_1h` score `-0.4569` n `88` status `ready` deltaP `1.7284` edge `-0.0167` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.5094` n `88` status `ready` deltaP `5.3493` edge `0.0225` maxDD `-3.211`
- `market_context_high->metal_1h` score `-0.5105` n `88` status `ready` deltaP `-1.1704` edge `-0.0082` maxDD `-1.6224`
- `market_context_high->crypto_alt_4h` score `-0.9623` n `88` status `ready` deltaP `3.2567` edge `-0.0061` maxDD `-5.7857`
- `market_context_high->crypto_alt_1h` score `-1.2443` n `88` status `ready` deltaP `-3.3206` edge `-0.0105` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.5315` n `88` status `ready` deltaP `5.7635` edge `-0.0812` maxDD `-10.619`
- `market_context_high->fx_24h` score `-1.7343` n `46` status `ready` deltaP `-4.7479` edge `0.0077` maxDD `-4.3126`
- `market_context_high->index_4h` score `-1.805` n `88` status `ready` deltaP `-9.3542` edge `-0.0436` maxDD `-4.7021`
- `market_context_high->unknown_1h` score `-3.3225` n `88` status `ready` deltaP `3.1982` edge `-0.2535` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.584` n `88` status `ready` deltaP `-12.5` edge `-0.078` maxDD `-7.6533`
- `market_context_high->metal_24h` score `-4.8535` n `46` status `ready` deltaP `-23.9885` edge `-0.1277` maxDD `-2.6802`
- `market_context_high->equity_4h` score `-6.4948` n `88` status `ready` deltaP `1.2472` edge `-0.3079` maxDD `-35.3129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
