# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T03:37:28.749075+00:00`
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

- `market_context_high->unknown_1h` score `318.4564` n `50` status `ready` deltaP `6.6826` edge `26.4984` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `280.5674` n `50` status `ready` deltaP `6.7073` edge `23.3359` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.0336` n `135` status `ready` deltaP `29.2477` edge `1.4121` maxDD `-1.0093`
- `market_context_high->crypto_major_4h` score `7.0163` n `50` status `ready` deltaP `19.2195` edge `0.5269` maxDD `-3.294`
- `news_risk_high->crypto_major_24h` score `6.4831` n `135` status `ready` deltaP `23.6459` edge `0.698` maxDD `-15.8971`
- `news_risk_high->equity_24h` score `6.4327` n `135` status `ready` deltaP `24.9074` edge `0.6049` maxDD `-9.4579`
- `market_context_high->crypto_alt_4h` score `4.0085` n `50` status `ready` deltaP `14.6646` edge `0.3656` maxDD `-7.6792`
- `market_context_high->crypto_major_1h` score `2.9854` n `50` status `ready` deltaP `15.3473` edge `0.1915` maxDD `-2.2692`
- `news_risk_high->metal_24h` score `2.8321` n `135` status `ready` deltaP `21.8866` edge `0.2175` maxDD `-2.192`
- `market_context_high->fx_4h` score `2.8133` n `50` status `ready` deltaP `31.7744` edge `0.0361` maxDD `-0.0791`
- `news_risk_high->index_24h` score `2.7144` n `135` status `ready` deltaP `25.8912` edge `0.1014` maxDD `-0.4916`
- `market_context_high->crypto_alt_1h` score `2.6279` n `50` status `ready` deltaP `13.1557` edge `0.1976` maxDD `-3.6387`
- `news_risk_high->equity_4h` score `1.922` n `135` status `ready` deltaP `23.6833` edge `0.1624` maxDD `-9.143`
- `market_context_high->fx_1h` score `1.392` n `50` status `ready` deltaP `19.7425` edge `0.0108` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.5532` n `135` status `ready` deltaP `6.8563` edge `0.0627` maxDD `-1.6514`
- `news_risk_high->crypto_alt_1h` score `0.5297` n `135` status `ready` deltaP `7.1557` edge `0.0875` maxDD `-4.2849`
- `news_risk_high->crypto_alt_4h` score `0.3807` n `135` status `ready` deltaP `8.3683` edge `0.2419` maxDD `-15.9436`
- `news_risk_high->index_1h` score `0.304` n `135` status `ready` deltaP `6.8718` edge `0.0083` maxDD `-0.302`
- `market_context_high->commodity_1h` score `0.0261` n `50` status `ready` deltaP `9.1976` edge `-0.0056` maxDD `-2.1892`
- `market_context_high->equity_1h` score `-0.1551` n `50` status `ready` deltaP `-1.1437` edge `0.0528` maxDD `-1.2043`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
