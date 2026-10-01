# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T01:08:03.703003+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6620`

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

- `market_context_high->unknown_1h` score `317.9693` n `50` status `ready` deltaP `6.5329` edge `26.4588` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `280.1222` n `50` status `ready` deltaP `6.7073` edge `23.2988` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `18.515` n `135` status `ready` deltaP `28.9004` edge `1.3712` maxDD `-1.0093`
- `market_context_high->crypto_major_4h` score `6.8303` n `50` status `ready` deltaP `18.3049` edge `0.5175` maxDD `-3.294`
- `news_risk_high->crypto_major_24h` score `6.3931` n `135` status `ready` deltaP `23.6459` edge `0.6905` maxDD `-15.8971`
- `news_risk_high->equity_24h` score `6.3544` n `135` status `ready` deltaP `24.213` edge `0.603` maxDD `-9.4579`
- `market_context_high->crypto_alt_4h` score `3.8631` n `50` status `ready` deltaP `14.5122` edge `0.3545` maxDD `-7.6792`
- `market_context_high->crypto_major_1h` score `2.9998` n `50` status `ready` deltaP `15.497` edge `0.1917` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.8399` n `50` status `ready` deltaP `31.9268` edge `0.0373` maxDD `-0.0791`
- `news_risk_high->index_24h` score `2.7927` n `135` status `ready` deltaP `26.5856` edge `0.1033` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `2.7863` n `135` status `ready` deltaP `21.5393` edge `0.216` maxDD `-2.192`
- `market_context_high->crypto_alt_1h` score `2.611` n `50` status `ready` deltaP `13.3054` edge `0.1952` maxDD `-3.6387`
- `news_risk_high->equity_4h` score `2.1772` n `135` status `ready` deltaP `25.2077` edge `0.1735` maxDD `-9.143`
- `market_context_high->fx_1h` score `1.3429` n `50` status `ready` deltaP `19.1437` edge `0.0107` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.7042` n `135` status `ready` deltaP `8.0539` edge `0.0673` maxDD `-1.6514`
- `news_risk_high->crypto_alt_1h` score `0.5129` n `135` status `ready` deltaP `7.3054` edge `0.0851` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.4119` n `135` status `ready` deltaP `8.0694` edge `0.0093` maxDD `-0.302`
- `news_risk_high->crypto_alt_4h` score `0.2353` n `135` status `ready` deltaP `8.2159` edge `0.2308` maxDD `-15.9436`
- `market_context_high->commodity_1h` score `-0.0057` n `50` status `ready` deltaP `9.1976` edge `-0.0074` maxDD `-2.3717`
- `market_context_high->equity_1h` score `-0.0569` n `50` status `ready` deltaP `0.0539` edge `0.0574` maxDD `-1.2043`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
