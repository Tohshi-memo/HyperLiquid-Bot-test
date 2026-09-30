# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T23:52:32.683718+00:00`
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

- `market_context_high->unknown_1h` score `317.9825` n `50` status `ready` deltaP `6.6826` edge `26.4589` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `279.9518` n `50` status `ready` deltaP `6.7073` edge `23.2846` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `18.2078` n `135` status `ready` deltaP `28.9004` edge `1.3456` maxDD `-1.0093`
- `market_context_high->crypto_major_4h` score `6.8847` n `50` status `ready` deltaP `18.6098` edge `0.52` maxDD `-3.294`
- `news_risk_high->crypto_major_24h` score `6.3787` n `135` status `ready` deltaP `23.6459` edge `0.6893` maxDD `-15.8971`
- `news_risk_high->equity_24h` score `6.3316` n `135` status `ready` deltaP `24.213` edge `0.6011` maxDD `-9.4579`
- `market_context_high->crypto_alt_4h` score `3.8139` n `50` status `ready` deltaP `14.5122` edge `0.3504` maxDD `-7.6792`
- `market_context_high->crypto_major_1h` score `3.013` n `50` status `ready` deltaP `15.497` edge `0.1928` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.8715` n `50` status `ready` deltaP `32.2317` edge `0.0379` maxDD `-0.0791`
- `news_risk_high->index_24h` score `2.8277` n `135` status `ready` deltaP `26.9329` edge `0.1039` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `2.7635` n `135` status `ready` deltaP `21.5393` edge `0.2141` maxDD `-2.192`
- `market_context_high->crypto_alt_1h` score `2.6206` n `50` status `ready` deltaP `13.3054` edge `0.196` maxDD `-3.6387`
- `news_risk_high->equity_4h` score `2.2557` n `135` status `ready` deltaP `25.665` edge `0.177` maxDD `-9.143`
- `market_context_high->fx_1h` score `1.3741` n `50` status `ready` deltaP `19.4431` edge `0.0113` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.7186` n `135` status `ready` deltaP `8.2036` edge `0.0675` maxDD `-1.6514`
- `news_risk_high->crypto_alt_1h` score `0.5225` n `135` status `ready` deltaP `7.3054` edge `0.0859` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.3999` n `135` status `ready` deltaP `7.9197` edge `0.0093` maxDD `-0.302`
- `news_risk_high->crypto_alt_4h` score `0.1861` n `135` status `ready` deltaP `8.2159` edge `0.2267` maxDD `-15.9436`
- `market_context_high->commodity_1h` score `0.0044` n `50` status `ready` deltaP `9.3473` edge `-0.0071` maxDD `-2.3717`
- `market_context_high->equity_1h` score `-0.0476` n `50` status `ready` deltaP `0.2036` edge `0.0576` maxDD `-1.2043`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
