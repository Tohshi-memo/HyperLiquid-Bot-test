# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T00:52:29.706096+00:00`
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

- `market_context_high->unknown_1h` score `317.9993` n `50` status `ready` deltaP `6.5329` edge `26.4613` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `280.0946` n `50` status `ready` deltaP `6.7073` edge `23.2965` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `18.443` n `135` status `ready` deltaP `28.9004` edge `1.3652` maxDD `-1.0093`
- `market_context_high->crypto_major_4h` score `6.8207` n `50` status `ready` deltaP `18.3049` edge `0.5167` maxDD `-3.294`
- `news_risk_high->crypto_major_24h` score `6.3859` n `135` status `ready` deltaP `23.6459` edge `0.6899` maxDD `-15.8971`
- `news_risk_high->equity_24h` score `6.3532` n `135` status `ready` deltaP `24.213` edge `0.6029` maxDD `-9.4579`
- `market_context_high->crypto_alt_4h` score `3.8427` n `50` status `ready` deltaP `14.5122` edge `0.3528` maxDD `-7.6792`
- `market_context_high->crypto_major_1h` score `3.0154` n `50` status `ready` deltaP `15.497` edge `0.193` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.8545` n `50` status `ready` deltaP `32.0793` edge `0.0375` maxDD `-0.0791`
- `news_risk_high->index_24h` score `2.8102` n `135` status `ready` deltaP `26.7593` edge `0.1036` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `2.7839` n `135` status `ready` deltaP `21.5393` edge `0.2158` maxDD `-2.192`
- `market_context_high->crypto_alt_1h` score `2.6362` n `50` status `ready` deltaP `13.4551` edge `0.1963` maxDD `-3.6387`
- `news_risk_high->equity_4h` score `2.1978` n `135` status `ready` deltaP `25.3602` edge `0.1742` maxDD `-9.143`
- `market_context_high->fx_1h` score `1.3561` n `50` status `ready` deltaP `19.2934` edge `0.0108` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.7198` n `135` status `ready` deltaP `8.2036` edge `0.0676` maxDD `-1.6514`
- `news_risk_high->crypto_alt_1h` score `0.5381` n `135` status `ready` deltaP `7.4551` edge `0.0862` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.425` n `135` status `ready` deltaP `8.2191` edge `0.0094` maxDD `-0.302`
- `news_risk_high->crypto_alt_4h` score `0.2149` n `135` status `ready` deltaP `8.2159` edge `0.2291` maxDD `-15.9436`
- `market_context_high->commodity_1h` score `-0.0158` n `50` status `ready` deltaP `9.0479` edge `-0.0077` maxDD `-2.3717`
- `market_context_high->equity_1h` score `-0.0468` n `50` status `ready` deltaP `0.2036` edge `0.0577` maxDD `-1.2043`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
