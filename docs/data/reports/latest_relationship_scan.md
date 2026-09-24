# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T23:07:33.520326+00:00`
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

- `market_context_high->unknown_1h` score `84.3727` n `47` status `ready` deltaP `9.9663` edge `6.9717` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `46.5101` n `47` status `ready` deltaP `30.4226` edge `3.7123` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `30.7528` n `47` status `ready` deltaP `24.782` edge `2.4355` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.5087` n `47` status `ready` deltaP `33.3739` edge `1.9388` maxDD `-2.1786`
- `market_context_high->index_24h` score `8.062` n `47` status `ready` deltaP `37.0198` edge `0.438` maxDD `-0.3705`
- `news_risk_high->unknown_1h` score `7.6491` n `114` status `ready` deltaP `-3.3223` edge `0.684` maxDD `-0.9543`
- `market_context_high->metal_24h` score `4.2808` n `47` status `ready` deltaP `36.1` edge `0.1399` maxDD `-0.2401`
- `news_risk_high->commodity_24h` score `3.2747` n `73` status `ready` deltaP `30.6316` edge `0.1035` maxDD `-1.7857`
- `news_risk_high->crypto_alt_1h` score `2.9073` n `114` status `ready` deltaP `14.7022` edge `0.1952` maxDD `-1.7416`
- `market_context_high->index_4h` score `2.8805` n `47` status `ready` deltaP `33.1117` edge `0.0347` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.3479` n `47` status `ready` deltaP `16.8396` edge `0.1252` maxDD `-1.3444`
- `news_risk_high->crypto_major_1h` score `1.9538` n `114` status `ready` deltaP `14.6155` edge `0.1213` maxDD `-2.4737`
- `news_risk_high->crypto_major_4h` score `1.5248` n `102` status `ready` deltaP `13.8182` edge `0.2481` maxDD `-13.719`
- `news_risk_high->crypto_alt_4h` score `1.4921` n `102` status `ready` deltaP `7.6757` edge `0.3183` maxDD `-15.9436`
- `news_risk_high->metal_1h` score `1.4522` n `114` status `ready` deltaP `18.7835` edge `0.0243` maxDD `-0.6142`
- `news_risk_high->fx_4h` score `1.1947` n `102` status `ready` deltaP `19.1027` edge `0.0358` maxDD `-0.421`
- `market_context_high->index_1h` score `0.9727` n `47` status `ready` deltaP `14.7598` edge `0.0105` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.9354` n `47` status `ready` deltaP `11.6161` edge `0.0408` maxDD `-1.5564`
- `news_risk_high->metal_24h` score `0.4054` n `73` status `ready` deltaP `20.536` edge `0.0599` maxDD `-7.2536`
- `news_risk_high->fx_24h` score `0.3751` n `73` status `ready` deltaP `18.1816` edge `0.09` maxDD `-1.7159`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
