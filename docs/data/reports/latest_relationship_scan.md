# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T03:22:31.664696+00:00`
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

- `market_context_high->unknown_1h` score `318.4528` n `50` status `ready` deltaP `6.6826` edge `26.4981` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `280.553` n `50` status `ready` deltaP `6.7073` edge `23.3347` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.018` n `135` status `ready` deltaP `29.2477` edge `1.4108` maxDD `-1.0093`
- `market_context_high->crypto_major_4h` score `6.9813` n `50` status `ready` deltaP `19.0671` edge `0.525` maxDD `-3.294`
- `news_risk_high->crypto_major_24h` score `6.4819` n `135` status `ready` deltaP `23.6459` edge `0.6979` maxDD `-15.8971`
- `news_risk_high->equity_24h` score `6.4315` n `135` status `ready` deltaP `24.9074` edge `0.6048` maxDD `-9.4579`
- `market_context_high->crypto_alt_4h` score `3.9965` n `50` status `ready` deltaP `14.6646` edge `0.3646` maxDD `-7.6792`
- `market_context_high->crypto_major_1h` score `2.9998` n `50` status `ready` deltaP `15.497` edge `0.1917` maxDD `-2.2692`
- `news_risk_high->metal_24h` score `2.8321` n `135` status `ready` deltaP `21.8866` edge `0.2175` maxDD `-2.192`
- `market_context_high->fx_4h` score `2.8267` n `50` status `ready` deltaP `31.9268` edge `0.0362` maxDD `-0.0791`
- `news_risk_high->index_24h` score `2.7156` n `135` status `ready` deltaP `25.8912` edge `0.1015` maxDD `-0.4916`
- `market_context_high->crypto_alt_1h` score `2.6339` n `50` status `ready` deltaP `13.1557` edge `0.1981` maxDD `-3.6387`
- `news_risk_high->equity_4h` score `1.9438` n `135` status `ready` deltaP `23.8358` edge `0.1632` maxDD `-9.143`
- `market_context_high->fx_1h` score `1.3932` n `50` status `ready` deltaP `19.7425` edge `0.0109` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.57` n `135` status `ready` deltaP `7.006` edge `0.0631` maxDD `-1.6514`
- `news_risk_high->crypto_alt_1h` score `0.5357` n `135` status `ready` deltaP `7.1557` edge `0.088` maxDD `-4.2849`
- `news_risk_high->crypto_alt_4h` score `0.3687` n `135` status `ready` deltaP `8.3683` edge `0.2409` maxDD `-15.9436`
- `news_risk_high->index_1h` score `0.316` n `135` status `ready` deltaP `7.0215` edge `0.0083` maxDD `-0.302`
- `market_context_high->commodity_1h` score `0.0129` n `50` status `ready` deltaP `9.0479` edge `-0.0063` maxDD `-2.1892`
- `market_context_high->equity_1h` score `-0.1441` n `50` status `ready` deltaP `-0.994` edge `0.0532` maxDD `-1.2043`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
