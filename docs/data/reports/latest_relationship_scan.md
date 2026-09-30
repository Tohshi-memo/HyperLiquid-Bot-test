# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T02:29:19.596238+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7026`

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

- `news_risk_high->unknown_24h` score `1395.3448` n `133` status `ready` deltaP `1.9097` edge `116.266` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.7667` n `133` status `ready` deltaP `30.7305` edge `1.5002` maxDD `-3.9611`
- `news_risk_high->crypto_major_24h` score `9.254` n `133` status `ready` deltaP `25.8824` edge `0.914` maxDD `-15.8971`
- `news_risk_high->equity_24h` score `9.1014` n `133` status `ready` deltaP `30.3963` edge `0.7907` maxDD `-9.4579`
- `news_risk_high->index_24h` score `4.1707` n `133` status `ready` deltaP `36.6999` edge `0.1507` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `3.837` n `133` status `ready` deltaP `28.4971` edge `0.2595` maxDD `-2.3787`
- `news_risk_high->equity_4h` score `2.9133` n `136` status `ready` deltaP `29.34` edge `0.2073` maxDD `-9.143`
- `news_risk_high->crypto_alt_4h` score `2.1588` n `136` status `ready` deltaP `12.2938` edge `0.3639` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `1.1194` n `136` status `ready` deltaP `9.2462` edge `0.1227` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.8571` n `136` status `ready` deltaP `8.96` edge `0.074` maxDD `-1.6514`
- `news_risk_high->index_1h` score `0.5082` n `136` status `ready` deltaP `8.9732` edge `0.0113` maxDD `-0.302`
- `news_risk_high->index_4h` score `-0.0739` n `136` status `ready` deltaP `7.5861` edge `0.0286` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.4501` n `136` status `ready` deltaP `1.5498` edge `0.0151` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.4538` n `136` status `ready` deltaP `2.8707` edge `0.0713` maxDD `-7.2607`
- `news_risk_high->metal_4h` score `-1.2556` n `136` status `ready` deltaP `-7.4875` edge `0.0303` maxDD `-2.975`
- `news_risk_high->crypto_major_4h` score `-1.3916` n `136` status `ready` deltaP `-2.9591` edge `0.1128` maxDD `-13.719`
- `news_risk_high->fx_4h` score `-1.4705` n `136` status `ready` deltaP `6.2589` edge `-0.0089` maxDD `-3.0414`
- `news_risk_high->commodity_1h` score `-1.8284` n `136` status `ready` deltaP `-8.6738` edge `-0.0091` maxDD `-3.3986`
- `news_risk_high->fx_1h` score `-1.8665` n `136` status `ready` deltaP `-9.4796` edge `-0.0043` maxDD `-1.0436`
- `news_risk_high->commodity_4h` score `-2.2477` n `136` status `ready` deltaP `-8.8504` edge `0.0127` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
