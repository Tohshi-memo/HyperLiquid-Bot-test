# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T10:07:27.286004+00:00`
- Price records: `672`
- Market context records: `6487`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5869`

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

- `news_risk_high->crypto_alt_24h` score `12.6823` n `32` status `ready` deltaP `34.2014` edge `0.8436` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.4854` n `32` status `ready` deltaP `53.9931` edge `0.1805` maxDD `0.0`
- `market_context_high->unknown_24h` score `6.3674` n `159` status `ready` deltaP `15.5169` edge `0.7572` maxDD `-15.0689`
- `news_risk_high->crypto_major_24h` score `4.4549` n `32` status `ready` deltaP `17.5347` edge `0.5322` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `3.9654` n `38` status `ready` deltaP `42.2176` edge `0.0536` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `2.9798` n `32` status `ready` deltaP `28.2986` edge `0.0802` maxDD `-0.3101`
- `market_context_high->unknown_1h` score `2.8878` n `180` status `ready` deltaP `-3.8922` edge `0.3567` maxDD `-3.2083`
- `news_risk_high->fx_1h` score `1.855` n `38` status `ready` deltaP `23.2115` edge `0.0179` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `0.5894` n `38` status `ready` deltaP `5.2001` edge `0.0946` maxDD `-2.6299`
- `market_context_high->index_4h` score `0.5846` n `168` status `ready` deltaP `13.1025` edge `0.029` maxDD `-0.4108`
- `market_context_high->commodity_24h` score `0.4826` n `159` status `ready` deltaP `7.4456` edge `0.1774` maxDD `-5.2791`
- `market_context_high->crypto_alt_4h` score `0.3905` n `168` status `ready` deltaP `9.4367` edge `0.125` maxDD `-6.7632`
- `market_context_high->unknown_4h` score `0.3341` n `168` status `ready` deltaP `-15.6432` edge `0.3727` maxDD `-10.5788`
- `market_context_high->metal_4h` score `0.1717` n `168` status `ready` deltaP `11.8394` edge `0.0442` maxDD `-2.7056`
- `news_risk_high->crypto_alt_1h` score `0.0921` n `38` status `ready` deltaP `1.7334` edge `0.0512` maxDD `-2.0756`
- `market_context_high->equity_4h` score `-0.4509` n `168` status `ready` deltaP `8.4857` edge `0.0555` maxDD `-8.2573`
- `news_risk_high->index_24h` score `-0.4517` n `32` status `ready` deltaP `4.6875` edge `-0.002` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.553` n `180` status `ready` deltaP `0.835` edge `0.0013` maxDD `-1.8877`
- `market_context_high->crypto_alt_1h` score `-0.5634` n `180` status `ready` deltaP `6.324` edge `0.0169` maxDD `-5.8368`
- `market_context_high->index_1h` score `-0.5793` n `180` status `ready` deltaP `-0.9614` edge `0.0041` maxDD `-0.7564`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
