# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T16:52:28.578644+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3744`

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

- `market_context_high->unknown_1h` score `32183.8309` n `45` status `ready` deltaP `2.1656` edge `2681.9809` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21874.2525` n `45` status `ready` deltaP `2.8727` edge `1822.8491` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `948.8759` n `31` status `ready` deltaP `2.3807` edge `79.0747` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `621.305` n `31` status `ready` deltaP `4.0913` edge `51.7538` maxDD `-0.1191`
- `news_risk_high->unknown_24h` score `385.8623` n `31` status `ready` deltaP `5.7292` edge `32.117` maxDD `0.0`
- `news_risk_high->equity_24h` score `46.1715` n `31` status `ready` deltaP `52.0833` edge `3.5004` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `42.4061` n `31` status `ready` deltaP `53.6458` edge `3.1762` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `38.8037` n `31` status `ready` deltaP `56.0764` edge `2.8598` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `12.0598` n `31` status `ready` deltaP `27.8275` edge `0.9065` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `12.0302` n `31` status `ready` deltaP `41.2355` edge `0.7551` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `11.6382` n `31` status `ready` deltaP `38.5966` edge `0.7606` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.5448` n `31` status `ready` deltaP `19.2171` edge `0.9809` maxDD `-7.6714`
- `news_risk_high->index_24h` score `7.3974` n `31` status `ready` deltaP `52.7778` edge `0.2646` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.4434` n `31` status `ready` deltaP `46.7462` edge `0.1548` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `4.1117` n `31` status `ready` deltaP `20.8856` edge `0.2221` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.53` n `31` status `ready` deltaP `37.3771` edge `0.071` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7549` n `31` status `ready` deltaP `32.2919` edge `0.0228` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.6964` n `31` status `ready` deltaP `11.5076` edge `0.3151` maxDD `-1.6897`
- `market_context_high->fx_4h` score `2.4688` n `45` status `ready` deltaP `30.2405` edge `0.0326` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.4662` n `31` status `ready` deltaP `13.4537` edge `0.2622` maxDD `-1.5232`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
