# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T01:37:34.235090+00:00`
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

- `market_context_high->unknown_1h` score `318.2789` n `50` status `ready` deltaP `6.5329` edge `26.4846` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `280.4606` n `50` status `ready` deltaP `6.7073` edge `23.327` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `18.653` n `135` status `ready` deltaP `28.9004` edge `1.3827` maxDD `-1.0093`
- `market_context_high->crypto_major_4h` score `6.8545` n `50` status `ready` deltaP `18.4573` edge `0.5185` maxDD `-3.294`
- `news_risk_high->crypto_major_24h` score `6.4003` n `135` status `ready` deltaP `23.6459` edge `0.6911` maxDD `-15.8971`
- `news_risk_high->equity_24h` score `6.3953` n `135` status `ready` deltaP `24.5602` edge `0.6041` maxDD `-9.4579`
- `market_context_high->crypto_alt_4h` score `3.8979` n `50` status `ready` deltaP `14.5122` edge `0.3574` maxDD `-7.6792`
- `market_context_high->crypto_major_1h` score `2.965` n `50` status `ready` deltaP `15.1976` edge `0.1908` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.8363` n `50` status `ready` deltaP `31.9268` edge `0.037` maxDD `-0.0791`
- `news_risk_high->metal_24h` score `2.7899` n `135` status `ready` deltaP `21.5393` edge `0.2163` maxDD `-2.192`
- `news_risk_high->index_24h` score `2.7613` n `135` status `ready` deltaP `26.2384` edge `0.103` maxDD `-0.4916`
- `market_context_high->crypto_alt_1h` score `2.6194` n `50` status `ready` deltaP `13.3054` edge `0.1959` maxDD `-3.6387`
- `news_risk_high->equity_4h` score `2.1324` n `135` status `ready` deltaP `24.9029` edge `0.1718` maxDD `-9.143`
- `market_context_high->fx_1h` score `1.3417` n `50` status `ready` deltaP `19.1437` edge `0.0106` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.6694` n `135` status `ready` deltaP `7.7545` edge `0.0664` maxDD `-1.6514`
- `news_risk_high->crypto_alt_1h` score `0.5213` n `135` status `ready` deltaP `7.3054` edge `0.0858` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.3843` n `135` status `ready` deltaP `7.77` edge `0.009` maxDD `-0.302`
- `news_risk_high->crypto_alt_4h` score `0.2701` n `135` status `ready` deltaP `8.2159` edge `0.2337` maxDD `-15.9436`
- `market_context_high->commodity_1h` score `0.0347` n `50` status `ready` deltaP `9.3473` edge `-0.0055` maxDD `-2.1892`
- `market_context_high->equity_1h` score `-0.0795` n `50` status `ready` deltaP `-0.2455` edge `0.0565` maxDD `-1.2043`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
