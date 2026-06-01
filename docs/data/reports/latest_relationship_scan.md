# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T19:52:17.611920+00:00`
- Price records: `672`
- Market context records: `2592`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9200`

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

- `market_context_high->unknown_24h` score `7.7013` n `132` status `ready` deltaP `18.1345` edge `0.5537` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `5.7127` n `146` status `ready` deltaP `25.9585` edge `0.5709` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.9856` n `146` status `ready` deltaP `16.7453` edge `0.4015` maxDD `-10.1468`
- `market_context_high->crypto_alt_24h` score `1.7794` n `132` status `ready` deltaP `3.3618` edge `0.7637` maxDD `-39.0265`
- `market_context_high->crypto_alt_1h` score `1.4515` n `146` status `ready` deltaP `11.8797` edge `0.1605` maxDD `-6.1656`
- `market_context_high->unknown_4h` score `0.9793` n `146` status `ready` deltaP `8.1419` edge `0.1323` maxDD `-3.7312`
- `market_context_high->index_24h` score `0.9111` n `132` status `ready` deltaP `8.7752` edge `0.1155` maxDD `-2.5127`
- `market_context_high->crypto_major_1h` score `0.8408` n `146` status `ready` deltaP `9.4619` edge `0.1264` maxDD `-4.2199`
- `market_context_high->index_4h` score `0.251` n `146` status `ready` deltaP `9.28` edge `0.0432` maxDD `-2.3986`
- `market_context_high->equity_24h` score `0.2312` n `132` status `ready` deltaP `16.8876` edge `-0.0263` maxDD `-2.3615`
- `market_context_high->index_1h` score `-0.1503` n `146` status `ready` deltaP `3.9414` edge `0.0106` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.3732` n `146` status `ready` deltaP `2.0999` edge `0.0212` maxDD `-2.6375`
- `market_context_high->commodity_1h` score `-0.4482` n `146` status `ready` deltaP `5.2026` edge `0.0158` maxDD `-4.3601`
- `market_context_high->metal_4h` score `-0.6146` n `146` status `ready` deltaP `4.6546` edge `0.0565` maxDD `-4.7664`
- `market_context_high->metal_1h` score `-0.6296` n `146` status `ready` deltaP `1.1115` edge `0.0149` maxDD `-2.9823`
- `market_context_high->fx_1h` score `-0.6772` n `146` status `ready` deltaP `-0.9843` edge `0.0036` maxDD `-0.278`
- `market_context_high->crypto_major_24h` score `-0.7103` n `132` status `ready` deltaP `5.2557` edge `0.4281` maxDD `-30.1198`
- `market_context_high->equity_1h` score `-0.8277` n `146` status `ready` deltaP `-0.3773` edge `0.0174` maxDD `-2.7085`
- `market_context_high->fx_4h` score `-0.9144` n `146` status `ready` deltaP `-0.378` edge `0.0121` maxDD `-0.8621`
- `market_context_high->fx_24h` score `-0.9614` n `132` status `ready` deltaP `2.8567` edge `0.0002` maxDD `-1.6157`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
