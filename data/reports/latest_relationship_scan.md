# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T02:22:32.442079+00:00`
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

- `market_context_high->unknown_1h` score `318.3952` n `50` status `ready` deltaP `6.6826` edge `26.4933` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `280.487` n `50` status `ready` deltaP `6.7073` edge `23.3292` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `18.9232` n `135` status `ready` deltaP `29.2477` edge `1.4029` maxDD `-1.0093`
- `market_context_high->crypto_major_4h` score `6.9185` n `50` status `ready` deltaP `18.7622` edge `0.5218` maxDD `-3.294`
- `news_risk_high->crypto_major_24h` score `6.4795` n `135` status `ready` deltaP `23.6459` edge `0.6977` maxDD `-15.8971`
- `news_risk_high->equity_24h` score `6.4447` n `135` status `ready` deltaP `24.9074` edge `0.6059` maxDD `-9.4579`
- `market_context_high->crypto_alt_4h` score `3.9555` n `50` status `ready` deltaP `14.5122` edge `0.3622` maxDD `-7.6792`
- `market_context_high->crypto_major_1h` score `3.0382` n `50` status `ready` deltaP `15.6467` edge `0.1939` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.8315` n `50` status `ready` deltaP `31.9268` edge `0.0366` maxDD `-0.0791`
- `news_risk_high->metal_24h` score `2.8273` n `135` status `ready` deltaP `21.8866` edge `0.2171` maxDD `-2.192`
- `news_risk_high->index_24h` score `2.7577` n `135` status `ready` deltaP `26.2384` edge `0.1027` maxDD `-0.4916`
- `market_context_high->crypto_alt_1h` score `2.7358` n `50` status `ready` deltaP `13.7545` edge `0.2026` maxDD `-3.6387`
- `news_risk_high->equity_4h` score `2.0598` n `135` status `ready` deltaP `24.4455` edge `0.1688` maxDD `-9.143`
- `market_context_high->fx_1h` score `1.3549` n `50` status `ready` deltaP `19.2934` edge `0.0107` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.6539` n `135` status `ready` deltaP `7.6048` edge `0.0661` maxDD `-1.6514`
- `news_risk_high->crypto_alt_1h` score `0.6376` n `135` status `ready` deltaP `7.7545` edge `0.0925` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.3711` n `135` status `ready` deltaP `7.6203` edge `0.0089` maxDD `-0.302`
- `news_risk_high->crypto_alt_4h` score `0.3277` n `135` status `ready` deltaP `8.2159` edge `0.2385` maxDD `-15.9436`
- `market_context_high->commodity_1h` score `0.0261` n `50` status `ready` deltaP `9.1976` edge `-0.0056` maxDD `-2.1892`
- `market_context_high->equity_1h` score `-0.0896` n `50` status `ready` deltaP `-0.3952` edge `0.0562` maxDD `-1.2043`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
