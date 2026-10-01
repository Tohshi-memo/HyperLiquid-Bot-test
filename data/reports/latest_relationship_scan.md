# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T08:22:38.145304+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6862`

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

- `market_context_high->unknown_1h` score `324.5463` n `50` status `ready` deltaP `7.2814` edge `27.0019` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `281.0068` n `50` status `ready` deltaP `6.8598` edge `23.3715` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.5259` n `124` status `ready` deltaP `29.1163` edge `1.454` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `8.7911` n `42` status `ready` deltaP `30.9027` edge `0.6682` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `6.4441` n `50` status `ready` deltaP `17.5427` edge `0.4904` maxDD `-3.294`
- `news_risk_high->equity_24h` score `5.7797` n `124` status `ready` deltaP `22.8046` edge `0.5645` maxDD `-9.4579`
- `news_risk_high->equity_4h` score `4.2101` n `124` status `ready` deltaP `28.3832` edge `0.2105` maxDD `-1.2436`
- `news_risk_high->crypto_major_24h` score `4.0888` n `124` status `ready` deltaP `21.7629` edge `0.6945` maxDD `-15.8971`
- `market_context_high->crypto_alt_24h` score `4.0103` n `42` status `ready` deltaP `14.0625` edge `0.4114` maxDD `-11.6768`
- `market_context_high->crypto_alt_4h` score `3.3306` n `50` status `ready` deltaP `12.8354` edge `0.3213` maxDD `-7.6792`
- `market_context_high->fx_4h` score `2.9594` n `50` status `ready` deltaP `33.4512` edge `0.0371` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `2.9471` n `50` status `ready` deltaP `14.8982` edge `0.1913` maxDD `-2.2692`
- `market_context_high->equity_24h` score `2.91` n `42` status `ready` deltaP `12.8968` edge `0.4733` maxDD `-11.8957`
- `news_risk_high->crypto_alt_4h` score `2.8597` n `124` status `ready` deltaP `12.1902` edge `0.3577` maxDD `-10.7193`
- `market_context_high->crypto_alt_1h` score `2.5967` n `50` status `ready` deltaP `12.5569` edge `0.199` maxDD `-3.6387`
- `news_risk_high->index_24h` score `2.5814` n `124` status `ready` deltaP `24.6192` edge `0.0988` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `2.1919` n `124` status `ready` deltaP `25.8625` edge `0.236` maxDD `-2.192`
- `market_context_high->fx_1h` score `1.4448` n `50` status `ready` deltaP `20.3413` edge `0.0112` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.7408` n `125` status `ready` deltaP `7.5581` edge `0.065` maxDD `-0.9592`
- `market_context_high->index_24h` score `0.4586` n `42` status `ready` deltaP `9.0278` edge `0.0557` maxDD `-1.2338`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
