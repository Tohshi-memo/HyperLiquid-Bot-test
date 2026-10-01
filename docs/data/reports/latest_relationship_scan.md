# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T04:37:34.155148+00:00`
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

- `market_context_high->unknown_1h` score `318.7828` n `50` status `ready` deltaP `6.8323` edge `26.5246` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `280.762` n `50` status `ready` deltaP `6.8598` edge `23.3511` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.0675` n `134` status `ready` deltaP `29.2367` edge `1.415` maxDD `-1.0093`
- `market_context_high->crypto_major_4h` score `7.0523` n `50` status `ready` deltaP `19.2195` edge `0.5299` maxDD `-3.294`
- `news_risk_high->crypto_major_24h` score `6.4349` n `134` status `ready` deltaP `23.4634` edge `0.6952` maxDD `-15.8971`
- `news_risk_high->equity_24h` score `6.3934` n `134` status `ready` deltaP `24.7305` edge `0.6028` maxDD `-9.4579`
- `market_context_high->crypto_alt_4h` score `3.9939` n `50` status `ready` deltaP `14.5122` edge `0.3654` maxDD `-7.6792`
- `market_context_high->crypto_major_1h` score `3.0142` n `50` status `ready` deltaP `15.3473` edge `0.1939` maxDD `-2.2692`
- `news_risk_high->metal_24h` score `2.8652` n `134` status `ready` deltaP `22.1496` edge `0.2185` maxDD `-2.192`
- `market_context_high->fx_4h` score `2.7987` n `50` status `ready` deltaP `31.622` edge `0.0359` maxDD `-0.0791`
- `news_risk_high->index_24h` score `2.6986` n `134` status `ready` deltaP `25.7696` edge `0.1009` maxDD `-0.4916`
- `market_context_high->crypto_alt_1h` score `2.6651` n `50` status `ready` deltaP `13.1557` edge `0.2007` maxDD `-3.6387`
- `news_risk_high->equity_4h` score `2.1077` n `134` status `ready` deltaP `23.6485` edge `0.1629` maxDD `-8.26`
- `market_context_high->fx_1h` score `1.392` n `50` status `ready` deltaP `19.7425` edge `0.0108` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.5005` n `134` status `ready` deltaP `6.4081` edge `0.0613` maxDD `-1.6514`
- `news_risk_high->crypto_alt_1h` score `0.4842` n `134` status `ready` deltaP `6.8572` edge `0.0857` maxDD `-4.2849`
- `news_risk_high->crypto_alt_4h` score `0.4388` n `134` status `ready` deltaP `8.6913` edge `0.2444` maxDD `-15.9284`
- `news_risk_high->index_1h` score `0.2649` n `134` status `ready` deltaP `6.4126` edge `0.0081` maxDD `-0.302`
- `market_context_high->commodity_1h` score `0.0822` n `50` status `ready` deltaP `9.7964` edge `-0.0024` maxDD `-2.1892`
- `market_context_high->equity_1h` score `-0.1683` n `50` status `ready` deltaP `-1.2934` edge `0.0521` maxDD `-1.2043`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
