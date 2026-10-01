# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T04:22:29.104503+00:00`
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

- `market_context_high->unknown_1h` score `318.6556` n `50` status `ready` deltaP `6.6826` edge `26.515` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `280.6684` n `50` status `ready` deltaP `6.8598` edge `23.3433` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.0888` n `135` status `ready` deltaP `29.2477` edge `1.4167` maxDD `-1.0093`
- `market_context_high->crypto_major_4h` score `7.0559` n `50` status `ready` deltaP `19.2195` edge `0.5302` maxDD `-3.294`
- `news_risk_high->crypto_major_24h` score `6.4819` n `135` status `ready` deltaP `23.6459` edge `0.6979` maxDD `-15.8971`
- `news_risk_high->equity_24h` score `6.4291` n `135` status `ready` deltaP `24.9074` edge `0.6046` maxDD `-9.4579`
- `market_context_high->crypto_alt_4h` score `4.0205` n `50` status `ready` deltaP `14.6646` edge `0.3666` maxDD `-7.6792`
- `market_context_high->crypto_major_1h` score `3.0058` n `50` status `ready` deltaP `15.3473` edge `0.1932` maxDD `-2.2692`
- `news_risk_high->metal_24h` score `2.8098` n `135` status `ready` deltaP `21.7129` edge `0.2168` maxDD `-2.192`
- `market_context_high->fx_4h` score `2.7853` n `50` status `ready` deltaP `31.4695` edge `0.0358` maxDD `-0.0791`
- `news_risk_high->index_24h` score `2.7048` n `135` status `ready` deltaP `25.8912` edge `0.1006` maxDD `-0.4916`
- `market_context_high->crypto_alt_1h` score `2.6519` n `50` status `ready` deltaP `13.1557` edge `0.1996` maxDD `-3.6387`
- `news_risk_high->equity_4h` score `1.8338` n `135` status `ready` deltaP `23.226` edge `0.1581` maxDD `-9.143`
- `market_context_high->fx_1h` score `1.392` n `50` status `ready` deltaP `19.7425` edge `0.0108` maxDD `-0.113`
- `news_risk_high->crypto_alt_1h` score `0.5537` n `135` status `ready` deltaP `7.1557` edge `0.0895` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.5352` n `135` status `ready` deltaP `6.7066` edge `0.0622` maxDD `-1.6514`
- `news_risk_high->crypto_alt_4h` score `0.3927` n `135` status `ready` deltaP `8.3683` edge `0.2429` maxDD `-15.9436`
- `news_risk_high->index_1h` score `0.2909` n `135` status `ready` deltaP `6.7221` edge `0.0082` maxDD `-0.302`
- `market_context_high->commodity_1h` score `0.0706` n `50` status `ready` deltaP `9.6467` edge `-0.0029` maxDD `-2.1892`
- `market_context_high->equity_1h` score `-0.1667` n `50` status `ready` deltaP `-1.2934` edge `0.0523` maxDD `-1.2043`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
