# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T14:52:24.833991+00:00`
- Price records: `672`
- Market context records: `5673`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8686`

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

- `market_context_high->equity_24h` score `2.1215` n `197` status `ready` deltaP `16.4084` edge `0.5753` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `0.9727` n `247` status `ready` deltaP `11.7335` edge `0.2256` maxDD `-13.4882`
- `market_context_high->crypto_alt_4h` score `0.4871` n `247` status `ready` deltaP `8.7896` edge `0.163` maxDD `-9.1473`
- `market_context_high->equity_4h` score `0.2871` n `247` status `ready` deltaP `6.208` edge `0.1464` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2602` n `259` status `ready` deltaP `1.9739` edge `0.0011` maxDD `-0.4764`
- `market_context_high->equity_1h` score `-0.4714` n `259` status `ready` deltaP `4.6061` edge `0.0307` maxDD `-5.0555`
- `market_context_high->crypto_alt_1h` score `-0.5153` n `259` status `ready` deltaP `2.2814` edge `0.038` maxDD `-5.0257`
- `market_context_high->fx_24h` score `-0.5666` n `197` status `ready` deltaP `15.8956` edge `0.0499` maxDD `-2.9135`
- `market_context_high->index_1h` score `-0.5726` n `259` status `ready` deltaP `1.2491` edge `0.0051` maxDD `-0.9472`
- `market_context_high->crypto_major_1h` score `-0.6735` n `259` status `ready` deltaP `4.0541` edge `0.0414` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.7807` n `259` status `ready` deltaP `0.4295` edge `-0.0004` maxDD `-2.0682`
- `market_context_high->commodity_1h` score `-0.9075` n `259` status `ready` deltaP `0.6184` edge `-0.0032` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.204` n `247` status `ready` deltaP `3.3413` edge `0.0068` maxDD `-1.3415`
- `market_context_high->index_4h` score `-1.2647` n `247` status `ready` deltaP `-0.5221` edge `0.0085` maxDD `-3.04`
- `market_context_high->index_24h` score `-2.4931` n `197` status `ready` deltaP `6.5206` edge `0.0358` maxDD `-16.9124`
- `market_context_high->metal_4h` score `-2.915` n `247` status `ready` deltaP `-12.3531` edge `-0.0538` maxDD `-11.6719`
- `market_context_high->commodity_4h` score `-3.7302` n `247` status `ready` deltaP `-1.7398` edge `-0.0317` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.5738` n `197` status `ready` deltaP `4.2671` edge `0.0361` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-8.3281` n `197` status `ready` deltaP `-12.5159` edge `-0.2497` maxDD `-32.7652`
- `market_context_high->commodity_24h` score `-12.3556` n `197` status `ready` deltaP `-12.1704` edge `-0.0876` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
