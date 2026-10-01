# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T02:07:27.264941+00:00`
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

- `market_context_high->unknown_1h` score `318.3712` n `50` status `ready` deltaP `6.6826` edge `26.4913` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `280.4858` n `50` status `ready` deltaP `6.7073` edge `23.3291` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `18.8596` n `135` status `ready` deltaP `29.2477` edge `1.3976` maxDD `-1.0093`
- `market_context_high->crypto_major_4h` score `6.8931` n `50` status `ready` deltaP `18.6098` edge `0.5207` maxDD `-3.294`
- `news_risk_high->crypto_major_24h` score `6.4567` n `135` status `ready` deltaP `23.6459` edge `0.6958` maxDD `-15.8971`
- `news_risk_high->equity_24h` score `6.4399` n `135` status `ready` deltaP `24.9074` edge `0.6055` maxDD `-9.4579`
- `market_context_high->crypto_alt_4h` score `3.9387` n `50` status `ready` deltaP `14.5122` edge `0.3608` maxDD `-7.6792`
- `market_context_high->crypto_major_1h` score `3.0166` n `50` status `ready` deltaP `15.497` edge `0.1931` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.8327` n `50` status `ready` deltaP `31.9268` edge `0.0367` maxDD `-0.0791`
- `news_risk_high->metal_24h` score `2.8098` n `135` status `ready` deltaP `21.7129` edge `0.2168` maxDD `-2.192`
- `news_risk_high->index_24h` score `2.7589` n `135` status `ready` deltaP `26.2384` edge `0.1028` maxDD `-0.4916`
- `market_context_high->crypto_alt_1h` score `2.7022` n `50` status `ready` deltaP `13.6048` edge `0.2008` maxDD `-3.6387`
- `news_risk_high->equity_4h` score `2.0852` n `135` status `ready` deltaP `24.598` edge `0.1699` maxDD `-9.143`
- `market_context_high->fx_1h` score `1.3417` n `50` status `ready` deltaP `19.1437` edge `0.0106` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.6683` n `135` status `ready` deltaP `7.7545` edge `0.0663` maxDD `-1.6514`
- `news_risk_high->crypto_alt_1h` score `0.604` n `135` status `ready` deltaP `7.6048` edge `0.0907` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.3843` n `135` status `ready` deltaP `7.77` edge `0.009` maxDD `-0.302`
- `news_risk_high->crypto_alt_4h` score `0.3109` n `135` status `ready` deltaP `8.2159` edge `0.2371` maxDD `-15.9436`
- `market_context_high->commodity_1h` score `0.0386` n `50` status `ready` deltaP `9.3473` edge `-0.005` maxDD `-2.1892`
- `market_context_high->equity_1h` score `-0.0803` n `50` status `ready` deltaP `-0.2455` edge `0.0564` maxDD `-1.2043`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
