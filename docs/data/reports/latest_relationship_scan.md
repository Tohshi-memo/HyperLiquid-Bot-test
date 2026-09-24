# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T22:52:28.626312+00:00`
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

- `market_context_high->unknown_1h` score `84.4555` n `47` status `ready` deltaP `9.9663` edge `6.9786` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `46.3877` n `47` status `ready` deltaP `30.4226` edge `3.7021` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `30.6928` n `47` status `ready` deltaP `24.782` edge `2.4305` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.46` n `47` status `ready` deltaP `33.2003` edge `1.9359` maxDD `-2.1786`
- `market_context_high->index_24h` score `8.0445` n `47` status `ready` deltaP `36.8462` edge `0.4377` maxDD `-0.3705`
- `news_risk_high->unknown_1h` score `7.2447` n `114` status `ready` deltaP `-3.3223` edge `0.6503` maxDD `-0.9543`
- `market_context_high->metal_24h` score `4.2573` n `47` status `ready` deltaP `35.9264` edge `0.1391` maxDD `-0.2401`
- `news_risk_high->commodity_24h` score `3.1636` n `74` status `ready` deltaP `29.5279` edge `0.1016` maxDD `-1.7857`
- `news_risk_high->crypto_alt_1h` score `2.9277` n `114` status `ready` deltaP `14.7022` edge `0.1969` maxDD `-1.7416`
- `market_context_high->index_4h` score `2.8805` n `47` status `ready` deltaP `33.1117` edge `0.0347` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.3309` n `47` status `ready` deltaP `16.6872` edge `0.1248` maxDD `-1.3444`
- `news_risk_high->crypto_major_1h` score `1.9622` n `114` status `ready` deltaP `14.6155` edge `0.122` maxDD `-2.4737`
- `news_risk_high->crypto_major_4h` score `1.7494` n `102` status `ready` deltaP `14.6461` edge `0.2613` maxDD `-13.719`
- `news_risk_high->crypto_alt_4h` score `1.6805` n `102` status `ready` deltaP `7.6757` edge `0.334` maxDD `-15.9436`
- `news_risk_high->metal_1h` score `1.4533` n `114` status `ready` deltaP `18.7835` edge `0.0244` maxDD `-0.6142`
- `news_risk_high->fx_4h` score `1.2765` n `102` status `ready` deltaP `19.9306` edge `0.0371` maxDD `-0.421`
- `market_context_high->index_1h` score `0.9739` n `47` status `ready` deltaP `14.7598` edge `0.0106` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.9498` n `47` status `ready` deltaP `11.7658` edge `0.041` maxDD `-1.5564`
- `news_risk_high->metal_24h` score `0.4627` n `74` status `ready` deltaP `20.9178` edge `0.0647` maxDD `-7.2536`
- `news_risk_high->fx_24h` score `0.4266` n `74` status `ready` deltaP `18.811` edge `0.0924` maxDD `-1.7159`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
