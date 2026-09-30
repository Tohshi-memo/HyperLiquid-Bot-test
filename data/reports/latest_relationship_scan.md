# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T21:52:28.762424+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6836`

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

- `market_context_high->unknown_1h` score `318.1` n `50` status `ready` deltaP `7.2814` edge `26.4647` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `280.0958` n `50` status `ready` deltaP `6.7073` edge `23.2966` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `17.6695` n `135` status `ready` deltaP `28.7268` edge `1.3019` maxDD `-1.0093`
- `market_context_high->crypto_major_4h` score `7.0333` n `50` status `ready` deltaP `19.372` edge `0.5273` maxDD `-3.294`
- `news_risk_high->crypto_major_24h` score `6.3859` n `135` status `ready` deltaP `23.6459` edge `0.6899` maxDD `-15.8971`
- `news_risk_high->equity_24h` score `6.3268` n `135` status `ready` deltaP `24.213` edge `0.6007` maxDD `-9.4579`
- `market_context_high->crypto_alt_4h` score `3.7573` n `50` status `ready` deltaP `14.3598` edge `0.3467` maxDD `-7.6792`
- `market_context_high->crypto_major_1h` score `3.037` n `50` status `ready` deltaP `15.6467` edge `0.1938` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.8715` n `50` status `ready` deltaP `32.2317` edge `0.0379` maxDD `-0.0791`
- `news_risk_high->index_24h` score `2.8433` n `135` status `ready` deltaP `26.9329` edge `0.1052` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `2.7407` n `135` status `ready` deltaP `21.5393` edge `0.2122` maxDD `-2.192`
- `market_context_high->crypto_alt_1h` score `2.7022` n `50` status `ready` deltaP `13.7545` edge `0.1998` maxDD `-3.6387`
- `news_risk_high->equity_4h` score `2.3501` n `135` status `ready` deltaP `26.2748` edge `0.1808` maxDD `-9.143`
- `market_context_high->fx_1h` score `1.3729` n `50` status `ready` deltaP `19.4431` edge `0.0112` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.8456` n `135` status `ready` deltaP `9.4012` edge `0.0701` maxDD `-1.6514`
- `news_risk_high->crypto_alt_1h` score `0.604` n `135` status `ready` deltaP `7.7545` edge `0.0897` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.5053` n `135` status `ready` deltaP `9.1173` edge `0.0101` maxDD `-0.302`
- `news_risk_high->crypto_alt_4h` score `0.1295` n `135` status `ready` deltaP `8.0635` edge `0.223` maxDD `-15.9436`
- `market_context_high->equity_1h` score `0.035` n `50` status `ready` deltaP `1.4012` edge `0.0602` maxDD `-1.2043`
- `market_context_high->commodity_1h` score `0.006` n `50` status `ready` deltaP `9.3473` edge `-0.0069` maxDD `-2.3717`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
