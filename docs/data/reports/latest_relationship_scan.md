# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T04:52:26.828943+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6730`

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

- `market_context_high->unknown_1h` score `324.6028` n `50` status `ready` deltaP `6.8323` edge `27.0096` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `280.816` n `50` status `ready` deltaP `6.8598` edge `23.3556` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.0618` n `133` status `ready` deltaP `29.2254` edge `1.4146` maxDD `-1.0093`
- `market_context_high->crypto_major_4h` score `7.0197` n `50` status `ready` deltaP `19.0671` edge `0.5282` maxDD `-3.294`
- `news_risk_high->crypto_major_24h` score `6.3865` n `133` status `ready` deltaP `23.2783` edge `0.6924` maxDD `-15.8971`
- `news_risk_high->equity_24h` score `6.3526` n `133` status `ready` deltaP `24.5509` edge `0.6006` maxDD `-9.4579`
- `market_context_high->crypto_alt_4h` score `3.9541` n `50` status `ready` deltaP `14.3598` edge `0.3631` maxDD `-7.6792`
- `market_context_high->crypto_major_1h` score `3.0142` n `50` status `ready` deltaP `15.3473` edge `0.1939` maxDD `-2.2692`
- `news_risk_high->metal_24h` score `2.9047` n `133` status `ready` deltaP `22.4193` edge `0.22` maxDD `-2.192`
- `market_context_high->fx_4h` score `2.8133` n `50` status `ready` deltaP `31.7744` edge `0.0361` maxDD `-0.0791`
- `news_risk_high->index_24h` score `2.6911` n `133` status `ready` deltaP `25.6461` edge `0.1011` maxDD `-0.4916`
- `market_context_high->crypto_alt_1h` score `2.6711` n `50` status `ready` deltaP `13.1557` edge `0.2012` maxDD `-3.6387`
- `news_risk_high->equity_4h` score `2.4121` n `133` status `ready` deltaP `24.0796` edge `0.1685` maxDD `-7.242`
- `market_context_high->fx_1h` score `1.392` n `50` status `ready` deltaP `19.7425` edge `0.0108` maxDD `-0.113`
- `news_risk_high->crypto_alt_4h` score `0.6109` n `133` status `ready` deltaP `9.0215` edge `0.2492` maxDD `-15.3413`
- `news_risk_high->equity_1h` score `0.4727` n `133` status `ready` deltaP `6.1051` edge `0.061` maxDD `-1.6514`
- `news_risk_high->crypto_alt_1h` score `0.4432` n `133` status `ready` deltaP `6.5542` edge `0.0843` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.2903` n `133` status `ready` deltaP `6.7005` edge `0.0083` maxDD `-0.302`
- `market_context_high->commodity_1h` score `0.083` n `50` status `ready` deltaP `9.7964` edge `-0.0023` maxDD `-2.1892`
- `market_context_high->equity_1h` score `-0.1699` n `50` status `ready` deltaP `-1.2934` edge `0.0519` maxDD `-1.2043`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
