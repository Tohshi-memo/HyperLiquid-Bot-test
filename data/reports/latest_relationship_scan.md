# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T04:07:28.247699+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4662`

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

- `market_context_high->unknown_4h` score `323.7416` n `50` status `ready` deltaP `13.7195` edge `26.887` maxDD `0.0`
- `market_context_high->unknown_1h` score `278.0304` n `62` status `ready` deltaP `3.2645` edge `23.1836` maxDD `-0.8932`
- `market_context_high->crypto_alt_24h` score `12.7188` n `50` status `ready` deltaP `27.7262` edge `1.0454` maxDD `-11.6271`
- `news_risk_high->equity_24h` score `11.8471` n `59` status `ready` deltaP `31.0019` edge `0.7906` maxDD `-0.1353`
- `news_risk_high->crypto_major_4h` score `10.956` n `65` status `ready` deltaP `40.1736` edge `0.6655` maxDD `-0.6258`
- `market_context_high->crypto_major_24h` score `10.6108` n `50` status `ready` deltaP `33.4731` edge `0.8027` maxDD `-9.3299`
- `news_risk_high->crypto_alt_4h` score `7.4438` n `65` status `ready` deltaP `24.6646` edge `0.5903` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.0408` n `50` status `ready` deltaP `15.8659` edge `0.5513` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.553` n `50` status `ready` deltaP `14.6646` edge `0.4939` maxDD `-7.6465`
- `news_risk_high->index_24h` score `5.0074` n `59` status `ready` deltaP `34.662` edge `0.1862` maxDD `0.0`
- `news_risk_high->equity_4h` score `3.9035` n `65` status `ready` deltaP `26.9793` edge `0.2067` maxDD `-2.9013`
- `news_risk_high->index_4h` score `3.1026` n `65` status `ready` deltaP `33.743` edge `0.0598` maxDD `-0.4296`
- `market_context_high->fx_4h` score `3.0456` n `50` status `ready` deltaP `34.2134` edge `0.0392` maxDD `-0.0791`
- `news_risk_high->crypto_major_1h` score `2.9879` n `65` status `ready` deltaP `13.4592` edge `0.1948` maxDD `-1.5096`
- `news_risk_high->metal_4h` score `2.5646` n `65` status `ready` deltaP `21.9747` edge `0.1088` maxDD `-0.993`
- `market_context_high->crypto_major_1h` score `2.3829` n `62` status `ready` deltaP `11.8215` edge `0.1648` maxDD `-2.2692`
- `news_risk_high->index_1h` score `2.1082` n `65` status `ready` deltaP `25.9166` edge `0.0179` maxDD `-0.1997`
- `market_context_high->crypto_alt_1h` score `2.08` n `62` status `ready` deltaP `9.1607` edge `0.1869` maxDD `-3.6376`
- `news_risk_high->crypto_alt_1h` score `1.4875` n `65` status `ready` deltaP `4.719` edge `0.1444` maxDD `-2.4854`
- `market_context_high->fx_24h` score `1.2625` n `50` status `ready` deltaP `24.2184` edge `0.1022` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
